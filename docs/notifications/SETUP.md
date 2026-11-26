# OpenWave web push — activation checklist

Status: implementation prepared, not yet live. The page uses OneSignal's web SDK and stores subscription/preferences with that provider, not in public GitHub Issues. No OpenWave account is required. Do not activate until the provider privacy terms and data-tag allowance (all categories plus wildcard) have been reviewed.

1. Enable GitHub Pages for main /docs (if already configured, preserve its configuration). Verify https://moradst.github.io/OpenWave/notifications/ loads over HTTPS.
2. Create a OneSignal web push app for the exact HTTPS site origin https://moradst.github.io. Configure custom service worker URL /OpenWave/notifications/OneSignalSDKWorker.js and scope /OpenWave/notifications/. Check whether another app on that origin conflicts. Disable automatic subscription prompts.
3. Set the public app ID in docs/notifications/config.json and repository Actions variable ONESIGNAL_APP_ID. Store the private App API key only as Actions secret ONESIGNAL_API_KEY. Never commit it.
4. Verify provider plan supports the category tags and tag filters, and test subscription, opt-out, category matching and delivery on a desktop browser and an iOS 16.4+ Home Screen installation before announcing availability. Test with a real newly opened issue; no existing issues are backfilled. Test that unsubscribed browsers do not receive alerts. GitHub may suppress workflow events created with GITHUB_TOKEN; use an authorized user or approved app token for posts where needed.
5. Once verified, update README and OPENWAVE_AI.md status to live.

The README Topics table is the category source. New rows using the same marker format automatically appear in the UI and sender; title prefixes must correspond to the category display name or slug (aliases may need explicit routing). Member and Brand introductions are explicit additional categories. All categories includes future topics; individually selected topics do not. Following preference issues are excluded. Only newly opened issues trigger pushes; comments and edits do not. Incomplete posts can still trigger a push, so review moderation/spam exposure before public rollout. Notifications contain public titles and links, not private content. Device/browser settings govern visibility. Provider delivery is not guaranteed.

The setup page is not a general-purpose OpenWave account or feed. It is only for opt-in notifications.
