# Knob interactions

Draft for [#6](https://github.com/Aman-zishan/panda/issues/6). Same controls in Basic
and Connect; connected reminders require Connect or a community integration.

**Turn to adjust. Press to act. Long press to start listening.** No menus or double-clicks.

## Controls

| What PANDA is doing | Turn | Short press | Long press |
| --- | --- | --- | --- |
| Idle | Choose focus duration; show minutes briefly | Start focus with the selected duration | Start voice input |
| Focusing | Adjust speaker volume; show level briefly | Pause focus | Start voice input; timer continues |
| Focus paused | Adjust remaining time; turn down to zero to end the session | Resume, or end if zero is selected | Start voice input; timer stays paused |
| Showing a nudge or focus-complete signal | Snooze it using the saved snooze duration | Acknowledge and clear it | Start voice input without acknowledging it |
| Listening | Cancel capture | Cancel capture | No additional action |
| Processing voice | No action | Cancel the pending request | No additional action |
| Asking to confirm a proposed action | Discard the proposal | Confirm the displayed action | Replace the unsaved proposal with new voice input |

Only one prompt is shown at a time. A voice interaction temporarily takes priority;
after it ends, return to the underlying focus state or unresolved nudge. Unattended
prompts become silent rather than repeatedly sounding. Never cycle through a list.

## Starting defaults

- Focus starts at 25 minutes. Turning changes it in five-minute steps, from 5 to 120
  minutes. An unstarted selection clears after five seconds back to the saved default.
- While paused, adjust the remaining time in five-minute steps, clamped at zero.
  Zero shows “End focus?”; only a short press ends it. Turning up keeps the session.
- Snooze is five minutes initially. One turn in either direction snoozes once;
  further turns in the same gesture must not change the underlying timer or volume.
- Long press for about one second, release, then speak after the listening cue.
  There is no need to keep holding while talking. Release does not trigger a short
  press. Speech ends on silence, with a bounded capture time. The wake word remains
  the hands-free alternative.
- A sleeping display wakes on the first interaction without carrying out its action.

Timing and turn sensitivity need checking with the real knob. Settings such as
default duration, snooze duration and volume remain available in the companion app.

## Keep it calm and predictable

Knob turns are silent. Show only the current duration, volume or brief confirmation.
Changing volume never overrides meeting quiet mode or microphone mute. Holding a
muted device shows muted status and captures nothing. Local focus controls work
offline; unavailable voice services show a brief failure, never a false success.

Cancellation stops an uncommitted voice action from being saved or executed. A late
response must not revive it. If an action was already saved, show that outcome;
editing it belongs in the app. Acknowledging a reminder clears its nudge, not the
underlying task. Snooze or acknowledgement also ends its pending desktop escalation.

## Check on hardware

- Set and start 25 minutes in under five seconds without the app.
- Pause, resume and end a session without accidentally starting voice input.
- Acknowledge or snooze a nudge in one gesture, then return to the previous state.
- Hold and release without also triggering a short press; no false presses in an hour idle.
- Confirm mute, offline behaviour and cancellation before enabling saved voice actions.
