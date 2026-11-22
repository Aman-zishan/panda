# PANDA device release scope

Approved 2026-11-17 · [#10](https://github.com/Aman-zishan/panda/issues/10). PANDA handles local controls on the device.

## Standalone features

After setup, PANDA needs only USB power. Local features work without an account,
subscription, cloud API key, internet connection or running desktop app.

See [local and connected features](feature-matrix.md) for controls, offline focus, tiny-world persistence and local English voice commands. Validate wake-word and long-press activation, command phrases and recognition on hardware.

Later hardware adds presence-aware breaks, display sleep, head movement, visor feedback and physical microphone mute. Publish the parts list, verified wiring, enclosure files and build instructions. A custom PCB is optional.

## Audio files

Builders supply audio clips under the source's terms. The prototype uses
`animal-duckquack-rising.mp3` from [Casper's sound-effects library](https://www.casper.tw/sound-effects/license/).
Publish supported formats and cue assignments. Setup, focus and local voice must
work without clips, private recordings or audio tools. The display and light
communicate listening, confirmation and completion.

## Stage 1 preview

Label breadboard previews with tested parts and features. Candidates include the
timer, knob, display, local voice and saved world state. Presence, hardware mute,
head movement and the enclosure follow initial bring-up. Validate sensors and movement on the bench before packaging.

## Source-available release scope

Publish the firmware, hardware build files, PANDA Connect companion app, backend,
integrations and documented device and audio interfaces with a working example.
Builders can connect their own services. Local device features work offline after setup.
Credentials, user records and third-party assets require separate handling.
The [PANDA Noncommercial Licence](../LICENSE.md) permits noncommercial builds and sharing. Commercial use requires separate written permission.

## Ready to release when

- A builder can follow the published instructions, build the software and reproduce
  the supported hardware without access to a private repository or service.
- Setup and basic settings work through Connect; tested desktop platforms
  and known limitations are listed with the release.
- With internet and the app disconnected after setup, local controls, focus, world
  persistence and the documented voice commands still work.
- With no audio files installed, visual feedback still makes the same core actions
  understandable. Adding or replacing sounds does not require a hosted service.
- Every advertised hardware feature has been checked on the listed build. Muting
  the microphone prevents capture, including through extension interfaces.
- Source, dependencies and distributed assets have recorded reuse terms consistent
  with [LICENSE.md](../LICENSE.md). Nothing essential requires an unreleased private file.
