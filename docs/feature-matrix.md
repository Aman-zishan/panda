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
| F02 | Focus sessions | Local; voice via community integration | Local + integrated voice start | 1 | Set and complete a session without app interaction; clearly signal its end. |
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
| F13 | Wake word and long-press capture | Capture and audio interface; community integration for understanding | Integrated capture and understanding | 1 | Accept a short request after a wake word or deliberate press. Begin request recording after the listening sound. |
| F14 | Reminders, notes and to-dos | Community extension; not bundled | Integrated | 1 | Save the intended text and time; give a brief confirmation. Do not signal success for an unsaved request. |
| F15 | Scheduled reminders | Local focus/break signals; other schedules via extensions | Managed scheduler | 1 | Deliver due nudges within five seconds under normal connected operation; allow acknowledgement and snooze. |
| F16 | Microphone privacy | Yes | Yes | 2 | Hardware switch disables the microphone electrically and exposes its state. Muted means no audio leaves the device. |
| F17 | Calendar awareness | Community extension; not bundled | Integrated | 2 | Warn before meetings; no sound or movement during an active meeting. |
| F18 | Connection loss | Local fallback | Local fallback | 1 | Make unavailable connected functions clear. Retain on-device focus, controls, world state and available presence/movement hardware if the backend is unreachable. Voice understanding, stored-item access and calendar services require an available configured backend. |

## Companion app

Basic includes setup, device controls and status. Connect includes the integrated experiences below. Community developers can build alternatives through the documented interfaces; a complete self-hosted Connect equivalent is not a Basic deliverable.

| ID | Feature | Stage | Required outcome |
| --- | --- | --- | --- |
| F23 | Basic app | 1 | Open-source setup, controls and status; usable without paying for Connect. |
| F24 | Community interfaces | 1 | Document audio, device events and commands; provide examples for third-party integrations. |
| F19 | Connect capture transcript | 1 | Show the full transcript after each capture. |
| F20 | Connect items, history, search and preferences | 1 | Inspect reminders, notes and to-dos; review history and configure behaviour away from the robot. |
| F21 | Connect desktop notifications | 2 | Surface relevant device events without becoming a general notification feed. Delivery and duplication rules need definition. |
| F22 | Both apps: platform scope | 1 / later | PC first. Mobile and Bluetooth-assisted setup are deferred. |

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
