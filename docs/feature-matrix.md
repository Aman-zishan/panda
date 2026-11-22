# Local and connected features

PANDA uses the same hardware whether it is online or offline. These are planned
capabilities. The [device release scope](basic-release.md) lists the components and
hardware checks for each build.

| What you want to do | What you need |
| --- | --- |
| Start or pause focus, adjust volume, or see the tiny world grow | PANDA alone after setup. The knob, display and feedback work offline, and world growth survives restarts. |
| Start focus or change volume by voice | PANDA listens locally after the wake word or a long press. The exact English commands and recognition accuracy still need bench testing. |
| Set up PANDA, check its status or assign your own sounds | The Connect desktop app and a local connection to PANDA. Setup and controls work without hosted services. |
| Speak a note, to-do or reminder in your own words | Connect uses hosted speech and interpretation. Review transcripts, search saved items and edit schedules in the app. |
| Schedule a one-off, recurring or conditional nudge | Confirm the schedule through Connect. When PANDA nudges, press to acknowledge or turn to snooze. Desktop follow-up is optional. |

**If the internet drops**, local controls and focus keep working. New connected
captures and sync need the service. Delivery of previously saved reminders during
an outage is still an open requirement. See [Connect release scope](connect-release.md#connectivity-and-outages).

Calendar-based quiet mode and opt-in meeting transcription are planned for the
[integrated breadboard stage](connect-release.md#integrated-breadboard-stage).
