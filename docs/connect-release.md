# PANDA Connect release scope

Connect handles desktop setup, transcripts, editing, search and preferences. PANDA gives immediate feedback on the device.

## First release

- Capture English notes and to-dos using [voice capture and confirmation](voice-capture.md). Ask for clarification when a request is unclear.
- Confirm one-off and recurring schedules before saving. Explain unsupported conditions. At-desk conditions require presence hardware.
- Provide hosted speech, interpretation, storage and supported app updates without separate provider accounts.
- Limit requests to supported desk tasks. Keep feeds, productivity scores, chat and long spoken replies off the device.

## Reminder behaviour

When a reminder comes due, briefly show its action and give one short cue if quiet
settings permit. During focus, keep the timer running. The knob acts on the reminder
while its prompt is visible, then resumes its usual controls.

| Response | What happens to this occurrence |
| --- | --- |
| Short press | Acknowledge the nudge, clear the prompt and cancel pending desktop follow-up. The underlying task stays as it was. |
| Turn | Snooze for the saved interval (initially five minutes). Clear the prompt and cancel pending desktop follow-up. When the interval ends, nudge once more. |
| No response | Return to the timer or idle display. The device stays silent for this occurrence. If the user enabled desktop follow-up for this reminder, send at most one notification after their chosen delay, respecting quiet periods. |

Future occurrences of a recurring reminder follow their schedule. For example, ignoring
the 2 pm water reminder leaves the 3 pm reminder in place.

## Integrated breadboard stage

Test calendar integration and automatic meeting quiet mode on the integrated bench. An optional
meeting agent may join when invited or enabled, transcribe meetings and send
proposed reminders to PANDA after approval. Define supported platforms and consent before launch.

## Connectivity and outages

- Hosted interpretation, new connected captures and sync require internet and service availability.
- Show failed saves. Reconnection must preserve cancellations and prevent duplicates.
- Local controls, focus, world state and supported local voice commands remain available
  during outages and after service expiry. Presence, head movement and mute belong to the device.
- Offline reminder delivery is unresolved. Before release, document in the app which
  saved reminders run locally, how missed reminders work and when the desktop app must run.

## Ready for a hosted release when

- Capture, confirmation, editing, nudging and acknowledgement work together on the
  supported build, with measured response times and clear failures.
- Schedule timezones, conditions, missed reminders, reconnection and duplicate
  prevention have agreed behaviour and have been checked.
- Verify speech-provider retention settings and actual audio disposal, including failed
  and cancelled captures, before promising [transcript-only history](voice-capture.md#voice-capture-privacy).
- Privacy controls, data retention, deletion and account cancellation are documented;
  microphone mute is respected throughout capture.
- Pricing, usage limits, supported desktop platforms and required connections are
  published. Account expiry does not disable local device functions.

Release dates and remaining service policies are open.
