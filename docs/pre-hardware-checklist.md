# PANDA pre-hardware checklist

Use this checklist while waiting for the complete Stage 1 delivery. In this period,
the ESP32-S3, breadboards, jumper wires, microphone, amplifier, speaker, OLED and
rotary encoder are all treated as unavailable. Do not assign GPIO pins or claim that
hardware behaviour has passed until the breadboard is assembled and tested.

Use the [feature matrix](feature-matrix.md), [decision log](decisions.md) and
[product philosophy](product-philosophy.md) for current scope. The
[original concept PDF](PANDA_desk_companion_concept_v1.pdf) is a historical reference.

## 1. Lock the decisions that shape the build

- [x] Choose the wake word. `Panda` is the current candidate.
    - Panda
- [x] Choose the prototype speech-to-text provider: Deepgram Nova-3, English.
- [x] Choose the prototype language model: GPT-OSS 20B hosted by Groq.
- [x] Choose whether to adapt an existing ESP32 voice-firmware project or build new
      firmware.
    - existing ESP-SR firmware
- [x] Choose the backend language and framework: Python with FastAPI.
- [x] Choose the PC companion-app technology: Electron with React and TypeScript.

Record confirmed choices in [decisions.md](decisions.md). Update the feature matrix
when scope changes; keep the original concept PDF as a historical reference.

### Recorded decisions

| Date | Decision | Reason |
|---|---|---|
| 2026-11-16 | Backend: Python with FastAPI | It supports asynchronous I/O and persistent WebSocket connections while keeping the first backend quick to build and easy to change. |
| 2026-11-16 | PC companion app: Electron with React and TypeScript | One desktop codebase can ship on macOS, Windows and Linux, and it has mature support for local networking, notifications and desktop packaging. |

## 2. Define the product behaviour

- [ ] Write example spoken commands for a reminder, note, to-do, focus timer,
      snooze and acknowledgement.
- [ ] Define how the system turns a transcript into a reminder, note or to-do.
- [ ] Define the focus-session rules: default length, pause/resume, completion and
      what happens when a session is interrupted.
- [ ] Review the [tiny-world rules](tiny-world.md): focus, rest, growth and recovery.
      It must never punish and must recover within one day.
- [ ] List every user-visible device state: idle, listening, recording, processing,
      confirmed, focus running, focus complete, reminder, muted, offline and error.
- [ ] Decide what the LED, sound and OLED confirmation do for each state.

## 3. Write the interfaces before building them

- [ ] Define the persistent device-to-backend connection and message types.
- [ ] Define backend commands for sound, LED state, OLED update, confirmation,
      reminder and focus-timer actions.
- [ ] Define device events for wake word, audio capture, knob twist, short press,
      long press, connection changes and errors.
- [ ] Define the backend data model for reminders, notes, to-dos, focus sessions,
      world state and event history.
- [ ] Specify the structured serial-log format for every device state change.
- [ ] Decide how credentials are supplied locally. Wi-Fi credentials and API keys
      must stay out of Git.

## 4. Prepare the repository

- [x] Add a `README` describing PANDA and linking the project documents.
- [ ] Add run instructions when implementation begins.
- [ ] Add a `.gitignore` for local credentials, build outputs and editor files.
- [ ] Create folders for `firmware`, `backend`, `app`, `shared` and `tests` when
      implementation begins.
- [ ] Add a single, initially blank pin-map file. It becomes the only source of GPIO
      assignments after the breadboard is wired.
- [ ] Keep hardware access behind a firmware abstraction layer so the non-hardware
      logic can be developed and tested separately.
- [x] Add a decision log for confirmed choices and open decisions.

## 5. Prepare the physical build

- [ ] Check the order includes every Stage 1 item: ESP32-S3 DevKit N16R8 with
      headers, INMP441, MAX98357A with headers and terminal, 4-ohm 3-W speaker,
      0.96-inch I2C OLED, KY-040 encoder, two 830-point breadboards, all jumper-wire
      types and a USB-C data cable.
- [ ] Obtain a small screwdriver, side cutters, wire stripper and, if possible, a
      multimeter.
- [ ] Save each part listing and datasheet. Module-board pin labels and OLED driver
      variants need confirming against the specific item received.
- [ ] Sketch the Stage 1 desk layout: breadboards, USB cable route, speaker position
      and where the device will sit for the one-metre voice test.
- [ ] Do not finalize the shell, collar or head dimensions yet. Measure the actual
      parts first.

## 6. Prepare validation before assembly

- [ ] Make a Stage 1 bench-check sheet for microphone, speaker, OLED, onboard LED,
      knob, Wi-Fi and USB power.
- [ ] Write the one-metre voice-capture test: ten spoken reminders with the expected
      text and time, aiming for at least nine correct.
- [ ] Write the sound check: every defined state has its own identifiable sound.
- [ ] Write the LED timing check: listening, muted and offline appear within one
      second of the state change.
- [ ] Write the encoder check: distinguish twist, short press and long press, with
      no false presses during one hour idle.
- [ ] Write the focus check: complete a 25-minute session without app interaction.
- [ ] Prepare a daily three-week log. Each workday, use voice capture, the knob and
      the tiny world once presence and head movement are available. Stage 1 uses bench
      checks and a few working days of reliability checks.

## When the hardware arrives

1. Inspect each module against its saved listing and datasheet.
2. Assemble only the Stage 1 breadboard circuit and write the real pin map.
3. Bring up one component at a time: OLED, LED, encoder, speaker/amplifier, then
   microphone and Wi-Fi.
4. Record a bench check after each component works.
5. Check Stage 1 reliability for a few working days. Defer the three-week usefulness
   test until presence and head movement work together.

## Explicitly deferred until later stages

- Presence radar and hardware microphone mute switch (Stage 2).
- Servo, head, collar, visor LED, PETG shell, carrier board and final power design
  (Stage 3).
- A custom PCB. Build one only after the validation tests establish the final pin map,
  selected modules, power behaviour and enclosure layout.

## GitHub tracker

Milestones and active work tickets live in the
[GitHub tracker](https://github.com/Aman-zishan/panda/milestones). Keep temporary
thinking in the ignored `notes/` folder; move only settled decisions and evidence back
into `docs/`.

## Release plans

PANDA Basic includes open-source hardware files, firmware, a community setup/control
app and audio/event interfaces with examples. PANDA Connect is the private, paid app
with maintained integrations and hosted speech/AI services. The approved
[licence split](../LICENSE.md) covers software, hardware and documentation;
asset permissions and availability will be documented with each release.
