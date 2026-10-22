# drawio-diagram-skills

[![Skills CI](https://github.com/Tunhoclaptrinh/drawio-diagram-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/Tunhoclaptrinh/drawio-diagram-skills/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

**English** · [Tiếng Việt](README.vi.md)

Agent skills that help an AI agent (Claude Code and other agents that read `SKILL.md`) **analyse a business process, model it and review it in draw.io**. The output is an editable `.drawio` file, PNG/SVG/PDF renderings produced by the real draw.io renderer, notation and layout checks, and a written explanation. Priorities: correct business logic → correct notation → readable layout → colour.

Most guides and examples are written in Vietnamese; the tooling, `SKILL.md` and the notation references are in English.

## Skills

| Skill | Diagram type | Version | Status |
|---|---|---|---|
| [bpmn-drawio](skills/bpmn-drawio/README.md) | BPMN 2.0.2 Process / Collaboration | `1.0.0-rc.2` | Pre-release for trial and feedback |

Each skill lives in `skills/<name>/` with its own version, tests and ZIP package. Other diagram types (for example UML, ERD, C4) are **planned, not implemented**; they will follow the same `skills/<type>-drawio/` layout.

![BPMN example: interlibrary loan, colour variant](examples/bpmn/interlibrary-loan/color/interlibrary-loan.png)

## What the BPMN skill checks

- Event triggers/results by position (OMG BPMN 2.0.2 tables 10.84–10.93): top-level start, subprocess start, event-subprocess start, catch, throw, boundary, end.
- Message flows by catch/throw direction; boundary events need an outgoing flow; Link pairs; gateways must split or merge; sequence flows stay inside one pool and scope.
- The colour variant differs from the normal variant only in colour; hidden strokes/text and low-contrast markers are rejected.
- Layout on rendered geometry: label overflow, labels leaving a lane, labels on a border, connectors crossing labels, overlapping connectors.

Checks are selective. They are not a full BPMN validator, an execution engine or OMG certification, and passing them is not a business validation. See the [coverage matrix](skills/bpmn-drawio/references/coverage.md).

## Documentation

| Document | Contents |
|---|---|
| [User guide](docs/user-guide.md) (Vietnamese) | Installation, prompts for agents, running the tools, reading audit reports, layout findings with pictures, themes, troubleshooting |
| [Examples](examples/README.md) | 9 example sets: `.drawio` in two variants, PNG/SVG, explanations |
| [bpmn-drawio README](skills/bpmn-drawio/README.md) · [SKILL.md](skills/bpmn-drawio/SKILL.md) | Design principles, components, sources; agent entry point |
| [BPMN rules](skills/bpmn-drawio/references/bpmn-rules.md) · [Coverage](skills/bpmn-drawio/references/coverage.md) | Event matrix, connection rules; what is automated and what needs review |
| [Contributing](CONTRIBUTING.md) · [Releasing](RELEASING.md) · [Changelog](CHANGELOG.md) | Bug reports, new rules and skills; release procedure; version history |

The BPMN standard is cited by name with a link to the official [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/PDF) publication; the specification PDF is not redistributed here.

## Install

1. Download `bpmn-drawio-<version>-candidate.zip` from **Releases**, verify it against the `.sha256` file and unzip it, keeping the `bpmn-drawio/` folder.
2. Put the folder where your agent loads skills, for example with Claude Code: `~/.claude/skills/bpmn-drawio/` (all projects) or `.claude/skills/bpmn-drawio/` (one project).
3. Check the package from the downloaded archive:

   ```bash
   python3 -B bpmn-drawio/scripts/smoke_package.py bpmn-drawio-1.0.0-rc.2-candidate.zip --report smoke.json
   ```

You can also clone this repository and copy `skills/bpmn-drawio/`.

## Requirements

- Python 3.10+ (the core uses the standard library only).
- Chrome or Chromium for rendering SVG/PNG/PDF.
- A local draw.io source tree supplied by you (not bundled). Tested with commit `17b367b91dbab91804f852645788d7ffb46dcb79` (draw.io 32.5.5):

  ```bash
  git clone --filter=blob:none https://github.com/jgraph/drawio.git
  git -C drawio checkout 17b367b91dbab91804f852645788d7ffb46dcb79
  python3 skills/bpmn-drawio/scripts/doctor.py --drawio-root drawio --output-dir output
  ```

Tested on Linux. Windows and macOS have not been verified.

## Tests

```bash
python3 -B skills/bpmn-drawio/scripts/run_checks.py
python3 -B skills/bpmn-drawio/scripts/run_checks.py --render --drawio-root drawio --output-dir output/render --report output/render/checks.json
```

CI ([workflow](.github/workflows/ci.yml)) runs the fast tests on Python 3.10, 3.12 and 3.14, packages the skill and smoke-tests the extracted ZIP; the rendering job runs on manual dispatch.

## Disclaimer

Not affiliated with or endorsed by OMG, JGraph (draw.io) or Bizagi. The colour profile name `bizagi-inspired` only refers to a presentation style; it is not an official Bizagi palette.

## License

[Apache-2.0](LICENSE). Copyright 2026 Tunhoclaptrinh — see [NOTICE](NOTICE). Keep LICENSE and NOTICE when redistributing.
