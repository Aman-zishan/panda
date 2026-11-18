# Stage 1 pre-hardware checklist

The complete breadboard kit is pending. Assign GPIO pins after wiring and record
hardware results only after bench testing.

## Product behaviour

- [x] Record prototype stack and wake-word choices in the [decision log](decisions.md).
- [x] Review [voice capture](voice-capture.md), [focus sessions](focus-experience.md)
      and [tiny-world behaviour](tiny-world.md).
- [x] Review [Basic](basic-release.md) and [Connect](connect-release.md) release scope.
- [ ] Define exact local voice phrases and spoken snooze/acknowledgement commands.
- [ ] List every user-visible device state: idle, listening, recording, processing,
      confirmed, focus running, focus complete, reminder, muted, offline and error.
- [ ] Decide what the LED, sound and OLED confirmation do for each state.

## Device and backend interfaces

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

## Repository setup

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

## Parts and desk layout

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

## Bench tests to prepare

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
      the tiny world once presence and head movement are available.

## When the hardware arrives

1. Inspect each module against its saved listing and datasheet.
2. Assemble only the Stage 1 breadboard circuit and write the real pin map.
3. Bring up one component at a time: OLED, LED, encoder, speaker/amplifier, then
   microphone and Wi-Fi.
4. Record a bench check after each component works.
5. Check Stage 1 reliability over a few working days.

## Later hardware stages

- Presence radar and hardware microphone mute switch (Stage 2).
- Servo, head, collar, visor LED, PETG shell, carrier board and final power design
  (Stage 3).
- A custom PCB. Build one only after the validation tests establish the final pin map,
  selected modules, power behaviour and enclosure layout.
