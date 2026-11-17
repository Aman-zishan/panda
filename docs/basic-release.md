# PANDA Basic release scope

Draft for [#10](https://github.com/Aman-zishan/panda/issues/10). The
[feature matrix](feature-matrix.md) defines the editions; this page defines what
someone must receive to build and use Basic without a private PANDA service.

## A useful standalone companion

After setup, Basic runs its local features with just USB power. It requires no
PANDA account, subscription, cloud API key or continuously running desktop app.
The [product philosophy](product-philosophy.md) applies: physical controls and brief
feedback on the device; setup and detailed settings in the companion app.

| Included in the eventual public build | What the person can do |
| --- | --- |
| Firmware and physical controls | Use the knob, display, status light and local feedback without internet. |
| Focus and tiny world | Start, pause and complete focus; retain world growth across restarts, following the approved experience rules. |
| Local voice | Activate listening by wake word or long press and use a small documented English command set for focus, timer and volume. Exact phrases and recognition quality require validation. |
| Presence and breaks | Use presence-aware rest, break nudges and display sleep with the supported sensor. |
| Physical character and privacy | Use the supported head movement, visor and hardware microphone mute. |
| Community desktop app | Set up the device, change basic settings, assign builder-supplied sounds, use controls and inspect status locally. |
| Build materials | Obtain source, parts list, verified wiring, enclosure files and instructions to reproduce the supported build. A custom PCB is not required. |
| Extension interfaces | Access documented device events, controls and audio interfaces, with a working community integration example. |

The microphone has a useful local role. Connecting it to an external service is an
optional extension, not a requirement for Basic's bundled commands or controls.

Audio files are supplied by each builder and are not included in the public release.
Our prototype uses `animal-duckquack-rising.mp3` from Casper's sound-effects site;
builders can choose their own sounds under the source's applicable terms. See
[Casper's usage terms](https://www.casper.tw/sound-effects/license/).

Missing sound files must not prevent setup, focus or local voice controls. Listening,
confirmation and completion remain clear through the display and status light.
The release documents the supported file format and cue assignments so builders
can supply clips without our private audio tools or recordings.

## What can arrive earlier

A Stage 1 breadboard preview can cover the timer, knob, display, local voice and
saved world state as they are validated. Label previews with their actual supported
features and parts. They do not imply that presence, the mute switch, head movement
or the enclosure have been tested. Those remain part of Basic as later hardware
stages become ready, rather than paid upgrades.

## Outside the bundled release

Basic does not include flexible AI requests, voice notes or to-dos, connected
reminder scheduling, calendar and meeting services, desktop escalation, hosted
storage or managed AI. Those are Connect features. Community integrations may add
alternatives; Basic does not promise a complete self-hosted version of Connect.

No phone-like dashboard, scrolling task lists, feeds or productivity scores belong
on the device. Detailed connected experiences stay in their companion applications.

## Ready to release when

- A builder can follow the published instructions, build the software and reproduce
  the supported hardware without access to a private repository or service.
- Setup and basic settings work through the community app; tested desktop platforms
  and known limitations are listed with the release.
- With internet and the app disconnected after setup, local controls, focus, world
  persistence and the documented voice commands still work.
- With no audio files installed, visual feedback still makes the same core actions
  understandable. Adding or replacing sounds does not require a hosted service.
- Every advertised hardware feature has been checked on the listed build. Muting
  the microphone prevents capture, including through extension interfaces.
- Source, dependencies and distributed assets have recorded reuse terms consistent
  with [LICENSE.md](../LICENSE.md). Nothing essential requires an unreleased private file.

These are release requirements, not claims that the current planning repository
already contains a working Basic build.
