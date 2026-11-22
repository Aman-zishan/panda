# Voice capture outcomes

Approved 2026-11-17 · [#11](https://github.com/Aman-zishan/panda/issues/11). English first.
PANDA handles its documented local commands; the captures below belong to Connect.
Community integrations may provide their own alternatives.

## What gets saved

| Request | Result | Confirmation |
| --- | --- | --- |
| “Note: try a wider base for PANDA.” | A note preserving the thought, with no invented details or reminder. | Show “Note saved” only after storage succeeds. Full text is in the app. |
| “Add a to-do: order jumper wires.” | One incomplete task. No deadline or alert unless requested. | Show “Task saved” after storage succeeds. |
| “Remind me tomorrow at 3 PM to order jumper wires.” | A proposed reminder with an explicit date, time and action. | Show the resolved date/time and short action; save and activate only after confirmation. |
| “Remind me to drink water every hour while I’m at my desk.” | A proposed recurring schedule with its interval, active hours and supported presence condition. | Clarify missing scheduling details, then confirm. If the condition cannot be supported, do not silently drop it. |

Press to confirm a visible reminder, turn to discard, or long-press to replace it.
Cancelled or expired proposals schedule nothing. If the full schedule takes more
than a glance, review it in the app before activation. See [knob controls](knob-interactions.md).

## Voice capture privacy

While the microphone is enabled, PANDA checks for the wake word on the device.
PANDA processes its supported commands locally. For a Connect capture, the listening
cue signals when to speak. Only speech captured after activation goes to the
connected speech service for transcription.

Connect stores the transcript and saved item in its managed storage for review in
the companion app. Raw audio is temporary: discard it after transcription, or when
a capture fails or is cancelled. Capture history offers text only.

The Stage 2 physical mute switch disables microphone input, including wake-word
detection and knob-initiated capture. The knob and local timer keep working.

## Listening and clarification

- Use the wake word or long-press and release. Speak after the ready cue. Display and light must distinguish listening, processing and saved, even without sound files. PANDA never speaks replies.
- For an unclear request, display one brief question such as “What time?” and wait for an explicit reply. End without saving if none arrives. Never guess dates or create tasks from uncertain transcripts.
- In the first release, ask the user to split unrelated actions into separate requests.
- PANDA explains unsupported requests locally. Supported local commands, including focus, remain available. Exact phrases need hardware validation.

## Correction, cancellation and failure

- **Before saving:** cancel or replace the pending request. A late response must
  not revive a cancelled action. A corrected reminder requires fresh confirmation.
- **After saving:** show that it was saved; edit or delete it in the app. A new
  capture is not an implicit edit of an earlier item.
- **Not understood or definitely not saved:** briefly show that outcome and allow
  a fresh attempt. Never confirm an action just because speech was transcribed.
- **Save outcome uncertain after connection loss:** show “Save unconfirmed”, reconcile
  the original attempt when connected, and avoid duplicate items. Do not silently
  submit it again as a new capture.
- **Microphone muted:** capture nothing and show muted status. Existing local
  controls remain usable. Connection failures do not interrupt local focus.

Return to the underlying focus/world state after feedback. No repeated failure
alerts, scrolling transcripts or notification feed on the device.

Recognition and feedback still require prototype validation. See
[reminder behaviour](connect-release.md#reminder-behaviour) and
[privacy requirements (#14)](https://github.com/Aman-zishan/panda/issues/14).
