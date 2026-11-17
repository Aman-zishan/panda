# PANDA repository structure

Keep one private repository while PANDA is being proven. Do not create a public code
repository yet. This makes it hard to publish private work accidentally and keeps the
project simple while it changes quickly.

## Suggested layout

```text
PANDA/
├── README.md                 What PANDA is and the current stage
├── docs/                     Product plan, decisions and validation records
│   ├── product-philosophy.md The device's purpose and feature guardrails
│   ├── decisions/            Short records of choices and why they were made
│   ├── validation/           Bench checks and daily-use logs
│   ├── designs/              Drawings, dimensions and later build notes
│   └── assets/               Sound sources, licences and visual references
├── notes/                    Local scratch notes; deliberately ignored by Git
├── firmware/                 Private device behaviour
├── backend/                  Private connected service
├── app/                      Private companion app
└── hardware/                 Private wiring, boards and enclosure work
```

Create folders when the work begins; empty folders do not need to be committed now.

## What belongs where

- `docs/product-philosophy.md`: the rules used to accept or reject device features.
- `docs/decisions`: choices that affect scope, experience, publishing or future work.
- `docs/validation`: what actually happened during bench checks and daily use.
- `docs/designs`: sketches and measured dimensions; keep early ideas separate from
  final measured designs.
- `docs/assets`: a source link and licence record for every borrowed sound or visual.
- `notes/`: personal working notes, rough ideas and temporary material. It stays out
  of Git until an item is ready to become a decision, design or validation record.
- `firmware`, `backend`, `app`, `hardware`: working product material; all private
  until the M7 publishing decision.

## The "not a phone" product rule

PANDA has a physical job: it listens, responds with sound/light/posture, offers a
quick knob interaction, and shows only immediate confirmation or its small world.

The companion app may show detail, history, editing and settings. PANDA itself should
not become a dashboard, chat screen, scrolling list, keyboard, feed or a place for
long-form notifications. Before adding a feature, ask whether the knob, a sound, a
single glance or the companion app already handles the job better.

## Later public release

After M7, create a separate public `panda-basic` repository only for approved PANDA
Basic material. Do not mirror the private repository: copy selected files into the
public project deliberately, with their licences and source records.
