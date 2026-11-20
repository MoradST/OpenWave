# Follow the People — X conversations

OpenWave is **human-first**. Rather than ingesting viral posts from X at random, this feature will help OpenWave members discover conversations initiated by people and organizations who **explicitly opt in**.

## Status (November 2026)

**Opt-in profile fields are implemented. Automatic X discovery is NOT implemented or enabled.** There is no live connection to X yet, no scraping and no automated posting. A working integration requires API credentials, review of X's applicable terms and endpoint limits, and a controlled scheduled workflow.

## How to opt in

1. Create a [Member profile](https://github.com/MoradST/OpenWave/issues/new?template=member.yml) or [Brand profile](https://github.com/MoradST/OpenWave/issues/new?template=brand.yml).
2. Enter your own public X profile URL.
3. Select **Yes — opt in to future conversation discovery**.
4. Existing members: edit your own profile Issue to include:

```text
X profile: https://x.com/yourhandle
X discovery: yes
```

No consent should be inferred from the presence of a link alone. An opt-in without a valid public account URL is not actionable. Members can revoke consent at any time by editing their Issue to `X discovery: no`, changing the form selection to No, or deleting the link.

## Future conversation radar — proposed workflow

1. Read current Member and Brand profile Issues and extract accounts with explicit opt-in.
2. Validate and deduplicate account handles, while distinguishing self-declared and unverified identities.
3. Retrieve posts and public thread metrics from approved X API endpoints **only**. Respect rate limits, retrieval quotas, attribution requirements and deletion requests.
4. Select candidate conversations that demonstrate real replies from distinct people and have substance; not merely high likes or repost counts.
5. Summarize the subject in original words, link to the X original and credit its author. Avoid full-text replication, fabricated reply counts or unverified quotations.
6. Publish at most a handful of discussion invitations per day in OpenWave, using a clear `Source: X` marker. Avoid duplicates and add conversation source IDs for deduplication.
7. Give precedence to conversations that subsequently attract **human replies in OpenWave**. Do not count X replies as OpenWave engagement.

## Safety and trust

- Participation is voluntary; accounts must be provided by the profile author, not collected from someone else's profiles.
- X handles and public posts are visible to everyone. Don't ask members for access tokens or private accounts.
- Keep opt-in revocable and check it before every fetch and publication.
- No automated replies or impersonation on X; no engagement manipulation or copying full threads.
- A member's self-declared X handle is not an identity verification or proof of control.
- Be transparent that any summaries are created by automation and should link back to the source.
- Respect GitHub policies and X terms; X API access, pricing and data retention rules must be checked before activation.

## Success metric

Count **unique humans who participate in conversations on OpenWave**, not the number of imported posts or engagement on X.

The next milestone is an opt-in pilot with members who explicitly consent, then API-based ingestion after credentials and quotas are available.
