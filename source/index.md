---
nosearch:
---

# Vítejte v Olivea 2025!

```{toctree}
:glob:

*
```

Only HTML or HTML-based builders.

## Deployment

- published at root / (not subfolder)

## File system organization

## Sphinx configuration

html_baseurl = 'https://documatt.com/blog'

## Nox configuration

### Supported builders

### Supported languages

### Building docs

Default builder/langauge

```
nox -s build
```

Specify builder/language

```
nox -s build -- html cs
```

### Build all builders/languages

```
nox -s build_all
```

### Redirect to default language

```
nox -s build_all redirect
```

### Clean build dir

```
nox -s clean
```

```
nox -s clean build
```

### Live preview

Default builder and language

```
nox -s preview
```

Pass builder and language on commandline

```
nox -s preview -- dirhtml cs
```
