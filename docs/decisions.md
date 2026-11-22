# Decisions

## Product and release decisions

| Date | Topic | Decision |
| --- | --- | --- |
| 2026-11-22 | Community licence | New project-owned releases allow forks, modifications, personal builds and free sharing. Sales require separate written permission. Earlier releases retain their original grants. See [licence terms](../LICENSE.md). |
| 2026-11-22 | Build sequence and source | Develop Connect alongside each breadboard stage. Complete the integrated three-week trial before the final body. Publish the device and Connect sources together. |
| 2026-11-17 | Voice capture | Approved [save, confirmation and cancellation rules](voice-capture.md) for Connect. |
| 2026-11-17 | Release scope | Approved the [PANDA device build](basic-release.md) and [Connect release sequence](connect-release.md). |
| 2026-11-17 | Audio distribution | Eight cue meanings and distinct tunes approved in [#7](https://github.com/Aman-zishan/panda/issues/7). Builders supply audio. Public releases exclude recordings and private audio-processing tools. See [prototype source and terms](basic-release.md). |
| 2026-11-17 | Device behaviour | Approved [knob controls](knob-interactions.md), [focus sessions](focus-experience.md) and [tiny-world growth and recovery](tiny-world.md). |
| 2026-11-17 | Earlier release licences (superseded) | Basic software: GPL-3.0-only. Hardware designs: CERN-OHL-S-2.0. Documentation: CC-BY-SA-4.0. The original private Connect boundary was superseded on 2026-11-22; branding and asset exceptions are listed in [LICENSE.md](../LICENSE.md). |
| 2026-11-17 | Name and logo | Accurate “Built with PANDA” and “Compatible with PANDA” descriptions are allowed. Modified products use their own branding; official status and product use of the logo require permission. See [BRAND.md](../BRAND.md). |
| 2026-11-17 | Local voice | Include a small set of on-device commands for focus, timer and volume. Exact phrases require hardware validation; no cloud needed. |
| 2026-11-17 | Connect scheduling | Understand one-off, recurring and conditional reminder requests. Confirm schedules before saving; clarify missing timing or conditions. |
| 2026-11-17 | Notification escalation | Connect can send one desktop notification for selected nudges left unacknowledged after a configurable delay. Stop escalation on acknowledgement or snooze; respect quiet periods. |
| 2026-11-17 | Meeting agent | Optional Connect feature: join when invited/enabled, save transcripts, propose reminders for confirmation and send approved schedules to PANDA. |
| 2026-11-17 | Device and app roles | Approved the [product philosophy](product-philosophy.md) and [feature matrix](feature-matrix.md). Local functions survive backend outages. |
| 2026-11-17 | Project home | Public GitHub repository, GitHub Pages website, and GitHub issues and milestones. |
| 2026-11-17 | Validation timing | Check Stage 1 reliability over a few working days. Run the three-week usefulness test once presence and head movement work together. |
| 2026-11-17 | Validation records | Defer until hardware work begins; excluded from project-home ticket #5. |

## Prototype stack

| Date | Component | Choice and rationale |
| --- | --- | --- |
| 2026-11-17 | Prototype speech | English first. Start with Deepgram Nova-3; validate accuracy and response time with real commands. |
| 2026-11-17 | Prototype language model | Start with Groq-hosted GPT-OSS 20B for command interpretation. Validate extracted actions and schedules before relying on them. |
| 2026-11-17 | Prototype hosting | Run FastAPI on the builder's PC. Keep speech and model providers replaceable. GCP is a candidate for hosted Connect, not a final infrastructure decision. |
| 2026-11-16 | Voice stack | Use ESP-SR with PANDA-specific firmware. |
| 2026-11-16 | Wake word | Use “Panda”; model support and recognition accuracy still need checking. |
| 2026-11-16 | Backend | Python with FastAPI for asynchronous I/O, persistent WebSockets and rapid prototyping. |
| 2026-11-16 | PC app | Electron, React and TypeScript for a shared macOS, Windows and Linux codebase with local networking, notifications and desktop packaging. |

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
- GPIO assignments during breadboard assembly, after inspecting module pin labels.
- Enclosure dimensions after measuring the parts.
