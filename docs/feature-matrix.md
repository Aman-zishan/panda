# Feature matrix

Approved 2026-11-17 · [#3 — Basic and Connect](https://github.com/Aman-zishan/panda/issues/3).
Defines behaviour and edition scope, not implementation. Approval confirms scope;
all features still require implementation and validation.

Sources: [concept v1, pages 3–7](PANDA_desk_companion_concept_v1.pdf),
[approved philosophy](product-philosophy.md), and [decisions](decisions.md).

## Editions and stages

- **Basic:** open-source firmware, hardware build files and a community app for setup, controls and device status. Includes local focus and a simple tiny world, plus documented audio/event interfaces and integration examples.
- **Connect:** a private, paid companion app maintained by the creator, with integrated voice workflows, reminders, notes, calendar, history and hosted speech/AI services.
- **Stage 1:** breadboard controls, focus, sound, display and connected voice loop.
- **Stage 2:** presence, electrical microphone mute and calendar behaviour.
- **Stage 3:** enclosure, visor and head movement.

Stages describe build order, not edition tiers. Presence and movement require their
respective hardware even when included in an edition.

## Device behaviour

| ID | Feature | Basic | Connect | Stage | Required outcome |
| --- | --- | --- | --- | --- | --- |
| F01 | Knob controls | Yes | Yes | 1 | Turn to adjust; press to start or acknowledge. Exact gestures are defined separately. |
| F02 | Focus sessions | Knob + limited local voice commands | Local + flexible voice requests | 1 | Set and complete a session without app interaction; clearly signal its end. |
| F03 | Sound vocabulary | Local events + integration interface | Local + integrated events | 1 | Short, distinct sounds with one meaning each. No spoken replies. |
| F04 | Status light | Local, listening, muted and offline states | Same | 1 | Make current state clear within one second; never show listening when capture is unavailable. |
| F05 | Tiny world | Simple local world | Local world + connected behaviours | 1 | Focus affects the world. It never dies or shames; recovery takes no more than a day. |
| F06 | State persistence | Local world | Local world; managed records | 1 | World state survives a restart. Basic must not require the backend for this. |
| F07 | Brief display feedback | Timer/local state; integration display interface | Also captured item/time | 1 | Read at a glance. Full text, lists and editing belong in the app. |
| F08 | Presence | Yes | Yes | 2 | Recognize at-desk and away; use presence for breaks, world behaviour and display sleep. |
| F09 | Break nudges | Local | Yes | 2 | Use desk presence to time a gentle nudge. Avoid repeated demands for attention. |
| F10 | Display protection | Local presence-driven dim/sleep | Presence-driven dim/sleep | 2 | Shift pixels, dim and sleep as appropriate; Basic must work without calendar access. |
| F11 | Head movement | Yes | Yes | 3 | Respond to arrival, breaks or absence. Movement must not interfere with capture or sound. |
| F12 | Enclosure and visor | Yes | Yes | 3 | Support a compact, repairable build; a plain shell remains possible without a servo. |

## Connected behaviour

| ID | Feature | Basic | Connect | Stage | Required outcome |
| --- | --- | --- | --- | --- | --- |
| F13 | Wake word and long-press capture | Limited local commands + audio integration interface | Local commands + integrated language understanding | 1 | Accept a short request after a wake word or deliberate press. Begin request recording after the listening sound. |
| F14 | Reminders, notes and to-dos | Community extension; not bundled | Integrated | 1 | Save the intended text and time; give a brief confirmation. Do not signal success for an unsaved request. |
| F15 | Scheduled reminders | Local focus/break signals; other schedules via extensions | Managed scheduler | 1 | Deliver due nudges within five seconds under normal connected operation; allow acknowledgement and snooze. |
| F16 | Microphone privacy | Yes | Yes | 2 | Hardware switch disables the microphone electrically and exposes its state. Muted means no audio leaves the device. |
| F17 | Calendar awareness | Community extension; not bundled | Integrated | 2 | Warn before meetings; no sound or movement during an active meeting. |
| F18 | Connection loss | Local operation | Local fallback | 1 | Retain focus, controls, local voice commands, world state and available presence/movement hardware. Flexible language understanding and connected services need an available backend; clearly indicate when unavailable. |

## Voice commands and scheduling

| ID | Feature | Basic | Connect | Required outcome |
| --- | --- | --- | --- | --- |
| F29 | Limited local voice commands | Yes | Yes | Recognize a small fixed command set on the device without cloud access. Candidates: start focus, stop timer and volume down. Final phrases and recognition reliability require hardware validation. |
| F30 | Natural-language schedules | Community extensions only | Yes | Interpret one-off, recurring and conditional reminders. Confirm the interpreted schedule before saving and ask when intent or timing is unclear. |

- Local commands must produce clear feedback and must not guess an unsupported action.
  The knob remains available; hardware mute also disables local voice commands.
- Connect example: “Remind me to drink water every hour while I’m at my desk.”
  Confirm the interval, active hours and presence condition before activating it.
- Support recurrence such as hourly, weekdays or specified times, with conditions
  such as at-desk presence, selected hours and outside meetings. Presence conditions
  require radar hardware; meeting conditions require calendar access.
- Users can review, edit, pause or cancel schedules in the app. Changes must update
  pending nudges and desktop escalations without duplicates.
- Define timezone, missed-occurrence and resumption rules before implementation.
  Do not send a burst of missed nudges when someone returns to the desk.
- Scope is desk reminders and routines, not unrestricted AI tasks. F30 follows the
  core reminder flow; it is not a prerequisite for the first voice bench check.

## Companion app

Basic includes setup, device controls and status. Connect includes the integrated experiences below. Community developers can build alternatives through the documented interfaces; a complete self-hosted Connect equivalent is not a Basic deliverable.

| ID | Feature | Stage | Required outcome |
| --- | --- | --- | --- |
| F23 | Basic app | 1 | Open-source setup, controls and status; usable without paying for Connect. |
| F24 | Community interfaces | 1 | Document audio, device events and commands; provide examples for third-party integrations. |
| F19 | Connect capture transcript | 1 | Show the full transcript after each capture. |
| F20 | Connect items, history, search and preferences | 1 | Inspect reminders, notes and to-dos; review history and configure behaviour away from the robot. |
| F21 | Connect desktop notification escalation | 2 | For user-selected event types, send one desktop notification if the device nudge remains unacknowledged after a configurable delay. Acknowledge, snooze, complete or cancel stops pending escalation. |
| F22 | Both apps: platform scope | 1 / later | PC first. Mobile and Bluetooth-assisted setup are deferred. |

### Notification escalation

- Start with reminders and focus/break nudges; users choose which types may escalate.
- Track lack of acknowledgement, not assumed lack of attention. PANDA cannot know whether a person noticed a nudge.
- Keep the same event across the robot and app so acknowledgement in either stops further alerts.
- Respect quiet hours and meeting quiet mode. Do not produce a backlog of duplicate alerts after reconnecting.
- The desktop app must be running and have notification permission. Show when desktop delivery is unavailable.
- Exact delay defaults and handling of expired events remain to be defined. No repeated escalation loop.

## Optional meeting agent — Connect

| ID | Feature | Scope | Required outcome |
| --- | --- | --- | --- |
| F25 | Join a meeting | Connect only; platform support to be decided | Join only when invited or explicitly enabled for the meeting. Make the agent's presence and transcription clear to participants and follow the platform's consent requirements. |
| F26 | Meeting transcript | Connect app | Save the transcript for review, with controls to stop capture and delete the record. Keep transcripts off the robot's display. |
| F27 | Extract reminders | Connect app | Identify tasks assigned to the user and proposed due times. Show the source passage; ask for confirmation or clarification before scheduling. |
| F28 | Deliver meeting reminders | Connect app + device | Save approved reminders, send their schedule to the paired PANDA and show whether delivery succeeded. PANDA nudges at the due time and supports snooze or acknowledgement. |

Cancellation or edits must update the device schedule. Reconnecting must not produce
duplicate reminders. Pending device delivery must be visible in the app. Local reminder
storage, timekeeping and restart behaviour need implementation requirements before
offline delivery can be promised. PANDA remains quiet during active meetings.

This extends the PDF's calendar awareness. It is optional, follows the core reminder
flow, and is not required to validate the first breadboard prototype. Meeting platforms,
retention defaults and the delivery mechanism remain to be decided.

## Build requirements shared by both editions

- USB power, no battery; signal levels and supply limits must match the selected parts.
- Keep the DevKit for v1. Final dimensions follow measured parts and fit checks.
- Keep controls reliable, sounds volume-limited and movement gentle.
- Keep hardware access separate from behaviour, use one pin map and log state changes.
- Validate power, audio, wiring and physical interactions on the actual device.
- Basic firmware, community app, interface examples and hardware build files are intended for open-source release; licences remain to be selected.

These cover the PDF's HW requirements and firmware maintenance constraints. Detailed
pin assignments, protocols and component choices belong in later implementation tasks.

## Boundaries

No chat screen, scrolling lists, feed, camera, battery, driving, touch keyboard or
human-language speech output. Voice capture supports quick desk tasks, not an open-ended
chat assistant. Detailed reading and multi-step choices belong in the app.

## Service requirements

- Basic is useful locally. Users may build or run community voice/AI integrations; PANDA does not promise a bundled self-hosted Connect backend.
- Connect provides the maintained paid app, hosted speech/AI, storage and integrated behaviours. Managed updates are included in scope; pricing, accounts and service guarantees remain undefined.
- Hardware capabilities are not gated by edition. Both editions follow the same product philosophy and microphone privacy rules.

## Changes from the original concept

- Both editions retain on-device focus and world behaviour during backend outages.
  Basic exposes audio and hardware interfaces; Connect supplies the maintained integrated experience. This supersedes the earlier full self-hosted Basic proposal.
- Presence and movement were not assigned to editions in the PDF. Including them
  in Basic is approved because they directly support the product philosophy.
- The three-week usefulness test moves to the integrated prototype with presence
  and head movement. Stage 1 gets reliability checks and a few working days of use.

## Before development

Create feature tickets using these IDs. Each ticket
should specify its gestures, failure behaviour and acceptance checks. Existing PDF
bench targets remain starting points, not evidence that a feature already works.
