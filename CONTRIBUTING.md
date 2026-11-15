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

See the [desktop validation record](docs/validation.md) for the tested paths and remaining platform coverage.

## Automated checks

Use Python 3.12 or newer and install the [development dependencies](requirements-dev.txt), preferably in a virtual environment:

```sh
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python scripts/validate.py
```

The same commands run in GitHub Actions on pushes and pull requests. The checker validates frontmatter (including duplicate keys), shared properties, supported variables, known date-format regressions, rating scales, and coverage in both catalogs. It checks local inline Markdown links outside fenced code blocks and wiki links between completed examples. It does not resolve links in reusable templates, since those refer to the user's vault, or test external websites and live Obsidian behavior.

Populated date properties must use real `YYYY-MM-DD` dates; template date variables must specify that format explicitly. Status values follow the [property conventions](docs/properties.md), and unknown values may be left empty. When adding a date field or changing the supported statuses, update both that guide and the definitions in [the validator](scripts/validate.py).
