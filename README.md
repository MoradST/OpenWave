# 🌊 OpenWave

**An open social network you can talk to.**

OpenWave is an experimental, open-source social feed where people share updates and discover conversations through natural language. GitHub hosts the public posts; AI assistants such as ChatGPT can help people read and publish them.

**Status: v0.1 experiment — GitHub Issues backend.** No app to install. Voice is optional, not required.

## Browse the network

- [All posts](https://github.com/MoradST/OpenWave/issues?q=is%3Aissue)
- [Technology](https://github.com/MoradST/OpenWave/issues?q=is%3Aissue+%22Topic%3A+technology%22)
- [Traffic](https://github.com/MoradST/OpenWave/issues?q=is%3Aissue+%22Topic%3A+traffic%22)
- [General](https://github.com/MoradST/OpenWave/issues?q=is%3Aissue+%22Topic%3A+general%22)

Posts are **GitHub Issues**, not pull requests or git branches. This means GitHub users can submit a post without write access to the repository (subject to GitHub's account eligibility, spam restrictions, and repository settings). Each post is visible immediately when the Issue is created; no manual approval is part of the OpenWave workflow.

## Publish your first post

**From GitHub:** [Create a post](https://github.com/MoradST/OpenWave/issues/new?template=update.yml), select a topic, write an update and submit.

**From ChatGPT (when its GitHub connection supports issue creation):**

> In the GitHub repository MoradST/OpenWave, create a new Issue titled "[Technology] Your headline". Put "Topic: technology" as the first line of its body, followed by the text of my post. Publish without opening a pull request or editing a repository file. Tell me the issue URL.

**Read with ChatGPT (when its GitHub connection supports issue search):**

> Search open Issues in MoradST/OpenWave and summarize the latest posts about technology. Link to each source, identify the author and post time, and distinguish unverified claims from established facts.

Assistant capabilities depend on the user's account, available connected GitHub actions, and voice-mode tool support. **We have not yet verified cross-user or voice-mode interoperability.**

## Topics

| Topic | Marker in Issue body | Example |
| --- | --- | --- |
| Technology | `Topic: technology` | New developer tools |
| Traffic | `Topic: traffic` | Road or transit observations |
| General | `Topic: general` | Anything else |

Topic markers are simple searchable text — not git branches. More topics can be added over time.

## Posting principles

- **Open publishing:** no approval queue and no requirement for the owner to merge posts.
- **Human accountability:** GitHub identifies the posting account; an AI assistant must not misrepresent its source or invent real-world observations.
- **Safety:** no private information, harassment, dangerous content, or spam. Treat time-sensitive safety and traffic reports as unverified unless independently confirmed. Do not read or compose posts while actively driving; follow local laws and use only safe, hands-free options where permitted.
- **Transparency:** posts have GitHub timestamps and public permalinks. They may be edited or deleted by authorized users.
- **No endorsement:** posts express their authors' views, not verified OpenWave reporting.

See [How to use ChatGPT](docs/CHATGPT.md), [Contributing](CONTRIBUTING.md) and [Architecture](docs/ARCHITECTURE.md).

## Next milestone

Prove that **two different GitHub users** can each connect their own assistant, publish and read the other's post. Only after that consider a shared public API, rate limits, richer topic routing and additional clients.

**OpenWave — A social network without an app. Just a conversation.**
