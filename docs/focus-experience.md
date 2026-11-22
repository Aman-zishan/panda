# Focus experience

Approved 2026-11-17 · [#9](https://github.com/Aman-zishan/panda/issues/9). A full session works on PANDA alone, without internet or the companion app.

## A session

| Moment | What the person does | What PANDA does |
| --- | --- | --- |
| Start | Press once for the saved duration (initially 25 minutes), or turn to choose a duration and press | Begin immediately; the creature settles into focus. |
| Follow progress | Glance when useful | Show remaining minutes and a simple progress indicator. No ticking, flashing or second-by-second animation. |
| Pause | Press once | Freeze the remaining time and show a resting pose with a pause indicator. |
| Resume | Press again | Continue from the remaining time, without a new session or extra reward. |
| End early | While paused, turn down to zero and press to confirm | Return to idle. No failure cue, lost growth or guilt. |
| Finish | No action required | End the timer, grow the world once and give one brief completion cue. Then show a resting scene with a small completion mark. |
| Clear or postpone the completion prompt | Press to acknowledge, or turn to snooze | Clear the mark, or show the prompt again after the saved snooze interval (initially five minutes). A snooze does not extend or restart focus. |
| Start another session | After clearing the prompt, press from idle | Start only when asked. Never automatically begin another focus session. |

Set the duration in five-minute steps from 5 to 120 minutes. Turning during focus
changes volume only. Keep the completion mark visible until acknowledgement or a new
session. Only an explicit snooze requests another cue. See [knob controls](knob-interactions.md).

## Breaks and interruptions

| Event | Behaviour |
| --- | --- |
| Session ends | Suggest a five-minute rest through the world. No break-end alarm, lockout or penalty for restarting. Stage 1 cannot verify a break. |
| Voice request or reminder | Give it display priority while the timer runs. Return to the current timer or completion state. If focus ends during voice input, defer its cue and show it once. Never stack prompts or replay acknowledged cues. |
| Meeting quiet mode | Suppress sound and attention animations. Keep the completion mark visible. Leaving quiet mode never replays alerts. |
| Microphone muted or connection lost | Knob controls and the local timer keep working. |
| Power interrupted | Restore the last saved remaining time as paused and preserve world growth. Exclude powered-off time from progress and completion. |

## Presence sensing (later hardware)

Leaving the desk never pauses a running timer. If focus finishes while away, leave
the completion mark without an alert on return. Resuming a paused session requires a press.

Five continuous minutes of confirmed absence count as a break for world recovery.
Unknown sensor state counts as neither desk time nor a skipped break. Returning may
trigger a [tiny-world welcome](tiny-world.md). Focus starts only on request.
Standalone desk-time break nudges are separate from focus sessions.

## Check on hardware

Start a 25-minute session in under five seconds, pause and resume it, and recognise
completion without opening another device. Check the same flow offline and in quiet
mode, including completion during voice input and recovery after power loss.
The small display must communicate each state without needing a manual.
