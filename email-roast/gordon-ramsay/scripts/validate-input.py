#!/usr/bin/env python3
"""Validate a cold-email prospect/campaign JSON file before writing any copy.

Checks the things that quietly ruin a send: blank values, unrendered merge tags,
malformed emails and URLs, unsupported verification statuses, duplicate record
IDs, suppression matches, and stale signals.

Usage:
    python3 validate-input.py prospects.json
    python3 validate-input.py prospects.json --json
    python3 validate-input.py prospects.json --strict --today 2026-07-26

Exit codes:
    0   clean, or warnings only
    1   critical errors (or any warning under --strict)
    2   file missing, unreadable, or not the expected shape

Standard library only. Field names and aliases match references/enrichment-schema.md.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from urllib.parse import urlsplit

# --------------------------------------------------------------------------
# Schema constants — keep in sync with references/enrichment-schema.md
# --------------------------------------------------------------------------

CAMPAIGN_ALIASES = {
    "icp_definition": "icp", "target_icp": "icp", "ideal_customer_profile": "icp",
    "pain": "problem", "pain_point": "problem", "problem_addressed": "problem",
    "use_case": "problem",
    "value_prop": "offer", "solution": "offer", "pitch": "offer", "what_we_do": "offer",
    "desired_cta": "cta", "ask": "cta", "call_to_action": "cta", "next_step": "cta",
    "case_study": "proof", "social_proof": "proof", "evidence": "proof", "results": "proof",
    "sender_bio": "sender_credibility", "credibility": "sender_credibility",
    "about_sender": "sender_credibility",
    "voice": "tone", "style": "tone",
    "word_limit": "max_words", "max_length": "max_words",
    "banned_claims": "prohibited_claims", "legal_restrictions": "prohibited_claims",
    "do_not_say": "prohibited_claims",
    "suppressed_domains": "suppression_list", "dnc_list": "suppression_list",
    "exclusions": "suppression_list",
}

PROSPECT_ALIASES = {
    "id": "record_id", "row_id": "record_id", "uuid": "record_id",
    "crm_id": "record_id", "contact_id": "record_id",
    "first": "first_name", "fname": "first_name", "given_name": "first_name",
    "firstname": "first_name",
    "last": "last_name", "lname": "last_name", "surname": "last_name",
    "family_name": "last_name", "lastname": "last_name",
    "title": "job_title", "position": "job_title", "role": "job_title",
    "jobtitle": "job_title",
    "level": "seniority", "seniority_level": "seniority",
    "function": "department", "team": "department", "dept": "department",
    "city": "location", "geo": "location", "region": "location", "country": "location",
    "linkedin": "linkedin_url", "li_url": "linkedin_url",
    "linkedin_profile": "linkedin_url", "person_linkedin": "linkedin_url",
    "work_email": "email", "email_address": "email", "business_email": "email",
    "email_status": "verification_status", "email_verification": "verification_status",
    "verification": "verification_status", "deliverability": "verification_status",
    "company": "company_name", "account": "company_name", "organization": "company_name",
    "org": "company_name", "employer": "company_name",
    "website": "domain", "company_domain": "domain", "url": "domain",
    "company_website": "domain",
    "sector": "industry", "vertical": "industry", "naics_description": "industry",
    "headcount": "employee_count", "size": "employee_count",
    "employees": "employee_count", "company_size": "employee_count",
    "revenue": "estimated_revenue", "arr": "estimated_revenue",
    "annual_revenue": "estimated_revenue",
    "stage": "funding_stage", "last_round": "funding_stage", "funding": "funding_stage",
    "technologies": "tech_stack", "technology_stack": "tech_stack",
    "tools": "tech_stack", "stack": "tech_stack",
    "model": "business_model", "gtm_model": "business_model",
    "market": "target_market", "segment": "target_market",
    "customer_segment": "target_market",
    "company_linkedin": "company_linkedin_url", "org_linkedin": "company_linkedin_url",
    "dnc": "do_not_contact", "opt_out": "opted_out",
}

VERIFICATION_ALIASES = {
    "valid": "verified", "deliverable": "verified", "ok": "verified", "safe": "verified",
    "accept_all": "catch_all", "acceptall": "catch_all", "catchall": "catch_all",
    "undeliverable": "invalid", "bounced": "invalid", "bad": "invalid",
}
VERIFICATION_STATUSES = {
    "verified", "catch_all", "risky", "unknown", "invalid", "unverified",
}
UNSENDABLE_STATUSES = {"invalid"}

SIGNAL_TYPES = {
    "recent_funding", "recent_hiring", "leadership_change", "job_posting",
    "product_launch", "expansion", "technology_adoption", "website_change",
    "linkedin_activity", "company_news", "intent_signal",
}

SUPPRESSION_FLAGS = ("suppressed", "do_not_contact", "opted_out", "unsubscribed", "dnc")
SUPPRESSION_STATUSES = {
    "suppressed", "dnc", "do_not_contact", "opted_out", "unsubscribed", "blocked",
}

REQUIRED_CAMPAIGN = ("icp", "problem", "offer", "cta")
REQUIRED_PROSPECT = ("first_name", "job_title", "company_name")
CONTACTABLE = ("email", "domain", "linkedin_url")
URL_FIELDS = ("linkedin_url", "company_linkedin_url", "source_url")

PLACEHOLDERS = {
    "", "-", "--", "n/a", "na", "n.a.", "#n/a", "null", "none", "nil",
    "unknown", "tbd", "tba", "?", "not available", "not found", "undefined", "nan",
}
MERGE_TAG = re.compile(r"(\{\{.*?\}\}|\{%.*?%\}|\[\[.*?\]\]|<<.*?>>|%%.+?%%|\$\{.*?\})")
EMAIL_RE = re.compile(r"^[A-Za-z0-9!#$%&'*+/=?^_`{|}~.-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+$")
HOSTNAME_RE = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))+$")
CONFIDENCE_WORDS = {"high": 0.9, "medium": 0.6, "med": 0.6, "low": 0.3,
                    "a": 0.95, "b": 0.75, "c": 0.5, "d": 0.25}

STALE_DAYS = 120
CRITICAL = "ERROR"
WARNING = "WARN"
NOTE = "INFO"


# --------------------------------------------------------------------------
# Findings
# --------------------------------------------------------------------------

class Report:
    def __init__(self) -> None:
        self.findings: list[dict] = []

    def add(self, severity: str, record: str, field: str, code: str, message: str) -> None:
        self.findings.append({
            "severity": severity, "record": record,
            "field": field, "code": code, "message": message,
        })

    def error(self, *a) -> None:
        self.add(CRITICAL, *a)

    def warn(self, *a) -> None:
        self.add(WARNING, *a)

    def info(self, *a) -> None:
        self.add(NOTE, *a)

    def count(self, severity: str) -> int:
        return sum(1 for f in self.findings if f["severity"] == severity)

    def sort(self) -> None:
        """Most severe first, then by record, so text and JSON output agree."""
        order = {CRITICAL: 0, WARNING: 1, NOTE: 2}
        self.findings.sort(key=lambda f: (order[f["severity"]], f["record"]))


# --------------------------------------------------------------------------
# Normalization
# --------------------------------------------------------------------------

def simple_key(key: str) -> str:
    k = re.sub(r"[\s\-./]+", "_", str(key).strip().lower())
    return re.sub(r"_+", "_", k).strip("_")


def camel_key(key: str) -> str:
    return simple_key(re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", str(key)))


def normalize(record: dict, aliases: dict) -> tuple[dict, dict]:
    """Return (canonical record, canonical -> original key name)."""
    out: dict = {}
    origin: dict = {}
    for raw_key, value in record.items():
        canonical = None
        for candidate in (simple_key(raw_key), camel_key(raw_key)):
            canonical = aliases.get(candidate, candidate if candidate in _KNOWN else None)
            if canonical:
                break
        canonical = canonical or simple_key(raw_key)
        if canonical in out and out[canonical] not in (None, ""):
            continue  # first mapped value wins
        out[canonical] = value
        origin[canonical] = str(raw_key)
    return out, origin


_KNOWN = (
    set(CAMPAIGN_ALIASES.values()) | set(PROSPECT_ALIASES.values())
    | set(REQUIRED_CAMPAIGN) | set(REQUIRED_PROSPECT) | set(CONTACTABLE)
    | set(SUPPRESSION_FLAGS) | {
        "seniority", "department", "location", "last_name", "verification_status",
        "industry", "employee_count", "estimated_revenue", "funding_stage",
        "tech_stack", "business_model", "target_market", "company_linkedin_url",
        "signals", "suppression_status", "custom_fields", "proof", "tone",
        "max_words", "prohibited_claims", "suppression_list", "sender_credibility",
    }
)


def is_blank(value) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip().lower() in PLACEHOLDERS
    if isinstance(value, (list, dict)):
        return len(value) == 0
    return False


def unrendered_tag(value) -> str | None:
    if isinstance(value, str):
        hit = MERGE_TAG.search(value)
        if hit:
            return hit.group(0)
    return None


# --------------------------------------------------------------------------
# Field checks
# --------------------------------------------------------------------------

def check_email(value: str) -> str | None:
    """Return an error message, or None if the address parses."""
    addr = value.strip()
    if " " in addr or addr.count("@") != 1:
        return "not a single well-formed address"
    local, _, host = addr.partition("@")
    if not local or len(local) > 64:
        return "empty or over-long local part"
    if local.startswith(".") or local.endswith(".") or ".." in local:
        return "misplaced dots in the local part"
    if not EMAIL_RE.match(addr) or ".." in host:
        return "invalid syntax"
    if host.split(".")[-1].isdigit():
        return "numeric TLD"
    return None


def check_url(value: str) -> str | None:
    raw = value.strip()
    if any(c.isspace() for c in raw):
        return "contains whitespace"
    parts = urlsplit(raw if "//" in raw else "//" + raw)
    if "//" in raw and parts.scheme not in ("http", "https", ""):
        return f"unsupported scheme '{parts.scheme}'"
    host = (parts.hostname or "").strip()
    if not host or not HOSTNAME_RE.match(host):
        return "no valid hostname"
    return None


def check_domain(value: str) -> str | None:
    raw = value.strip().rstrip("/")
    host = urlsplit(raw if "//" in raw else "//" + raw).hostname or ""
    if not HOSTNAME_RE.match(host):
        return "not a valid domain"
    return None


def domain_of(value: str) -> str:
    raw = str(value).strip().rstrip("/").lower()
    host = urlsplit(raw if "//" in raw else "//" + raw).hostname or raw
    return host[4:] if host.startswith("www.") else host


def parse_iso(value) -> date | None:
    if isinstance(value, str):
        try:
            return datetime.strptime(value.strip()[:10], "%Y-%m-%d").date()
        except ValueError:
            return None
    return None


def normalized_confidence(value) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        num = float(value)
        return num / 100 if num > 1 else num
    if isinstance(value, str):
        return CONFIDENCE_WORDS.get(value.strip().lower())
    return None


# --------------------------------------------------------------------------
# Record validation
# --------------------------------------------------------------------------

def validate_campaign(raw: dict | None, report: Report) -> dict:
    if not isinstance(raw, dict) or not raw:
        report.error("campaign", "campaign", "missing_campaign",
                     "no campaign block — offer, problem, icp and cta are all unknown")
        return {}

    campaign, origin = normalize(raw, CAMPAIGN_ALIASES)
    for field in REQUIRED_CAMPAIGN:
        if field not in campaign:
            report.error("campaign", field, "missing_required",
                         f"required campaign field '{field}' is absent")
        elif is_blank(campaign[field]):
            report.error("campaign", origin.get(field, field), "blank_value",
                         f"'{field}' is present but blank")

    for field, value in campaign.items():
        tag = unrendered_tag(value)
        if tag:
            report.error("campaign", origin.get(field, field), "unrendered_tag",
                         f"unrendered merge tag {tag}")

    max_words = campaign.get("max_words")
    if max_words is not None and not is_blank(max_words):
        try:
            if not 20 <= int(max_words) <= 300:
                report.warn("campaign", "max_words", "implausible_value",
                            f"max_words={max_words} is outside the usable 20-300 range")
        except (TypeError, ValueError):
            report.warn("campaign", "max_words", "bad_type",
                        f"max_words={max_words!r} is not a number")

    if is_blank(campaign.get("proof")):
        report.info("campaign", "proof", "no_proof",
                    "no proof supplied — the email must omit the proof line, not invent one")
    if campaign.get("prohibited_claims"):
        report.info("campaign", "prohibited_claims", "constraints",
                    f"{len(campaign['prohibited_claims'])} prohibited claim(s) to honour")
    return campaign


def validate_signals(signals, rid: str, today: date, report: Report) -> None:
    if is_blank(signals):
        report.warn(rid, "signals", "no_signal",
                    "no why-now signal — trigger quality caps at 4, account-level only")
        return
    if not isinstance(signals, list):
        report.error(rid, "signals", "bad_type", "signals must be a list of objects")
        return

    for i, signal in enumerate(signals):
        field = f"signals[{i}]"
        if not isinstance(signal, dict):
            report.error(rid, field, "bad_type", "signal is not an object")
            continue

        stype = str(signal.get("type", "")).strip().lower()
        if not stype:
            report.warn(rid, f"{field}.type", "missing_field", "signal has no type")
        elif stype not in SIGNAL_TYPES:
            report.warn(rid, f"{field}.type", "unknown_signal_type",
                        f"'{stype}' is not a recognized signal type")

        if is_blank(signal.get("summary")):
            report.warn(rid, f"{field}.summary", "blank_value",
                        "signal has no summary — nothing to anchor an opener on")

        url = signal.get("source_url")
        if is_blank(url):
            report.warn(rid, f"{field}.source_url", "unverified_signal",
                        "no source URL — signal is UNVERIFIED and cannot be stated as fact")
        else:
            problem = check_url(str(url))
            if problem:
                report.error(rid, f"{field}.source_url", "invalid_url",
                             f"{problem}: {url!r}")

        raw_date = signal.get("source_date")
        if is_blank(raw_date):
            report.warn(rid, f"{field}.source_date", "undated_signal",
                        "no source date — treated as 121-180 days old, never called recent")
        else:
            parsed = parse_iso(raw_date)
            if parsed is None:
                report.error(rid, f"{field}.source_date", "invalid_date",
                             f"not an ISO date (YYYY-MM-DD): {raw_date!r}")
            elif parsed > today:
                report.error(rid, f"{field}.source_date", "future_date",
                             f"dated in the future: {raw_date}")
            else:
                age = (today - parsed).days
                if age > STALE_DAYS:
                    report.warn(rid, f"{field}.source_date", "stale_signal",
                                f"{age} days old — stale, do not present as news")

        if "confidence" in signal and not is_blank(signal["confidence"]):
            conf = normalized_confidence(signal["confidence"])
            if conf is None:
                report.warn(rid, f"{field}.confidence", "bad_confidence",
                            f"unrecognized confidence value {signal['confidence']!r}")
            elif conf < 0.5:
                report.warn(rid, f"{field}.confidence", "low_confidence",
                            f"confidence {conf:.2f} — may guide targeting, not assertion")


def validate_prospect(raw: dict, index: int, campaign: dict, today: date,
                      report: Report) -> dict:
    prospect, origin = normalize(raw, PROSPECT_ALIASES)
    rid = str(prospect.get("record_id") or "").strip()
    if not rid or is_blank(rid):
        rid = f"row_{index + 1}"
        report.warn(rid, "record_id", "missing_record_id",
                    "no record_id — generated one, but batch output will not round-trip")
    prospect["record_id"] = rid

    # Required fields, blanks, and unrendered merge tags.
    for field in REQUIRED_PROSPECT:
        if field not in prospect:
            report.error(rid, field, "missing_required",
                         f"required field '{field}' is absent")
        elif is_blank(prospect[field]):
            report.error(rid, origin.get(field, field), "blank_value",
                         f"'{field}' is present but blank")

    for field, value in prospect.items():
        if field.startswith("_") or field == "signals":
            continue  # signals get their own pass below
        tag = unrendered_tag(value)
        if tag:
            severity = report.error if field in REQUIRED_PROSPECT else report.warn
            severity(rid, origin.get(field, field), "unrendered_tag",
                     f"unrendered merge tag {tag} — this would ship literally")
        elif field not in REQUIRED_PROSPECT and is_blank(value):
            report.warn(rid, origin.get(field, field), "blank_value",
                        f"'{field}' is present but blank")

    if not any(not is_blank(prospect.get(f)) for f in CONTACTABLE):
        report.error(rid, "email|domain|linkedin_url", "unreachable",
                     "no email, domain or LinkedIn URL — the record cannot be resolved")

    # Email syntax and verification status.
    email = prospect.get("email")
    if not is_blank(email):
        problem = check_email(str(email))
        if problem:
            report.error(rid, origin.get("email", "email"), "invalid_email",
                         f"{problem}: {email!r}")

    status_raw = prospect.get("verification_status")
    status = None
    if is_blank(status_raw):
        if not is_blank(email):
            report.warn(rid, "verification_status", "unverified",
                        "no verification status — treated as unverified, half email confidence")
    else:
        key = simple_key(str(status_raw))
        status = VERIFICATION_ALIASES.get(key, key)
        if status not in VERIFICATION_STATUSES:
            report.error(rid, origin.get("verification_status", "verification_status"),
                         "unsupported_status",
                         f"'{status_raw}' is not a supported verification status "
                         f"({', '.join(sorted(VERIFICATION_STATUSES))})")
        elif status in UNSENDABLE_STATUSES:
            report.error(rid, "verification_status", "undeliverable",
                         f"status '{status}' — this address will bounce")
        elif status in ("catch_all", "risky", "unknown"):
            report.warn(rid, "verification_status", "weak_verification",
                        f"status '{status}' — half email confidence, send check VERIFY FIRST")

    # URLs and domain.
    for field in URL_FIELDS:
        value = prospect.get(field)
        if not is_blank(value):
            problem = check_url(str(value))
            if problem:
                report.error(rid, origin.get(field, field), "invalid_url",
                             f"{problem}: {value!r}")
            elif field == "linkedin_url" and "linkedin." not in str(value).lower():
                report.warn(rid, origin.get(field, field), "not_linkedin",
                            f"linkedin_url does not point at LinkedIn: {value!r}")

    domain = prospect.get("domain")
    if not is_blank(domain):
        problem = check_domain(str(domain))
        if problem:
            report.error(rid, origin.get("domain", "domain"), "invalid_domain",
                         f"{problem}: {domain!r}")
        elif not is_blank(email) and "@" in str(email):
            email_host = domain_of(str(email).split("@")[-1])
            record_host = domain_of(str(domain))
            if email_host and record_host and email_host != record_host \
                    and not email_host.endswith("." + record_host) \
                    and not record_host.endswith("." + email_host):
                report.warn(rid, "email|domain", "domain_mismatch",
                            f"email host '{email_host}' does not match domain "
                            f"'{record_host}' — one of them is wrong")

    # Suppression.
    reasons = [f for f in SUPPRESSION_FLAGS if prospect.get(f) is True
               or str(prospect.get(f, "")).strip().lower() == "true"]
    sup_status = simple_key(str(prospect.get("suppression_status", "")))
    if sup_status in SUPPRESSION_STATUSES:
        reasons.append(f"suppression_status={sup_status}")

    raw_list = campaign.get("suppression_list") or []
    if isinstance(raw_list, str):
        raw_list = [raw_list]
    suppression_list = {domain_of(str(d)) for d in raw_list}
    for candidate in (prospect.get("domain"), str(email).split("@")[-1] if email else None):
        if candidate and domain_of(str(candidate)) in suppression_list:
            reasons.append(f"domain on campaign suppression_list ({domain_of(str(candidate))})")
            break

    if reasons:
        report.error(rid, "suppression", "suppressed",
                     "DO NOT CONTACT — " + "; ".join(dict.fromkeys(reasons)))
    prospect["_suppressed"] = bool(reasons)

    validate_signals(prospect.get("signals"), rid, today, report)
    return prospect


def check_duplicates(prospects: list[dict], report: Report) -> None:
    by_id: dict[str, str] = {}
    by_email: dict[str, str] = {}
    by_person: dict[tuple, str] = {}

    for prospect in prospects:
        rid = prospect["record_id"]

        if rid in by_id:
            report.error(rid, "record_id", "duplicate_record_id",
                         f"record_id '{rid}' already used by an earlier row — "
                         "results cannot be matched back reliably")
        else:
            by_id[rid] = rid

        email = prospect.get("email")
        if not is_blank(email):
            key = str(email).strip().lower()
            if key in by_email:
                report.warn(rid, "email", "duplicate_contact",
                            f"same work email as {by_email[key]} — duplicate_of that record")
                continue
            by_email[key] = rid

        name = " ".join(str(prospect.get(f, "")).strip().lower()
                        for f in ("first_name", "last_name")).strip()
        host = domain_of(str(prospect.get("domain", ""))) if prospect.get("domain") else ""
        if name and host:
            key = (name, host)
            if key in by_person:
                report.warn(rid, "first_name|last_name|domain", "duplicate_contact",
                            f"same person and domain as {by_person[key]} — likely duplicate")
            else:
                by_person[key] = rid


# --------------------------------------------------------------------------
# Input loading
# --------------------------------------------------------------------------

def load(path: str) -> tuple[dict | None, list]:
    try:
        with open(path, encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError:
        sys.exit(f"validate-input: no such file: {path}")
    except UnicodeDecodeError as exc:
        sys.exit(f"validate-input: {path} is not valid UTF-8: {exc}")
    except json.JSONDecodeError as exc:
        sys.exit(f"validate-input: {path} is not valid JSON: line {exc.lineno}, {exc.msg}")

    if isinstance(payload, list):
        return None, payload
    if not isinstance(payload, dict):
        sys.exit("validate-input: expected a JSON object or array at the top level")

    keys = {simple_key(k): k for k in payload}
    campaign = payload.get(keys.get("campaign", "campaign"))
    for name in ("prospects", "records", "rows", "contacts", "leads", "data", "prospect"):
        if name in keys:
            value = payload[keys[name]]
            return campaign, value if isinstance(value, list) else [value]

    if campaign is None:
        return None, [payload]  # a bare prospect object
    return campaign, []


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

def print_report(report: Report, path: str, total: int, suppressed: int,
                 exit_code: int) -> None:
    findings = report.findings
    print(f"validate-input · {path}")
    print(f"{total} prospect record(s) · {report.count(CRITICAL)} error(s) · "
          f"{report.count(WARNING)} warning(s) · {report.count(NOTE)} note(s)")

    if findings:
        print()
        width = max(len(f["record"]) for f in findings)
        for finding in findings:
            print(f"  {finding['severity']:<5} {finding['record']:<{width}}  "
                  f"{finding['field']}: {finding['message']}")

    print()
    if suppressed:
        print(f"  {suppressed} record(s) suppressed — generate no copy for these.")
    if exit_code == 0:
        print("  PASS — no critical errors. Safe to proceed to the audit.")
    else:
        print("  FAIL — fix the errors above before writing copy.")


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="validate-input.py",
        description="Validate cold-email prospect and campaign data before writing copy.",
        epilog="Exit codes: 0 clean or warnings only · 1 critical errors · 2 bad input file.",
    )
    parser.add_argument("path", help="path to a JSON file")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="emit machine-readable JSON instead of a text report")
    parser.add_argument("--strict", action="store_true",
                        help="treat warnings as critical")
    parser.add_argument("--allow-suppressed", action="store_true",
                        help="downgrade suppression matches to warnings")
    parser.add_argument("--today", metavar="YYYY-MM-DD",
                        help="override today's date for signal-age checks")
    args = parser.parse_args()

    today = date.today()
    if args.today:
        parsed = parse_iso(args.today)
        if parsed is None:
            sys.exit(f"validate-input: --today must be YYYY-MM-DD, got {args.today!r}")
        today = parsed

    raw_campaign, raw_prospects = load(args.path)
    report = Report()
    campaign = validate_campaign(raw_campaign, report)

    if not raw_prospects:
        report.error("input", "prospects", "no_prospects", "no prospect records found")

    prospects = []
    for index, raw in enumerate(raw_prospects):
        if not isinstance(raw, dict):
            report.error(f"row_{index + 1}", "record", "bad_type",
                         "prospect entry is not an object")
            continue
        prospects.append(validate_prospect(raw, index, campaign, today, report))

    check_duplicates(prospects, report)

    if args.allow_suppressed:
        for finding in report.findings:
            if finding["code"] == "suppressed":
                finding["severity"] = WARNING

    report.sort()
    suppressed = sum(1 for p in prospects if p.get("_suppressed"))
    exit_code = 1 if report.count(CRITICAL) else 0
    if args.strict and report.count(WARNING):
        exit_code = 1

    if args.as_json:
        print(json.dumps({
            "file": args.path,
            "ok": exit_code == 0,
            "exit_code": exit_code,
            "records": len(prospects),
            "suppressed": suppressed,
            "counts": {
                "errors": report.count(CRITICAL),
                "warnings": report.count(WARNING),
                "notes": report.count(NOTE),
            },
            "findings": report.findings,
        }, indent=2))
    else:
        print_report(report, args.path, len(prospects), suppressed, exit_code)

    return exit_code


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as exc:
        if isinstance(exc.code, str):  # sys.exit("message") → usage failure
            print(exc.code, file=sys.stderr)
            sys.exit(2)
        raise
