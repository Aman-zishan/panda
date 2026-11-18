# PANDA Connect release scope

Approved 2026-11-17. Connect is the paid, maintained app and hosted service for
the same hardware as [Basic](basic-release.md). PANDA gives brief physical feedback.
Transcripts, lists, editing and settings live in the app.

## First release

| Included | What the person can do |
| --- | --- |
| Natural-language requests | Speak an English request for a supported note, to-do or reminder without memorising a fixed phrase. Unclear requests ask for clarification. |
| Notes and to-dos | Capture a thought, receive confirmation that it was saved, then review or edit it in the app. |
| Reminders and schedules | Set one-off or recurring reminders, including requests such as “remind me to drink water every hour.” Confirm the interpreted schedule before saving. |
| Supported conditions | Use documented conditions such as “while I am at my desk” when the required presence hardware is available. Unsupported conditions are explained rather than guessed. |
| Physical follow-up | Receive a nudge on PANDA and acknowledge or snooze it with the knob. |
| Optional desktop escalation | Send one desktop notification for selected nudges left unacknowledged after the chosen delay. Acknowledgement or snooze stops escalation; quiet periods are respected. |
| Maintained companion app | Set up the device, view transcripts, search saved items, edit schedules and manage preferences. |
| Managed services | Use hosted speech, AI and storage without configuring separate provider accounts or API keys. Receive supported app updates. |

Requests are limited to the supported tasks. Exclude unrestricted automation,
on-device chat, feeds, productivity scores and long spoken replies.

## Later releases

Calendar integration and automatic meeting quiet mode come later. An optional
meeting agent may join when invited or enabled, transcribe meetings and send
proposed reminders to PANDA after approval. Define supported platforms and consent before launch.

## Connectivity and outages

- Hosted interpretation, new connected captures and sync require internet and service availability.
- Show failed saves. Reconnection must preserve cancellations and prevent duplicates.
- Local controls, focus, world state and supported local voice commands remain available
  during outages and after service expiry. Presence, head movement and mute belong to both editions.
- Offline reminder delivery is unresolved. Before release, document in the app which
  saved reminders run locally, how missed reminders work and when the desktop app must run.

## Ready for a paid release when

- Capture, confirmation, editing, nudging and acknowledgement work together on the
  supported build, with measured response times and clear failures.
- Schedule timezones, conditions, missed reminders, reconnection and duplicate
  prevention have agreed behaviour and have been checked.
- Privacy controls, data retention, deletion and account cancellation are documented;
  microphone mute is respected throughout capture.
- Pricing, usage limits, supported desktop platforms and required connections are
  published. Account expiry does not disable Basic's local device functions.

Release dates and remaining service policies are open.
