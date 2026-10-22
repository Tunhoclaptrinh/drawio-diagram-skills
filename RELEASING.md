# Releasing

Maintainer checklist for publishing a skill version. Repository: <https://github.com/Tunhoclaptrinh/drawio-diagram-skills>.

## One-time setup: keep the e-mail address private

Commits pushed to GitHub expose the author e-mail. Use the GitHub no-reply address for this repository:

```bash
git config user.name "Tunhoclaptrinh"
git config user.email "146623045+Tunhoclaptrinh@users.noreply.github.com"
```

The number is the GitHub account id (`curl -s https://api.github.com/users/Tunhoclaptrinh` → `id`). Also enable, in GitHub **Settings → Emails**:

- **Keep my email addresses private**
- **Block command line pushes that expose my email** — GitHub then rejects any push containing the private address.

Check before pushing: `git log --format='%an <%ae> | %cn <%ce>' origin/main..HEAD` must show only the no-reply address. If an older commit still has another address and has **not** been pushed yet, rewrite it:

```bash
git rebase --root --exec 'git commit --amend --no-edit --reset-author'
```

Never rewrite commits that are already on GitHub without coordinating with other contributors.

Push over SSH: `git remote add origin git@github.com:Tunhoclaptrinh/drawio-diagram-skills.git` (the key must be registered on the account; check with `ssh -T git@github.com`).

## Each release

1. Update `skills/<skill>/VERSION` and the skill documentation; run the fast and render tests (see [CONTRIBUTING.md](CONTRIBUTING.md)).
2. Build the package and smoke-test it from the extracted ZIP:

   ```bash
   python3 -B skills/<skill>/scripts/package_skill.py --output-dir dist
   python3 -B skills/<skill>/scripts/smoke_package.py dist/<skill>-<version>-candidate.zip --drawio-root DRAWIO --report dist/smoke.json
   (cd dist && sha256sum <skill>-<version>-candidate.zip > <skill>-<version>-candidate.zip.sha256)
   ```

3. Add a section to [CHANGELOG.md](CHANGELOG.md); update `docs/` and `examples/` if behaviour or outputs changed.
4. Commit, tag and push:

   ```bash
   git commit -m "<skill> <version>: ..."
   git tag -a <skill>-v<version> -m "<skill> <version>"
   git push origin main
   git push origin <skill>-v<version>
   ```

5. On GitHub: **Releases → Draft a new release**, choose the tag, title `<skill> <version>`, paste the CHANGELOG section, attach `dist/<skill>-<version>-candidate.zip` and its `.sha256`. Tick **Set as a pre-release** for `-rc` versions. Publish.
6. Check **Actions**: the `Skills` workflow must pass on Python 3.10/3.12/3.14. Run the `render` job once with **Run workflow** for a release.

`dist/` is ignored by Git; release files are uploaded only as release assets.
