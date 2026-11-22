# Stage 1 pre-hardware checklist

The breadboard has arrived. All five [M2 requirements tickets](https://github.com/Aman-zishan/panda/milestone/3) are complete. While the remaining parts arrive, check the order and prepare the bench tests. Firmware and backend work can proceed alongside component testing.

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

- [ ] Specify Basic’s local focus, timer and volume phrases for hardware validation.
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
- [ ] When implementation begins, organize public firmware, companion app, shared interfaces
      and tests here alongside the Connect app and backend.
- [ ] Add a single, initially blank pin-map file. It becomes the only source of GPIO
      assignments after the breadboard is wired.
- [ ] Keep hardware access behind a firmware abstraction layer so the non-hardware
      logic can be developed and tested separately.

## Completed planning

- [x] Record prototype stack and wake-word choices in the [decision log](decisions.md).
- [x] Review [voice capture](voice-capture.md), [focus sessions](focus-experience.md)
      and [tiny-world behaviour](tiny-world.md).
- [x] Review [Basic](basic-release.md) and [Connect](connect-release.md) release scope.
- [x] Review [knob controls](knob-interactions.md) and the [eight sound cues](https://github.com/Aman-zishan/panda/issues/7). Physical knob and speaker checks remain pending.
- [x] Define when [connected reminders](connect-release.md#reminder-behaviour) nudge, repeat and stop. [#12](https://github.com/Aman-zishan/panda/issues/12)
- [x] Specify [device feedback and companion-app responsibilities](product-philosophy.md#device-and-app). [#13](https://github.com/Aman-zishan/panda/issues/13)
- [x] Document [listening, transmission, transcript-only history and physical mute](voice-capture.md#voice-capture-privacy). [#14](https://github.com/Aman-zishan/panda/issues/14)
- [x] Define the [open-source release scope](basic-release.md#open-source-release-scope). [#15](https://github.com/Aman-zishan/panda/issues/15)
- [x] Publish the project README and decision log.

## Breadboard to final build

| Milestone | What to demonstrate |
| --- | --- |
| [M3 · Bring-up](https://github.com/Aman-zishan/panda/milestone/4) | Bring up the modules, run local focus, pair Connect, display device status and disconnect the app while the timer runs. |
| [M4 · Capture and reminders](https://github.com/Aman-zishan/panda/milestone/5) | Speak a request, confirm on the device, edit in Connect and receive the nudge. Exercise snooze, desktop escalation and reconnect. Record reliability over several working days. |
| [M5 · Integrated bench](https://github.com/Aman-zishan/panda/milestone/6) | Add radar, physical mute, visor feedback and a servo on a temporary fixture. Check presence, movement, quiet mode, calendar and opt-in meeting flows together with Connect. Log voice capture, knob use and the tiny world each workday during the three-week trial. Record results and resolve failures across the feature matrix. |
| [M6 · Final form factor](https://github.com/Aman-zishan/panda/milestone/7) | Start after the complete device and companion experience passes on the breadboard. Measure and fit the shell, head, collar, speaker, mic and USB port. Recheck power, movement, acoustics and app behaviour in the assembled body. |

Choose a carrier or custom PCB only if the validated wiring, power and fit call for one.
