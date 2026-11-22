# PANDA Basic release scope

Approved 2026-11-17 · [#10](https://github.com/Aman-zishan/panda/issues/10). Basic is the standalone public build.

## Standalone features

After setup, Basic needs only USB power. Local features work without an account,
subscription, cloud API key, internet connection or running desktop app.

| Included in the eventual public build | What the person can do |
| --- | --- |
| Firmware and physical controls | Use the knob, display, status light and local feedback without internet. |
| Focus and tiny world | Start, pause and complete focus; retain world growth across restarts, following the approved experience rules. |
| Local voice | Activate listening by wake word or long press and use a small documented English command set for focus, timer and volume. Exact phrases and recognition quality require validation. |
| Presence and breaks | Use presence-aware rest, break nudges and display sleep with the supported sensor. |
| Physical character and privacy | Use the supported head movement, visor and hardware microphone mute. |
| Connect companion app | Set up the device, change basic settings, assign builder-supplied sounds, use controls and inspect status locally. |
| Build materials | Obtain source, parts list, verified wiring, enclosure files and instructions to reproduce the supported build. A custom PCB is not required. |
| Extension interfaces | Access documented device events, controls and audio interfaces, with a working community integration example. |

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

## Open-source release scope

Publish the firmware, hardware build files, PANDA Connect companion app, backend,
integrations and documented device and audio interfaces with a working example.
Builders can connect their own services. Local device features work offline after setup.
Credentials, user records and third-party assets require separate handling.
See [licences](../LICENSE.md) for terms applying to released materials.

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
