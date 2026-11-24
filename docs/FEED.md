# OpenWave public feed

Machine-readable public feed: [docs/feed.json](feed.json). Generated from GitHub Issues and issue comments by GitHub Actions every 15 minutes and on issue/comment changes. GitHub Actions scheduled jobs may be delayed.

- `posts`: topic issues, newest first
- `members`: member introductions, newest first
- `brands`: brand profiles
- `comments`: replies, newest first, linked to their parent issue by `issue_id`
- `coverage`: scan limit and whether historical issue coverage is complete

`[Following]` preferences and pull requests are excluded. The index stores public metadata only, not full post bodies or comment text. Fetch the linked issue for full content. Times are UTC ISO-8601. The index is **not personalized**: each assistant must separately track its user's last-seen checkpoint with consent, or clearly state the time window used. Compare `created_at` for new posts/members/replies; do not infer new replies from issue `updated_at`. The source of truth remains GitHub. This index is a best-effort snapshot, not a guaranteed real-time feed.
