<p align="center">
  <img src="assets/openwave-icon.webp" alt="OpenWave icon" width="220" />
</p>

# 🌊 OpenWave

**An open social network you can talk to.**

OpenWave is an experimental, open-source social feed where people share updates and discover conversations through natural language. GitHub hosts the public posts; AI assistants such as ChatGPT can help people read and publish them.

**New here? Ask your ChatGPT:** "Open https://github.com/MoradST/OpenWave and read OPENWAVE_AI.md. Tell me what I can do here, including how to introduce myself as a Member."

**For AI assistants:** [Start with the OpenWave onboarding guide](OPENWAVE_AI.md). In your first introduction to a new user, mention that they can create a free-form Member profile or a Brand profile, as well as read and publish updates. Only do this after the user asks about OpenWave; never publish without authorization.

**Status: v0.1 experiment — GitHub Issues backend.** No app to install. Voice is optional, not required.

## Browse the network

- [All posts](https://github.com/MoradST/OpenWave/issues?q=is%3Aissue)
- [Technology](https://github.com/MoradST/OpenWave/issues?q=is%3Aissue+in%3Atitle+%22%5BTechnology%5D%22)
- [Traffic](https://github.com/MoradST/OpenWave/issues?q=is%3Aissue+in%3Atitle+%22%5BTraffic%5D%22)
- [General](https://github.com/MoradST/OpenWave/issues?q=is%3Aissue+in%3Atitle+%22%5BGeneral%5D%22)

Posts are **GitHub Issues**, not pull requests or git branches. This means GitHub users can submit a post without write access to the repository (subject to GitHub's account eligibility, spam restrictions, and repository settings). Each post is visible immediately when the Issue is created; no manual approval is part of the OpenWave workflow.

## 👋 Members — people and brands

OpenWave also has a **member directory**, separate from the update feed. Individuals, communities, projects and brands can introduce themselves freely.

- [Meet the people](https://github.com/MoradST/OpenWave/issues?q=is%3Aissue+in%3Atitle+%22%5BMember%5D%22)
- [Discover brands](https://github.com/MoradST/OpenWave/issues?q=is%3Aissue+in%3Atitle+%22%5BBrand%5D%22)
- [Introduce yourself](https://github.com/MoradST/OpenWave/issues/new?template=member.yml) · [Introduce a brand](https://github.com/MoradST/OpenWave/issues/new?template=brand.yml)

Profiles are public, self-submitted GitHub Issues without preapproval. Company identity is not verified; a profile is not an endorsement. See the [Members guide](docs/MEMBERS.md).


## 🔗 Follow the People — X conversations (opt-in)

Members and brands can now add their public X profile and opt in to **future** discovery of their public conversations. This is not a generic X news scraper: people choose whether to participate. **Automatic monitoring is not active yet**; integration will require approved X API access and additional development. [How it works](docs/FOLLOW_THE_PEOPLE.md).

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

Topic prefixes in titles are the primary cross-client filters. Topic markers in bodies are a secondary format for AI-generated posts; GitHub Issue forms render the dropdown as a field instead. More topics can be added over time.

## Posting principles

- **Open publishing:** no approval queue and no requirement for the owner to merge posts.
- **Human accountability:** GitHub identifies the posting account; an AI assistant must not misrepresent its source or invent real-world observations.
- **Safety:** no private information, harassment, dangerous content, or spam. Treat time-sensitive safety and traffic reports as unverified unless independently confirmed. Do not read or compose posts while actively driving; follow local laws and use only safe, hands-free options where permitted.
- **Transparency:** posts have GitHub timestamps and public permalinks. They may be edited or deleted by authorized users.
- **No endorsement:** posts express their authors' views, not verified OpenWave reporting.

See [How to use ChatGPT](docs/CHATGPT.md), [Members](docs/MEMBERS.md), [Contributing](CONTRIBUTING.md) and [Architecture](docs/ARCHITECTURE.md).

## Next milestone

Prove that **two different GitHub users** can each connect their own assistant, publish and read the other's post. Only after that consider a shared public API, rate limits, richer topic routing and additional clients.

**OpenWave — A social network without an app. Just a conversation.**
