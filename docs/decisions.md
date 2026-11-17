# Decision log

This log records important product and technology choices. Each entry explains the
reason and tradeoff. When a decision changes, add a new entry referring to the old
one so the reasoning remains visible.

## 2026-11-17 — Product promise (proposed)

**Ticket:** [#1 — Write PANDA's one-sentence promise](https://github.com/Aman-zishan/panda/issues/1)

**Proposed promise:** PANDA is a calm desk companion that helps you focus, capture
thoughts and take breaks through simple physical interactions, without pulling you
away from your work.

**Reason:** Describe the benefit first, without requiring someone to understand the
hardware or software. Focus, capture and breaks connect directly to the planned
experience and the product philosophy.

**Tradeoff:** This describes the overall product direction. Voice capture belongs
to Connect; individual editions need their own feature descriptions. This is a
design promise, not a claim that the hardware has already been validated.

**Status:** Proposed for review. Once approved, use this sentence in the README.

## 2026-11-17 — PANDA Basic and Connect

**Decision:** Plan a self-contained Basic edition with local controls, sounds, a
focus timer and a tiny world. Plan Connect for voice understanding, reminders,
notes, calendar integration and the companion app.

**Reason:** Basic should be useful on its own and give builders a complete project
to learn from. Connect provides the additional connected experience.

**Tradeoff:** The two experiences need clear boundaries and separate validation.
Basic firmware, schematics and enclosure files are intended for public release;
Connect implementation will remain closed. Release licences are not yet selected.

## 2026-11-17 — Public project home

**Decision:** Use this public repository for the website, product documents and
future Basic releases. Host the website on GitHub Pages and track tasks in GitHub
issues and milestones.

**Reason:** Visitors and contributors can find the project and its progress in one
place. Documentation changes can be reviewed alongside the project files.

**Tradeoff:** Public documentation must distinguish planned behaviour from tested
features. The original concept PDF is historical and may differ from later decisions.

## 2026-11-17 — Physical interactions first

**Decision:** Include a device feature only when physical presence makes it faster,
calmer or more meaningful. Keep detailed reading, history and settings in the app.

**Reason:** PANDA should reduce distraction at the desk. It should not duplicate
something a phone already does well without distraction.

**Tradeoff:** PANDA deliberately limits its display and interaction complexity.
See the [product philosophy](product-philosophy.md) for the feature criteria.

## 2026-11-16 — Voice processing foundation

**Decision:** Use Espressif ESP-SR as the planned voice-processing foundation, with
PANDA-specific device behaviour around it. Use “Panda” as the intended wake word.

**Reason:** Reusing wake-word and audio-processing components reduces the work needed
to build the first voice loop.

**Tradeoff:** ESP-SR is a component stack, not complete PANDA firmware. Hardware
integration is still required. Availability and accuracy of a suitable “Panda”
wake-word model remain to be confirmed on the actual microphone setup.

## 2026-11-16 — Backend: Python and FastAPI

**Decision:** Use Python with FastAPI for the connected backend.

**Reason:** It supports asynchronous provider requests and persistent device
connections while keeping the prototype straightforward to develop.

**Tradeoff:** Framework choice alone does not guarantee fast responses. Speech
processing, provider latency and connection behaviour must be measured together.

## 2026-11-16 — Companion app: Electron, React and TypeScript

**Decision:** Use Electron with React and TypeScript for the PC companion app.

**Reason:** A shared desktop codebase suits the planned transcript, history and
settings screens across macOS, Windows and Linux.

**Tradeoff:** Electron has a larger download and memory footprint. Packaging and
platform-specific behaviour will still need verification on each supported system.

## Open decisions

- Speech-to-text and language-model providers.
- Final sound vocabulary and asset licences.
- Device/backend message format.
- GPIO assignments, after inspecting the delivered hardware.
- Final enclosure dimensions, after measuring and testing the parts.
- Release licences for Basic software, hardware and documentation.
