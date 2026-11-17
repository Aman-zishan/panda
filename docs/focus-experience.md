# Focus experience

Approved 2026-11-17 · [#9](https://github.com/Aman-zishan/panda/issues/9). Included in Basic and
Connect. A full session works on PANDA alone, without internet or the companion app.

Following the [product philosophy](product-philosophy.md), the benefit is a physical
start, quiet progress at a glance and a clear finish. No task lists, productivity
scores or menus on the device.

## A session

| Moment | What the person does | What PANDA does |
| --- | --- | --- |
| Start | Press once for 25 minutes, or turn to choose a duration and press | Begin immediately; the creature settles into focus. |
| Follow progress | Glance when useful | Show remaining minutes and a simple progress indicator. No ticking, flashing or second-by-second animation. |
| Pause | Press once | Freeze the remaining time and show a resting pose with a pause indicator. |
| Resume | Press again | Continue from the remaining time, without a new session or extra reward. |
| End early | While paused, turn down to zero and press to confirm | Return to idle. No failure cue, lost growth or guilt. |
| Finish | No action required | End the timer, grow the world once and give one brief completion cue. Then show a resting scene with a small completion mark. |
| Clear or postpone the completion prompt | Press to acknowledge, or turn to snooze | Clear the mark, or show the prompt again after five minutes. A snooze does not extend or restart focus. |
| Start another session | After clearing the prompt, press from idle | Start only when asked. Never automatically begin another focus session. |

The approved [knob controls](knob-interactions.md) set duration in five-minute steps
from 5 to 120 minutes. Changing volume during focus does not change the timer.
The completion mark stays understandable until acknowledged or a new session begins;
it does not flash or repeatedly alert. Only an explicit snooze requests another cue.

## Breaks and interruptions

After focus, suggest a five-minute rest through the world. It is an invitation, not
a compulsory countdown: there is no break-end alarm, lockout or penalty for starting
again. Stage 1 cannot tell whether a break happened and never claims that it did.

A voice interaction or reminder temporarily takes display priority without pausing
focus. On return, show the current timer or its completed state. If focus finishes
during voice input, defer the completion cue until the interaction ends; show it once.
Do not stack overlapping prompts or repeat cues already acknowledged.

Meeting quiet mode suppresses audible completion and attention animations; the
completion mark still conveys the outcome. Leaving quiet mode does not replay old
alerts. Microphone mute does not prevent knob control or stop the timer.

Connection loss does not interrupt local focus. After a power interruption, offer
the last saved remaining time in a paused state; never count powered-off time as
focus or invent a completion. Saved world growth remains intact.

## Later, with presence sensing

Leaving the desk does not silently change a timer the person started. Pause remains
explicit. A session finishing while away leaves its completion mark without an alert
on return. A paused session also waits for an explicit resume.

For world recovery, five continuous minutes of confidently detected absence count
as a break. Unknown sensor state does not count as desk time or a skipped break.
Returning may give the small welcome described in the [tiny-world rules](tiny-world.md),
without automatically starting focus. Standalone desk-time break nudges are separate
from this session flow.

## Check on hardware

Start a 25-minute session in under five seconds, pause and resume it, and recognise
completion without opening another device. Check the same flow offline and in quiet
mode, including completion during voice input and recovery after power loss.
The small display must communicate each state without needing a manual.
