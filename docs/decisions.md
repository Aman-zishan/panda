# Decisions

## Confirmed

| Date | Topic | Decision |
| --- | --- | --- |
| 2026-11-17 | Connect voice capture | [Outcomes approved](voice-capture.md): notes and tasks confirm after saving; reminders require schedule confirmation. Clarify uncertainty and prevent cancelled or duplicate saves. Basic retains limited local commands. |
| 2026-11-17 | Release scope | [Basic](basic-release.md) and [Connect](connect-release.md) scopes approved. Basic works independently; Connect starts with capture, reminders and the maintained app. Calendar and meeting-agent features come later. |
| 2026-11-17 | Audio distribution | Builders supply their own audio. The public release includes no recordings or audio-processing tools; prototype sources are referenced in the [Basic release scope](basic-release.md). |
| 2026-11-17 | Knob controls | [Table approved](knob-interactions.md). Turn to adjust, press to act, long press then release to start listening. No menus or double-clicks; timing needs hardware validation. |
| 2026-11-17 | Focus experience | [Flow approved](focus-experience.md). Default 25 minutes, explicit pause/resume, one completion cue and optional rest. No automatic restart or penalties; local focus works offline. |
| 2026-11-17 | Tiny world | [Rules approved](tiny-world.md). Focus adds growth; stopping loses nothing. No wilting in Stage 1. Later presence-based drooping is temporary and clears within a day. |
| 2026-11-17 | Release licences | Basic software: GPL-3.0-only. Hardware designs: CERN-OHL-S-2.0. Documentation: CC-BY-SA-4.0. Connect remains proprietary; branding and asset exceptions are listed in [LICENSE.md](../LICENSE.md). |
| 2026-11-17 | Name and logo | Accurate “Built with PANDA” and “Compatible with PANDA” descriptions are allowed. Modified products use their own branding; official status and product use of the logo require permission. See [BRAND.md](../BRAND.md). |
| 2026-11-17 | Prototype speech | English first. Start with Deepgram Nova-3; validate accuracy and response time with real commands. |
| 2026-11-17 | Prototype language model | Start with Groq-hosted GPT-OSS 20B for command interpretation. Validate extracted actions and schedules before relying on them. |
| 2026-11-17 | Prototype hosting | Run FastAPI on the builder's PC. Keep speech and model providers replaceable. GCP is a candidate for hosted Connect, not a final infrastructure decision. |
| 2026-11-17 | Basic voice | Include a small set of on-device commands for focus, timer and volume. Exact phrases require hardware validation; no cloud needed. |
| 2026-11-17 | Connect scheduling | Understand one-off, recurring and conditional reminder requests. Confirm schedules before saving; clarify missing timing or conditions. |
| 2026-11-17 | Notification escalation | Connect can send one desktop notification for selected nudges left unacknowledged after a configurable delay. Stop escalation on acknowledgement or snooze; respect quiet periods. |
| 2026-11-17 | Meeting agent | Optional Connect feature: join when invited/enabled, save transcripts, propose reminders for confirmation and send approved schedules to PANDA. |
| 2026-11-17 | Product philosophy | Approved. Use [the philosophy](product-philosophy.md) to assess every new feature. |
| 2026-11-17 | Product rule | Add device features only when physical interaction reduces distraction. Keep detail, history and settings in the app. |
| 2026-11-17 | PANDA Basic | Open-source firmware, hardware files, local focus/world, basic setup/control app and audio/event interfaces with examples. No complete Connect backend promised. |
| 2026-11-17 | Feature scope | [Feature matrix](feature-matrix.md) approved. Both editions retain on-device functions during backend outages; service-dependent functions need an available backend. |
| 2026-11-17 | PANDA Connect | Private, paid app maintained by the creator: integrated voice, reminders, notes, calendar, history, search, preferences, managed updates and hosted AI/storage. |
| 2026-11-17 | Project home | Public GitHub repository, GitHub Pages website, and GitHub issues and milestones. |
| 2026-11-17 | Validation timing | Check Stage 1 reliability over a few working days. Run the three-week usefulness test once presence and head movement work together. |
| 2026-11-17 | Validation records | Defer until hardware work begins; excluded from project-home ticket #5. |
| 2026-11-16 | Voice stack | Use ESP-SR with PANDA-specific firmware. |
| 2026-11-16 | Wake word | Use “Panda”; model support and recognition accuracy still need checking. |
| 2026-11-16 | Backend | Python + FastAPI. |
| 2026-11-16 | PC app | Electron + React + TypeScript. |

## Product promise

Approved 2026-11-17 · [#1](https://github.com/Aman-zishan/panda/issues/1)

PANDA (Presence-Aware Non-verbal Desk Assistant) is a calm desk companion that helps
you focus, capture thoughts and take breaks through simple physical interactions,
without pulling you away from your work.

## To decide

- Meeting platform support and transcript retention.
- Local voice command phrases and recognition targets.
- Schedule timezone, missed-occurrence and resumption rules.
- Connect pricing and service scope.
- Confirm production speech/model providers after prototype measurements.
- Select hosted Connect infrastructure; GCP is a candidate.
- Device/backend message format.
- GPIO assignments after inspecting the hardware.
- Enclosure dimensions after measuring the parts.
