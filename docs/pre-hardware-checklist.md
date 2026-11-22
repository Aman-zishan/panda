# Stage 1 pre-hardware checklist

The breadboard has arrived. Check the remaining parts and prepare the tests for [bring-up and pairing (#16)](https://github.com/Aman-zishan/panda/issues/16).

## Prepare now

### Parts and desk layout

- [ ] Check the order includes every Stage 1 item: ESP32-S3 DevKit N16R8 with
      headers, INMP441, MAX98357A with headers and terminal, 4-ohm 3-W speaker,
      0.96-inch I2C OLED, KY-040 encoder, two full-size breadboards, all jumper-wire
      types and a USB-C data cable.
- [ ] Obtain a small screwdriver, side cutters, wire stripper and, if possible, a
      multimeter.
- [ ] Save each part listing and datasheet. Module-board pin labels and OLED driver
      variants need confirming against the specific item received.
- [ ] Sketch the Stage 1 desk layout: breadboards, USB cable route, speaker position
      and where the device will sit for the one-metre voice test.

### Bench tests to prepare

- [ ] Make a Stage 1 bench-check sheet for microphone, speaker, OLED, onboard LED,
      knob, Wi-Fi and USB power.
- [ ] Write the connected voice-capture prototype test at one metre: ten spoken reminders with the expected
      text and time, aiming for at least nine correct.
- [ ] Plan a speaker check: each approved cue is identifiable on the speaker, quiet states stay silent and visual feedback works with no clips installed.
- [ ] Write the LED timing check for listening, muted and offline. Target one second from the state change. Verify physical mute with the Stage 2 switch.
- [ ] Write the encoder check: distinguish twist, short press and long press, with
      no false presses during one hour idle.
- [ ] Write the focus check: complete a 25-minute session without app interaction.

## When the hardware arrives

1. Inspect each module against its saved listing and datasheet.
2. Assemble only the Stage 1 breadboard circuit and write the real pin map.
3. Bring up one component at a time: OLED, LED, encoder, speaker/amplifier, then
   microphone and Wi-Fi.
4. Record a bench check after each component works.
5. Check [Stage 1 reliability](https://github.com/Aman-zishan/panda/milestone/5) over a few working days.

## During implementation

### Voice phrases and device feedback

- [ ] Specify PANDA’s local focus, timer and volume phrases for hardware validation.
- [ ] Define spoken snooze and acknowledgement phrases for connected reminders.
- [ ] List every user-visible device state: idle, listening, recording, processing, awaiting confirmation,
      saved, save unconfirmed, focus running, paused, complete, reminder, muted, offline and error.
- [ ] Decide what the LED, sound and OLED confirmation do for each state.

### Device and backend interfaces

Publish PANDA’s device events, controls and audio interfaces with the public build.
Publish the Connect backend and integrations. Keep credentials and user records private.

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

### Repository setup

- [ ] Add run instructions when implementation begins.
- [ ] Extend the existing `.gitignore` to cover local credential files alongside build outputs and editor files.
- [ ] When implementation begins, organize public firmware, Connect app and backend, shared interfaces and tests here.
- [ ] Add a single, initially blank pin-map file. It becomes the only source of GPIO
      assignments after the breadboard is wired.
- [ ] Keep hardware access behind a firmware abstraction layer so the non-hardware
      logic can be developed and tested separately.

## Completed planning

The [decision log](decisions.md) records the prototype stack, device interactions, Connect requirements and release scope. The [eight sound cues](https://github.com/Aman-zishan/panda/issues/7) await speaker validation.

## Breadboard to final build

Follow the [roadmap](roadmap.md) from pairing to the integrated trial, enclosure and release. Choose a carrier or custom PCB only if validated wiring, power or fit requires one.
