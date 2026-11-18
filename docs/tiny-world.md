# Tiny-world rules

Approved 2026-11-17 · [#8](https://github.com/Aman-zishan/panda/issues/8). Included in Basic and
Connect, with local state saved across restarts.

A creature and its landscape reflect focus and rest. No feeding, scores, streaks or daily chores.

## What you see

| What happens | How the world responds |
| --- | --- |
| Idle | The creature rests in a calm landscape. Nothing demands attention. |
| Focus starts | The creature settles into a focused pose. A simple progress indicator and remaining time make the session clear. |
| Focus is paused | Progress stops; the creature rests. Nothing is lost. |
| Focus ends early | Return to idle without a failure animation or loss of previous growth. |
| Focus completes | A small plant grows or blooms once. A brief celebration gives way to a resting scene, inviting a break. |
| Completion is acknowledged or snoozed | Clear the prompt or postpone it using the knob rules. The completed session's growth remains. |
| A voice request or reminder appears | Brief feedback takes priority, then the world returns. Captures and acknowledgements do not earn growth. |
| PANDA restarts or loses its connection | Restore saved growth. No decay or catch-up penalties for time offline or powered off. |

Growth stays within one small scene. Once it is fully grown, completed sessions can
briefly brighten it without adding more objects, levels or rewards to collect.
The creature never dies, becomes ill or asks to be rescued.

## Breaks and recovery

| Hardware | Break behaviour |
| --- | --- |
| Stage 1 | After focus, show a resting scene. Acknowledgement cannot confirm a break. Without a presence sensor, never infer desk time, absence or skipped breaks. The plant never wilts. Head movement comes in Stage 3. |
| With presence sensing | Rest while the person is away and welcome them back. Deferring a break nudge may briefly droop the plant. Preserve growth and keep the creature calm. Suppress attention cues in quiet mode. Never infer productivity from presence or wilt on uncertain readings. |

A detected break or the next completed focus session restores a drooping plant.
Any droop clears within a day, even without action. See [focus sessions](focus-experience.md)
for the break interval and absence threshold.

## Display checks

Use distinct poses and shapes on the monochrome display. Keep the scene still
between brief state-change animations. Exclude scrolling text, world menus,
creature alerts and flashing.

On hardware, check that someone can recognise focus, pause, completion and rest
without a manual. Check for distraction or any sense of obligation.
