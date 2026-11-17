# Decisions

## Confirmed

| Date | Topic | Decision |
| --- | --- | --- |
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
- Speech-to-text and language-model providers.
- Sound vocabulary and asset licences.
- Device/backend message format.
- GPIO assignments after inspecting the hardware.
- Enclosure dimensions after measuring the parts.
- Release licences for Basic software, hardware and documentation.
