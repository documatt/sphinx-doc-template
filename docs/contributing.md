# Contributing

## Local development

### Changes to a template are not reflected

Copier has a very specific algorithm for selecting which Git revision to use.

> By default, Copier will copy from the last release found in template Git tags, sorted as PEP 440, regardless of whether the template is from a URL or a local clone of a Git repository.

If the changes to the template are not reflected after coping, add `-r HEAD/--vcs-ref HEAD` to the `copier copy`.

> `-r, --vcs-ref VALUE:str`
>
> Git reference to checkout in `template_src`.
> If you do not specify it, it will try to
> checkout the latest git tag, as sorted using
> the PEP 440 algorithm. If you want to
> checkout always the latest version, use
> `--vcs-ref=HEAD`.

## Committing

Using conventional commits.

Most commits should have a scope either `template` (this repository itself) or `project` (files and folders generated from this template). (See [Copier basic concepts](https://copier.readthedocs.io/en/stable/#basic-concepts).)

For example:

- `chore(template): add git-cliff to dev dependencies` is change of this template repository
- `chore(project): update sphinx-reredirect 0.1.6` is change to projects generated from this template
- `docs: update CHANGELOG.md` has no scope because docs are just docs.

## Releasing

1. Create branch `release/vX.Y.Z`.
1. Work on changes.
1. Update changelog. Manually or with git-cliff tool (e.g., `git-cliff --prepend CHANGELOG.md --bump --unreleased`)
1. Fine tune `CHANGELOG.md`. Reorder, fix typos, reword, etc.
1. git-cliff also calculate new version number based on Git history. Remember it.
1. Increase version in `pyproject.toml`.
1. Create "release commit" containing changes to `pyproject.toml` with message `chore: release vX.Y.Z`. Release commit may contain other changes too, like to `CHANGELOG.md` and so on.
1. Create PR for branch. Review and merge to main branch.
1. Create tag `vX.Y.Z` on release commit.