# Major Release Notes Template

Use this template when preparing release notes for a major version release. Copy the content below into a new file at `docs/admin/release_notes/version_X.Y.md` and fill in each section.

## How to Identify Breaking Changes

When preparing a major release, review all commits since the last release tag to identify breaking changes. Focus on `.textfsm` file diffs and the `index` file:

* **Field renames**: `Value` lines where the field name changed
* **Output format changes**: `Value` type changes (e.g., scalar to `List`)
* **New fields added**: New `Value` lines added to existing templates
* **Parsing behavior changes**: Regex changes that alter what gets captured or matched
* **Index pattern changes**: Changes to command matching patterns in the `index` file

Use `git log vPREV..HEAD --oneline` to list all commits, then inspect each with `git show <commit> -- '*.textfsm'` to find template-level changes.

## Formatting Rules

* All PR references must be markdown links: `[#NNNN](https://github.com/networktocode/ntc-templates/pull/NNNN)`
* Template names in tables should be backtick-wrapped (e.g., `cisco_ios_show_version`)
* Use `→` for field rename notation in the summary table
* Use `->` in detailed migration guide text
* Include before/after Python code examples for field renames and output format changes

## Release Checklist

1. Bump `version` in `pyproject.toml`
2. Update Python `classifiers` in `pyproject.toml` if Python version support changed
3. Update `python` dependency constraint in `[tool.poetry.dependencies]` if minimum changed
4. Update `target-version` in `[tool.black]` if Python minimum changed
5. Create `docs/admin/release_notes/version_X.Y.md` using the template below
6. Add entry to `mkdocs.yml` nav (at the top of the Release Notes list)
7. Add entry to `docs/admin/release_notes/index.md` (at the top of the table)

---

## Template

````markdown
# Release Notes vX.Y.Z

## Major Release Highlights

<!-- Brief paragraph summarizing the release. -->

## Breaking Changes Summary

The following templates have breaking changes in this release. If you use any of these templates, review the details below and the [Migration Guide](#migration-guide) before upgrading.

| Template | Change Type | Details |
|----------|------------|---------|
| `template_name` | Field renamed | `old_name` → `new_name` |
| `template_name` | Output format changed | Description of what changed |
| `template_name` | New field added | `field_name` (type) |
| `template_name` | New fields added | `field1`, `field2` |
| `template_name` | Parsing behavior changed | Description of what changed |
| `template_name` | Index pattern changed | Description of what changed |

## Breaking Changes

### Python Version Support

<!-- Only include if Python version support changed. -->

* **Dropped Python X.Y support** - Minimum Python version is now X.Z+
* **Added Python X.W support** - Now supports Python X.Z, X.A, X.B, and X.W

### Field Name Changes (Breaking)

* **Template display name**: Renamed `old_field` to `new_field` for reason in [#NNNN](https://github.com/networktocode/ntc-templates/pull/NNNN)

### Output Format Changes (Breaking)

* **Template display name**: Description of output format change in [#NNNN](https://github.com/networktocode/ntc-templates/pull/NNNN)
  - Old: `example of old output`
  - New: `example of new output`

### New Fields Added to Existing Templates (Schema Changes)

* **Template display name**: New `field_name` field added in [#NNNN](https://github.com/networktocode/ntc-templates/pull/NNNN)

### Parsing Behavior Changes

* **Template display name**: Description of parsing change in [#NNNN](https://github.com/networktocode/ntc-templates/pull/NNNN)

## What's Changed

### New Templates

* Add Platform command description in [#NNNN](https://github.com/networktocode/ntc-templates/pull/NNNN)

### Enhanced Templates

* Enhancement description in [#NNNN](https://github.com/networktocode/ntc-templates/pull/NNNN)

### Bug Fixes

* Fix description in [#NNNN](https://github.com/networktocode/ntc-templates/pull/NNNN)

## Migration Guide

### Python Version

<!-- Only include if Python version support changed. -->

Ensure you are running Python X.Z or higher before upgrading. Python X.Y is no longer supported.

### Field Name Changes

If you are using the following template, update your code to use the new field name:

**Template display name:**
- `old_field` -> `new_field`

```python
# Before (vPREV)
result["old_field"]

# After (vCURR)
result["new_field"]
```

### Output Format Changes

**Template display name - `field_name`:**

Description of what changed and how to update code:

```python
# Before (vPREV)
# old usage pattern

# After (vCURR)
# new usage pattern
```

### New Fields in Existing Templates

The following templates now include additional fields in their output. If your code does strict schema validation or exact dictionary comparison, update accordingly:

| Template | New Field(s) |
|----------|-------------|
| `template_name` | `field_name` (type) |

### Parsing Behavior Changes

**Template display name:**
Description of what changed and how to update code.

## Statistics

- **Total Changes**: N commits
- **New Templates**: N
- **Enhanced Templates**: N
- **Bug Fixes**: N

**Full Changelog**: [vPREV...vCURR](https://github.com/networktocode/ntc-templates/compare/vPREV...vCURR)
````
