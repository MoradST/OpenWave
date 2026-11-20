# ChatGPT quick start

OpenWave is a public GitHub repository. To use an AI assistant with it, the user needs a GitHub connection that can **search and create Issues**. Availability differs by ChatGPT plan, mode and connector permissions. Reading a public GitHub URL without a connector might also be possible, but web search is not a guaranteed real-time feed.

## Publish

Try:

> Create an Issue in `MoradST/OpenWave`. Title: `[Technology] A brief headline`. Body: `Topic: technology` followed by my update and, if I supplied one, a source link. Do not create a pull request. Return the new Issue URL.

If the assistant reports an inability to create Issues, publish through [the GitHub form](https://github.com/MoradST/OpenWave/issues/new?template=update.yml).

## Read

Try:

> Search the latest Issues in `MoradST/OpenWave`, sorted by creation date. Summarize the five newest technology posts, preserving Issue URLs and author names. Mention timestamps and mark unverified statements as unverified.

For traffic, replace `technology` with `traffic`. For events, search for `[Community Events]` in titles or `Topic: community-events` and include dates and registration links. For jobs, search for `[Jobs]` in titles and include location, work model, application links and dates when available. For all posts, omit the topic filter.

## Members: introduce yourself or a brand

OpenWave has a profile directory separate from the news/update feed. With an authorized GitHub Issue creation connector, ask:

> Create a GitHub Issue in MoradST/OpenWave titled "[Member] My name", with body starting "Profile type: member" and my freely written introduction and optional public links. Don't invent details. Give me the published URL.

A company or community can use "[Brand] Name" and "Profile type: brand". Profiles are self-identified, not verified.

- [Person profile form](https://github.com/MoradST/OpenWave/issues/new?template=member.yml)
- [Brand profile form](https://github.com/MoradST/OpenWave/issues/new?template=brand.yml)
- [Members guide](MEMBERS.md)

## Follow people and channels

OpenWave supports public following preferences saved as GitHub Issues. Use the [following form](https://github.com/MoradST/OpenWave/issues/new?template=follow.yml) or an authorized ChatGPT GitHub connection to create your own list.

Ask: "What's new from the people and channels I follow on OpenWave?" The assistant should find your open `[Following]` issue, verify the **real Issue author's GitHub login**, and filter posts by followed GitHub accounts or channels. If it can't identify your account, it should ask for the login and state the limitation. Don't count profiles or following lists as news posts.

See [the complete following guide](FOLLOWING.md). Preferences are public and **do not generate push notifications**.

## Reply

GitHub Issue comments are conversations. Reply through GitHub or an assistant with Issue-comment permissions.

## Expectations and limitations

- This is an **experiment**, not a guaranteed universal ChatGPT integration.
- An assistant's tool capabilities can differ in text chat and in voice mode. Voice publishing is not yet verified.
- OpenWave itself does not have an autonomous shared ChatGPT bot. Each user connects their own authorized tools.
- Do not provide GitHub tokens in posts or public chats. Never grant unknown users push access.
- Information is posted by independent users and may be incorrect, late, incomplete or malicious.
- Public Github Issues can be cached or indexed; do not publish personal or confidential information.
