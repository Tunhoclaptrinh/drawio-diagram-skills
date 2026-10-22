# Contributing

Thanks for your interest. Bug reports, new examples, better checks and skills for other diagram types are welcome. Issues and pull requests may be written in English or Vietnamese.

## Reporting a bug

Open an issue with:

- a **minimal** `.drawio` file that reproduces the problem (no internal documents, exam papers or personal data);
- the command you ran and the JSON report (`audit_drawio.py`, `doctor.py`);
- the skill version (`VERSION`), draw.io commit, Chrome version and operating system;
- the expected result and its basis (section/table/page of the OMG specification for notation issues).

Say which kind it is: the checker **rejects a correct diagram**, the checker **misses an error**, or a rendering/layout problem.

## Changing or adding checks

- Base rules on the official standard (OMG BPMN 2.0.2 for BPMN) and cite the section/table/page in code or docs. draw.io behaviour comes from its source at the pinned commit.
- Every new rule needs at least one **valid case that must pass** and one **invalid case that must be rejected** in `tests/`.
- Never change an example's business logic or notation to make the checker pass. When a rule rejects a correct diagram, fix the rule and add a test.
- Anything that cannot be decided automatically goes to `manual_review`; never treat it as passed silently. Update `references/coverage.md`.
- The core uses only the Python 3.10+ standard library.

## Adding a skill for another diagram type

Create `skills/<type>-drawio/`, for example `skills/uml-drawio/`:

```text
skills/<type>-drawio/
├── SKILL.md          # frontmatter: name, description, license
├── README.md         # goals, usage, coverage, sources
├── VERSION
├── LICENSE, NOTICE
├── references/       # notation rules, workflow, coverage
├── scripts/          # tools, including run_checks.py and package_skill.py
├── assets/           # synthetic examples, themes
└── tests/
```

Keep `SKILL.md` short and point to `references/` so agents read details only when needed. Add the skill to the table in the [README](README.md) and to the CI workflow. Use English, kebab-case names for folders and files.

## Before opening a pull request

```bash
python3 -B skills/<skill>/scripts/run_checks.py
python3 -B skills/<skill>/scripts/run_checks.py --render --drawio-root DRAWIO --output-dir output/render --report output/render/checks.json
python3 -B skills/<skill>/scripts/package_skill.py --output-dir output/candidate
python3 -B skills/<skill>/scripts/smoke_package.py output/candidate/<skill>-<version>-candidate.zip --drawio-root DRAWIO --report output/smoke.json
```

Open and look at the renderings affected by your change. Do not commit `output/`, `dist/`, caches or the draw.io source. Do not add personal data, client documents or third-party copyrighted material.

## Versions and releases

Each skill has its own `VERSION` following SemVer; `-rc.N` marks a release candidate (published as a GitHub pre-release). Tags look like `<skill>-v<version>`, for example `bpmn-drawio-v1.0.0-rc.2`. Record changes in [CHANGELOG.md](CHANGELOG.md). Maintainers follow [RELEASING.md](RELEASING.md).

## License

Contributions are released under [Apache-2.0](LICENSE), like the rest of the repository.
