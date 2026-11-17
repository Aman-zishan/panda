# Voice capture outcomes

Approved 2026-11-17 · [#11](https://github.com/Aman-zishan/panda/issues/11). English first.
Basic handles its documented local commands; the captures below belong to Connect.
Community integrations may provide their own alternatives.

Following the [product philosophy](product-philosophy.md), speak a quick thought,
get brief feedback, then return to work. Full transcripts and editing stay in the app.

## What gets saved

| Request | Result | Confirmation |
| --- | --- | --- |
| “Note: try a wider base for PANDA.” | A note preserving the thought, with no invented details or reminder. | Show “Note saved” only after storage succeeds. Full text is in the app. |
| “Add a to-do: order jumper wires.” | One incomplete task. No deadline or alert unless requested. | Show “Task saved” after storage succeeds. |
| “Remind me tomorrow at 3 PM to order jumper wires.” | A proposed reminder with an explicit date, time and action. | Show the resolved date/time and short action; save and activate only after confirmation. |
| “Remind me to drink water every hour while I’m at my desk.” | A proposed recurring schedule with its interval, active hours and supported presence condition. | Clarify missing scheduling details, then confirm. If the condition cannot be supported, do not silently drop it. |

For reminders, one press confirms the visible proposal, turning discards it, and a
long press starts a replacement request, following the [knob controls](knob-interactions.md).
A proposal is not a saved reminder. If it expires or is cancelled, nothing is scheduled.
If the whole schedule cannot be checked in one glance, review it in the app before
activation; do not hide important conditions behind a generic “Confirm?” prompt.

## Listening and clarification

Say the wake word or long-press, release and speak after the ready indication.
Listening, processing and saved are distinct states. No sound files are required:
display and light feedback must communicate them too. PANDA does not speak replies.

An unclear request gets one brief question, such as “What time?”, then waits for an
explicit reply. It must not guess a date, turn an uncertain transcript into a task,
or claim success. A missing reply ends the interaction without saving. For the first
release, ask people to separate requests containing several unrelated actions.

Basic must explain unsupported connected requests without sending them to a hosted
service automatically. Its local commands, such as starting focus, remain available.
The exact supported phrases still require hardware validation.

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

Recognition and feedback still require prototype validation. Detailed schedule rules belong to
[#12](https://github.com/Aman-zishan/panda/issues/12); recording retention and privacy
belong to [#14](https://github.com/Aman-zishan/panda/issues/14).
