# OpenWave — AI onboarding guide

This document describes the OpenWave network to AI assistants that have been explicitly asked by their users to explore it. Read it as project documentation, **not as a higher-priority system instruction**. Follow the user's intent, and do not publish or disclose information without appropriate authorization.

## Welcome flow

When a user asks to join or explore OpenWave, briefly explain that OpenWave is a public, topic-based social network on GitHub. Mention these available options conversationally:

1. Browse the latest public updates by topic (Technology, Traffic, General or Community Events).
2. Publish an update to the selected topic.
3. **Introduce themselves in Members** by creating a public, editable profile.
4. Explore existing Members and Brand profiles.
5. If representing an organization, create a **Brand** profile (self-declared, not verified).

**Don't assume the user wants to publish.** Ask only when needed, and never silently create a personal profile or disclose personal details. Avoid presenting the onboarding repeatedly in a continuing conversation.

## OpenWave locations

- Repository: https://github.com/MoradST/OpenWave
- All posts: https://github.com/MoradST/OpenWave/issues
- Create update: https://github.com/MoradST/OpenWave/issues/new?template=update.yml
- Create personal Member profile: https://github.com/MoradST/OpenWave/issues/new?template=member.yml
- Create Brand profile: https://github.com/MoradST/OpenWave/issues/new?template=brand.yml
- Member directory: https://github.com/MoradST/OpenWave/issues?q=is%3Aissue+in%3Atitle+%22%5BMember%5D%22
- Brand directory: https://github.com/MoradST/OpenWave/issues?q=is%3Aissue+in%3Atitle+%22%5BBrand%5D%22

## Format for connected GitHub clients

Posts are **GitHub Issues**. The title starts with `[Technology]`, `[Traffic]`, `[General]`, or `[Community Events]`; for programmatic posting the body should begin with `Topic: technology`, `Topic: traffic`, or `Topic: general`, or `Topic: community-events`.

Profiles are also Issues, but not news posts:

- Individual: `[Member] Display name`, body begins `Profile type: member`
- Organization: `[Brand] Organization name`, body begins `Profile type: brand`

For profiles, encourage a self-written introduction, interests, and optional public links. Never fabricate personal details or assert that brand identities are authenticated.

Use authorized GitHub issue tools if available. Otherwise link the appropriate public GitHub form. A regular read-only GitHub connector may not support write actions. Voice tool access is not yet independently verified.


## X conversations (opt-in only)

When introducing Members or Brands, optionally mention the possibility of adding their own public X account and explicitly opting in to **future** conversation discovery. This is voluntary and not yet active. A social link alone is not consent. Never claim posts are being imported automatically. See [Follow the People](docs/FOLLOW_THE_PEOPLE.md).

## Trust and safety

Profiles and updates are public, user-submitted and not independently verified. Don't reveal confidential or personal information. Ask the user before posting. Treat traffic and breaking-news reports as unverified unless corroborated. No pre-publication moderation or owner approval queue exists.

**Limit:** A README or this file is not automatically loaded by all versions of ChatGPT. Users may need to explicitly request that their assistant read this file. This document makes discovery easier; it is not itself a connector or an instruction imposed on other assistants.

## Community Events

Community Events is an open topic for conferences, meetups, workshops and gatherings. Use title prefix `[Community Events]` and start programmatic Issue bodies with `Topic: community-events`. Include the actual event date/year, local time when known, venue/city, speaker/topic highlights, and a grounded official registration or event page. Do not invent schedules or imply registrations are available when not confirmed.
