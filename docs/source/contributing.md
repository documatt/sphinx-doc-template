# Contributing

## Local development

### Changes to template are not reflected

Copier has a very specific algorithm to select which Git revision to use.

> By default, Copier will copy from the last release found in template Git tags, sorted as PEP 440, regardless of whether the template is from a URL or a local clone of a Git repository.

If the changes to template are not reflected after coping, add `-r HEAD`/`--vcs-ref HEAD` to `copier copy`.

> `-r, --vcs-ref VALUE:str`
>
> Git reference to checkout in `template_src`.
> If you do not specify it, it will try to
> checkout the latest git tag, as sorted using
> the PEP 440 algorithm. If you want to
> checkout always the latest version, use
> `--vcs-ref=HEAD`.
