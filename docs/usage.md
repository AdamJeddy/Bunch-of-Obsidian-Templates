# Setup and automatic values

## Insert any template with core Templates

1. Copy the category folders you want into a `Templates` folder inside your vault.
2. Enable **Settings → Core plugins → Templates**.
3. Set **Templates → Template folder location** to `Templates`.
4. Create a note with its final name, such as `The Dispossessed` or `Community Garden`.
5. Open the command palette and run **Templates: Insert template**. Choose the relevant template.
6. Edit Properties at the top, then fill in the body. Delete prompts or sections you do not need.

Only insert one full-note template into an empty note. These templates include frontmatter, which belongs at the beginning of a note.

## Fill values without enabling Templates

There are two built-in alternatives. They still use Obsidian core plugins, but do not need the Templates plugin or any community plugin.

### Daily notes

1. Enable **Settings → Core plugins → Daily notes**.
2. Under **Daily notes**, set the date format to `YYYY-MM-DD` and choose a new-file location such as `Daily Notes`.
3. Set **Template file location** to the copied `Daily & Weekly/Daily Note Template.md` inside your `Templates` folder.
4. Run **Daily notes: Open today's daily note**.

Daily notes creates the note and fills the template's date/time/title variables. Opening an existing daily note does not insert the template again. See [Obsidian's Daily notes guide](https://obsidian.md/help/plugins/daily-notes).

### Unique note creator

1. Enable **Settings → Core plugins → Unique note creator**.
2. Set its **Template file location** to the template you want to use.
3. Run **Unique note creator: Create new unique note**.

This creates a timestamp-named note using the configured template. Its title variable reflects the generated filename. Rename the note and heading afterward if you want a descriptive title. Change the configured template when you want a different note type. See [Unique note creator](https://obsidian.md/help/plugins/unique-note).

### No creation plugin at all

Copying a file or pasting Markdown does not evaluate `{{...}}` variables. Replace them manually, including the `created` timestamp. Obsidian's date property picker can help enter a date, but does not automatically populate all template fields.

Obsidian also exposes file creation/modification times through [Bases](https://obsidian.md/help/bases/functions). A Base can display `file.ctime` or `file.mtime`; that is a view of filesystem metadata, rather than an update to a note's YAML `created` property. Creation times can change when files are copied between systems.

## What updates automatically?

| Value | Behavior |
| --- | --- |
| `{{title}}` | Filename at insertion time |
| `{{date:YYYY-MM-DD}}` | Date supplied by the creation/insertion command |
| `{{time:HH:mm:ss}}` | Time supplied by the creation/insertion command |
| A manual prompt such as `[Company]` | You fill it in |
| Status, rating, task counts, and table totals | You update them manually |
| `last_reviewed` | You enter the date when you review the note |

Treat inserted values as snapshots. They do not keep changing with the clock or when you rename a file. Core Templates uses today's date rather than reading a date from the filename. Review dates when creating a note for another day, week, month, or year.

For core-compatible variables, use **Templates: Insert template**. A Templater insertion command does not convert the `{{...}}` syntax. See [core Templates variables](https://obsidian.md/help/plugins/templates).

## Optional advanced date arithmetic

The Month template leaves previous/next month links for you to fill, for example `[[2026-10|Previous month]]`. Formatting strings such as `MM-1M` do not subtract a month.

If you already use Templater, you can replace the navigation line with this snippet in a dedicated advanced template. Name the destination note `YYYY-MM`, then use Templater's insertion command:

```markdown
[[<% moment(tp.file.title, "YYYY-MM", true).subtract(1, "month").format("YYYY-MM") %>|Previous month]] | [[<% moment(tp.file.title, "YYYY-MM", true).add(1, "month").format("YYYY-MM") %>|Next month]]
```

This calculates from the note's month, including year boundaries. It does not convert the rest of a core template: replace its remaining core variables with Templater expressions, for example `{{title}}` → `<% tp.file.title %>` and the created timestamp → `<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>`. Use a valid `YYYY-MM` filename. See [Templater's documentation](https://silentvoid13.github.io/Templater/).

## Troubleshooting

- **Variables remain visible:** you copied text directly, used the wrong insertion command, or selected a different template. Follow one of the creation paths above.
- **A field became strange YAML:** edit source templates in Source mode and keep variables inside quotes. Obsidian's Properties editor can rewrite unquoted variables.
- **A link opens a missing note:** wiki links refer to notes in your own vault. Create the linked note or replace the sample name with yours.
- **A table does not calculate or sync:** ordinary Markdown tables are manual. Editing a body table does not change frontmatter.
- **The habit grid has extra dates:** cross out days outside that month. The table is a reusable 31-day layout, rather than a generated calendar.
- **Older notes look different:** updating a template does not migrate notes already created from it. See the [property migration notes](properties.md).
