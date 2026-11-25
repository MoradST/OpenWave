"""Review the latest version of one issue using the workflow's issue permissions."""
import json
import os
import subprocess

from job_posts import inspect_job, is_job


def api(path, method="GET", payload=None):
    args = ["gh", "api", "--method", method, path]
    if payload is not None:
        args += ["--input", "-"]
    result = subprocess.run(args, input=json.dumps(payload) if payload is not None else None,
                            check=True, text=True, stdout=subprocess.PIPE)
    return json.loads(result.stdout) if result.stdout.strip() else None


repo = os.environ["GITHUB_REPOSITORY"]
number = int(os.environ["ISSUE_NUMBER"])
path = f"repos/{repo}/issues/{number}"
issue = api(path)
if is_job(issue):
    errors, title = inspect_job(issue)
    labels = {label["name"] for label in issue["labels"]}
    for label, color in [("jobs", "215B91"), ("needs-details", "EAC54F")]:
        subprocess.run(["gh", "label", "create", label, "--repo", repo, "--color", color, "--force"], check=True)
    if errors:
        api(path + "/labels", "POST", {"labels": ["jobs", "needs-details"]})
        marker = "<!-- openwave-job-review -->"
        message = marker + "\nPlease edit this listing so it can appear in the Jobs feed.\n\n" + "\n".join("- " + error for error in errors)
        page = 1
        while True:
            comments = api(path + f"/comments?per_page=100&page={page}")
            prior = next((c for c in comments if c["user"]["login"] == "github-actions[bot]" and c["body"].startswith(marker)), None)
            if prior or len(comments) < 100:
                break
            page += 1
        if not prior:
            api(path + "/comments", "POST", {"body": message})
        elif prior["body"] != message:
            api(prior["url"], "PATCH", {"body": message})
    else:
        if title != issue["title"]:
            api(path, "PATCH", {"title": title})
        if "needs-details" in labels:
            api(path + "/labels/needs-details", "DELETE")
        if "jobs" not in labels and (title != issue["title"] or "role / position" in (issue.get("body") or "").lower()):
            api(path + "/labels", "POST", {"labels": ["jobs"]})
