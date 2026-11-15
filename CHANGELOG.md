# Changelog

## Unreleased

### Added

- A project workflow with decision, retrospective, and dashboard templates, plus linked completed examples.
- Setup instructions for core Templates, Daily notes, Unique note creator, and manual use.
- Per-template naming and usage guidance, contribution guidance, and an MIT License.
- A People-template walkthrough with personal/professional examples, addressing the documentation request in [issue #1](https://github.com/AdamJeddy/Bunch-of-Obsidian-Templates/issues/1).
- Automated checks for template metadata, catalog coverage, local links, and completed examples.

### Changed

- Template editing tips are hidden comments, so generated notes keep their guidance in source without displaying setup instructions in reading mode.

- Templates use scalar ISO creation timestamps and explicit note types; migration guidance covers existing notes.
- Structured facts live in Properties, with manual dashboards and rating scales documented explicitly.
- People templates have descriptive catalog labels while retaining their original filenames.

### Fixed

- Repository checks reject invalid dates and unsupported status values, including malformed unquoted dates that previously caused the checker to crash.

- Weekly labels use the ISO week-year at New Year.
- Month navigation uses editable links in the core template; optional Templater arithmetic is documented separately.
- Setup no longer sends core template variables through Templater commands.
