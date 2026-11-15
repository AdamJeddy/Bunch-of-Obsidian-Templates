# Contributing

Templates, corrections, and clearer examples are welcome. Keep each contribution focused on one workflow or improvement.

## Template checklist

- Put reusable templates in the appropriate category folder, with a name ending in `Template.md`.
- Include `note_type`, a scalar ISO `created` timestamp, and a nonempty `tags` list. Follow the [property conventions](docs/properties.md).
- Use core-compatible `{{title}}`, `{{date:FORMAT}}`, and `{{time:FORMAT}}` variables. Quote variables in YAML.
- Keep community plugins optional. Document any advanced plugin-dependent snippet separately, with its requirements and a manual alternative.
- Use Properties as the home for structured fields. Avoid adding a second editable copy of the same fact to body tables.
- Keep instructions short and distinguish manual prompts from automatic values.
- Add a catalog entry to [README](README.md) and usage/naming guidance to the [template guide](docs/template-guide.md).
- For a workflow, show how notes link together and add a small, fictional completed example. Keep examples outside template folders.
- Preserve existing filenames where possible so users' configured template paths keep working.
- Credit external sources and include only material you have permission to contribute under the repository's [MIT License](LICENSE).

## Manual verification

1. Insert the template into an empty, named note using core Templates.
2. Confirm that automatic variables disappear and Properties remain valid.
3. Fill an example and check the links, tables, and checklists in reading mode.
4. If you changed date expressions, check month/year boundaries and leap years.
5. State what you tested in the pull request, including any optional plugins you used.
