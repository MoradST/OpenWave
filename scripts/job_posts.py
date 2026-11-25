"""Recognize OpenWave job submissions and explain missing listing details."""
import re


def sections(body):
    parts = re.split(r"(?m)^#{1,6}[ \t]+(.+?)[ \t]*\r?$", body)
    return {key.strip().lower(): value.strip() for key, value in zip(parts[1::2], parts[2::2])}


def is_job(issue):
    title, body = issue["title"], issue.get("body") or ""
    return bool(re.match(r"^(?:\[jobs\]|💼\s*Job opportunity)", title, re.I)
                or re.search(r"(?im)^Topic:\s*jobs[ \t]*\r?$", body)
                or any(label["name"].lower() == "jobs" for label in issue.get("labels", []))
                or {"role / position", "official application link"} <= sections(body).keys())


def substantive(value):
    value = value.strip()
    return (bool(re.search(r"[^\W\d_]", value)) and not re.fullmatch(
        r"(?:n/?a|tbd|_?no response_?|not specified|unknown|[-.]+)", value, re.I)
        and not re.match(r"^(?:(?:please )?(?:see|check|visit|refer to)\b|https?://)", value, re.I))


def inspect_job(issue):
    body = issue.get("body") or ""
    fields = sections(body)
    title = issue["title"]
    # Jobs also hosts hiring conversations. Validate listings, not discussions.
    match = re.match(r"^\[Jobs\]\s+(.+?) at (.+?)(?:\s+\|\s+(.+))?$", title, re.I)
    form = "role / position" in fields or "company or organization" in fields
    if not (form or match or re.search(r"(?i)job opportunity|job opening|vacancy|hiring at", title)
            or any(label["name"] == "jobs" for label in issue.get("labels", []))
            or re.search(r"\[.*?apply.*?\]\(|https?://(?:jobs|careers)\.|^#{1,6} (?:responsibilities|requirements|official application link)", body, re.I | re.M) or re.fullmatch(r"(?:Topic: jobs\s+)?https?://\S+", body.strip(), re.I)):
        return [], title
    role, company, location = match.groups() if match else ("", "", "")
    role = fields.get("role / position", role)
    company = fields.get("company or organization", company)
    location = fields.get("location and work model", location) or ""
    errors = []
    if not substantive(role) or re.fullmatch(r"(?:REF|REQ|JOB|JR)?[-#\s]*\d[\w-]*", role, re.I):
        errors.append("Add the role name from the employer’s listing.")
    if not substantive(company):
        errors.append("Add the hiring company.")
    details = fields.get("role details", fields.get("what you’ll build", fields.get("responsibilities", "")))
    if not substantive(details) or len(details.split()) < 4:
        errors.append("Describe what someone in this role will do under Responsibilities.")
    qualifications = fields.get("requirements", fields.get("what you’ll bring", ""))
    if not substantive(qualifications) and not (form and "requirements" not in fields and "role details" in fields and re.search(r"experience|qualifications|requirements", details, re.I)):
        errors.append("List the qualifications under Requirements, or say the employer did not specify them.")
    links = fields.get("official application link", "") if form else body
    if not re.search(r"https?://[^\s/)]+\.[^\s/)]+(?:/[^\s)]*)?", links):
        errors.append("Include the employer’s application URL.")
    new_title = f"[Jobs] {role} at {company}"
    if substantive(location):
        new_title += " | " + location
    if form and (len(new_title) > 256 or "\n" in new_title):
        errors.append("Keep role, company and location short enough for a single issue title.")
    return errors, new_title if form and not errors else title
