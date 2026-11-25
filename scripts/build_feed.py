#!/usr/bin/env python3
"""Build a public, assistant-readable OpenWave activity index from GitHub Issues."""
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from job_posts import inspect_job, is_job

REPO = os.environ.get("GITHUB_REPOSITORY", "MoradST/OpenWave")
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
API = "https://api.github.com"
OUT = Path("docs/feed.json")
MAX_ISSUES = 1000

def get_pages(endpoint, params=None, limit=None):
    params = dict(params or {})
    params["per_page"] = 100
    result = []
    page = 1
    while True:
        params["page"] = page
        url = API + endpoint + "?" + urllib.parse.urlencode(params)
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "openwave-feed-indexer", "X-GitHub-Api-Version": "2022-11-28"}
        if TOKEN:
            headers["Authorization"] = "Bearer " + TOKEN
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=40) as response:
            batch = json.load(response)
        if not isinstance(batch, list):
            raise RuntimeError("Expected a list from GitHub API")
        result.extend(batch)
        if len(batch) < 100 or (limit and len(result) >= limit):
            break
        page += 1
    return result[:limit] if limit else result

def kind(title):
    if title.startswith("[Member]"):
        return "member"
    if title.startswith("[Brand]"):
        return "brand"
    if title.startswith("[Following]"):
        return "following"
    if title.startswith("[") and "]" in title:
        return "post"
    return "post"

def identity(user):
    return (user or {}).get("login")

def main():
    issues = get_pages("/repos/" + REPO + "/issues", {"state": "all", "sort": "created", "direction": "desc"}, MAX_ISSUES)
    posts, members, brands, comments = [], [], [], []
    for issue in issues:
        if "pull_request" in issue:
            continue
        category = kind(issue.get("title", ""))
        if category == "following":
            continue
        item = {
            "id": issue["number"], "title": issue["title"], "url": issue["html_url"],
            "author": identity(issue.get("user")), "created_at": issue["created_at"],
            "updated_at": issue["updated_at"], "state": issue["state"],
            "comment_count": issue.get("comments", 0)
        }
        if category == "member":
            members.append(item)
        elif category == "brand":
            brands.append(item)
        else:
            item["category"] = issue["title"].split("]", 1)[0][1:] if issue["title"].startswith("[") else "General"
            if is_job(issue):
                errors, item["title"] = inspect_job(issue)
                if errors:
                    continue
                item["category"] = "Jobs"
            posts.append(item)
        if issue.get("comments", 0):
            for comment in get_pages("/repos/" + REPO + "/issues/" + str(issue["number"]) + "/comments"):
                comments.append({
                    "id": comment["id"], "issue_id": issue["number"],
                    "author": identity(comment.get("user")), "url": comment["html_url"],
                    "created_at": comment["created_at"], "updated_at": comment["updated_at"]
                })
    for items in (posts, members, brands, comments):
        items.sort(key=lambda x: (x["created_at"], x["id"]), reverse=True)
    feed = {
        "schema_version": 1, "repository": REPO,
        "assistant_guide_url": "https://github.com/MoradST/OpenWave/blob/main/OPENWAVE_AI.md",
        "assistant_guide_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "coverage": {"issue_limit": MAX_ISSUES, "issues_fetched": len(issues), "historical_coverage_complete": len(issues) < MAX_ISSUES},
        "posts": posts, "members": members, "brands": brands, "comments": comments
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(feed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Indexed %d posts, %d members, %d brands, %d comments" % (len(posts), len(members), len(brands), len(comments)))

if __name__ == "__main__":
    main()
