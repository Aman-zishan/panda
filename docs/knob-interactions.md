# Knob interactions

Approved 2026-11-17 · [#6](https://github.com/Aman-zishan/panda/issues/6). Same controls in Basic
and Connect; connected reminders require Connect or a community integration.

**Turn to adjust. Press to act. Long press to start listening.** No menus or double-clicks.

## Controls

| What PANDA is doing | Turn | Short press | Long press |
| --- | --- | --- | --- |
| Idle | Choose focus duration; show minutes briefly | Start focus with the selected duration | Start voice input |
| Focusing | Adjust speaker volume; show level briefly | Pause focus | Start voice input; timer continues |
| Focus paused | Adjust remaining time; turn down to zero to show “End focus?” | Resume, or end if zero is selected | Start voice input; timer stays paused |
| Showing a nudge or focus-complete signal | Snooze it using the saved snooze duration | Acknowledge and clear it | Start voice input without acknowledging it |
| Listening | Cancel capture | Cancel capture | No additional action |
| Processing voice | No action | Cancel the pending request | No additional action |
| Asking to confirm a proposed action | Discard the proposal | Confirm the displayed action | Replace the unsaved proposal with new voice input |

Show one prompt at a time. Voice takes priority, then returns to the underlying
focus state or unresolved nudge. Unattended prompts fall silent. Never cycle through a list.

## Defaults and timing

| Setting | Behaviour |
| --- | --- |
| Focus duration | Default 25 minutes. Adjust in five-minute steps from 5 to 120. An unstarted selection reverts to the saved default after five seconds. |
| Paused timer | Adjust remaining time in five-minute steps down to zero. At “End focus?”, press to end or turn up to keep the session. |
| Snooze | Default five minutes. One turn in either direction snoozes once. Ignore further turns in the same gesture to protect timer and volume settings. |
| Voice activation | Hold about one second, release, then speak after the cue. Release never triggers a short press. Capture ends on silence or at its time limit. The wake word also activates listening. |
| Display asleep | The first interaction only wakes the display. |

Set default focus duration, snooze duration and volume in the app. Validate timing and turn sensitivity on the physical knob.

## Feedback and cancellation

- Turns are silent. Briefly show the duration, volume or confirmation. Volume changes respect quiet mode and microphone mute.
- Holding while muted shows mute status and captures nothing. Focus works offline. Unavailable voice services show a brief failure.
- Cancellation prevents pending actions from executing or saving, even if a response arrives late. Show the outcome of an already saved action and edit it in the app.
- Acknowledgement clears the nudge and preserves the task. Snooze and acknowledgement both stop pending desktop escalation.

## Check on hardware

- Set and start 25 minutes in under five seconds without the app.
- Pause, resume and end a session without accidentally starting voice input.
- Acknowledge or snooze a nudge in one gesture, then return to the previous state.
- Hold and release without also triggering a short press; no false presses in an hour idle.
- Confirm mute, offline behaviour and cancellation before enabling saved voice actions.
