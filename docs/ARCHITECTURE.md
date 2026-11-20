# OpenWave architecture — v0.1

## Goal

A public, topic-based social feed which multiple users can read and update through their own AI assistants, without operating a proprietary social app.

## Data model

**One post = one GitHub Issue** in `MoradST/OpenWave`.

- `number`: GitHub-generated unique post identifier.
- `title`: e.g. `[Technology] New release`.
- `body`: begins with exact searchable `Topic: technology`, `Topic: traffic` or `Topic: general`.
- `user.login`: GitHub-authorized publishing identity.
- `created_at`: server timestamp.
- `html_url`: stable reference for reading and sharing.
- `comments`: discussion and replies.
- `state`: open or closed; **do not treat closed as automatically false**.

The issue form provides a consistent human publishing surface. The programmatic path uses GitHub's Issues API via the user's authorized GitHub connector.

## Flow

```text
User → own ChatGPT → connected GitHub create_issue → public Issue
User → own ChatGPT → connected GitHub search_issues → summary and links
User → github.com → Issue form / Issue feed
```

No Git branches, PR approvals, automatic bot tokens or owner intervention are required for routine posting.

## Constraints

- Creating Issues requires GitHub authentication; repository must permit Issues and GitHub may apply platform restrictions.
- Search may be eventually consistent and rate limited; assistant connectors may not be universally installed.
- Open/public does NOT mean anonymous. GitHub identity and its terms apply.
- GitHub Issues are not optimized as a large social-feed database or live location service.
- Topic indexing currently relies on consistent body strings. A future version may use labels and a small ingestion service.
- v0.1 has **no custom web service, no automatic verification, no content ranking, no federated identity**, and no live-traffic accuracy guarantees.
- GitHub abuse reporting, deletion and account restrictions are platform safety backstops, not comprehensive automated moderation.
- In the current proof of concept, no separate OpenWave rate limiter exists; GitHub's own controls apply.

## Acceptance test

1. User A creates an Issue from their own GitHub-connected ChatGPT.
2. User B (separate account and ChatGPT connection) finds the Issue by searching the repository.
3. User B creates another Issue.
4. User A can read it.
5. Repeat in voice mode, recording whether GitHub actions are available there.
6. Check topic filtering, post timestamps and attribution.

Passing the first four steps establishes a text-chat cross-user MVP. Voice support is a separate test.
