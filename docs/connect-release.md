# PANDA Connect release scope

Draft alongside the [Basic release scope](basic-release.md). The
[feature matrix](feature-matrix.md) describes the planned editions; not every Connect
feature is part of its first release.

Connect is the paid, maintained companion app and managed service. It adds quick
voice capture and useful follow-up to the same physical PANDA. Following the
[product philosophy](product-philosophy.md), the device gives brief feedback and
nudges; transcripts, lists, editing and settings stay in the app.

## Proposed first release

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

This is assistance with the listed tasks, not unrestricted automation or an on-device
chat interface. It does not add feeds, productivity scores or long spoken replies.

## Later releases

Calendar integration and automatic meeting quiet mode come later. The optional
meeting agent also comes later: joining when invited or enabled, producing
transcripts and proposing reminders for approval before sending them to PANDA.
Supported platforms and consent behaviour must be defined before those features ship.

## Internet, outages and local use

Hosted interpretation, new connected captures and synchronisation require an
internet connection and an available service. A failed request must never appear
saved. Reconnection must not silently replay a cancelled request or create duplicates.

Basic's local controls, focus, world and supported local voice commands continue
without Connect, including when service access ends. The same hardware capabilities
remain available; Connect does not unlock presence, head movement or microphone mute.

Connected reminder delivery during outages is not yet an offline guarantee. Before
release, define which saved reminders can run locally, what happens to missed ones
and whether the desktop app must be running. Explain those limits in the app.

## Ready for a paid release when

- Capture, confirmation, editing, nudging and acknowledgement work together on the
  supported build, with measured response times and clear failures.
- Schedule timezones, conditions, missed reminders, reconnection and duplicate
  prevention have agreed behaviour and have been checked.
- Privacy controls, data retention, deletion and account cancellation are documented;
  microphone mute is respected throughout capture.
- Pricing, usage limits, supported desktop platforms and required connections are
  published. Account expiry does not disable Basic's local device functions.

This page defines the product offering. Release dates and the remaining service
policies are still to be decided.
