# Changelog

Each skill is versioned separately. Git tags look like `<skill>-v<version>`, for example `bpmn-drawio-v1.0.0-rc.2`.

## bpmn-drawio 1.0.0-rc.2 — 2026-10-22 (pre-release)

First public release, for trial and feedback.

### Added

- Event trigger/result matrix by position (OMG BPMN 2.0.2, tables 10.84–10.93): top-level start, subprocess start, interrupting/non-interrupting event-subprocess start, catch, throw, interrupting/non-interrupting boundary, end.
- Message flows checked by catch/throw direction; boundary events need an outgoing sequence flow; normal-flow intermediate events need incoming and outgoing flows; Link events must pair by name within one process level; gateways must split or merge.
- Recognition of Call Activity and native draw.io lanes; event symbols the renderer does not draw are reported as unsupported.
- Colour variants may not hide strokes or text; markers need enough contrast to tell catch from throw.
- Layout checks on rendered geometry: label overflow, labels leaving a lane/pool, labels on a container border, connectors crossing labels, overlapping connectors.
- Reports record the tool version and digest; `smoke_package.py` verifies the package from the extracted ZIP.
- Apache-2.0 license.

### Changed

- Bundled pattern files renamed to `assets/bpmn-patterns.drawio` and `assets/bpmn-patterns-color.drawio`.

### Testing

75 fast tests; 28 pages rendered with the draw.io viewer; 41 new notation cases (the previous candidate handled 15 correctly, this one 41).

### Known limitations

Windows and macOS not verified. SVG output in `preserve` text mode contains a random viewer id, so its hash changes between renders. Choreography, Conversation, executable BPMN XML and automatic layout are not supported.

## bpmn-drawio 1.0.0-rc.1

Internal candidate, not published.
