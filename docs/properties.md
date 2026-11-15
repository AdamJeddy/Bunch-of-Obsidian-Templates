# Template properties

Properties are the YAML fields between the opening `---` lines. Edit them in Obsidian's Properties panel or in Source mode. They hold the structured facts about a note; body sections hold the details, reflections, and tasks.

## Shared fields

| Field | Format | How to use it |
| --- | --- | --- |
| `note_type` | Lowercase identifier such as `project` or `book` | Identifies the kind of note for filtering. Keep the template's value. |
| `created` | One timestamp, `YYYY-MM-DDTHH:mm:ss` | Filled when inserted through a supported creation command. It is a snapshot, not a live clock. |
| `tags` | YAML list | Add your own tags alongside the defaults. |
| `status` | Text | Use the values listed below for templates that have a status. |
| `project` | Quoted wiki link, for example `"[[Community Garden]]"` | Links a meeting, decision, or retrospective to its project. |

For example, a completed property block can look like this:

```yaml
---
note_type: project
created: "2026-11-02T09:30:00"
tags:
  - project
status: active
priority: medium
deadline: 2026-11-14
category: community
---
```

## Dates and numbers

- Use `YYYY-MM-DD` for dates: `birthday`, `deadline`, `meeting_date`, `decision_date`, `review_date`, `date_started`, `date_finished`, `applied_date`, `start_date`, `end_date`, and `last_reviewed`.
- Use one ISO timestamp for `created`. The default template uses explicit date/time formats so changing your global Templates format does not change the stored shape.
- Use numbers for ratings, pages, servings, budgets, and prep/cook times. Prep/cook times are in minutes. Put currency codes such as `AED` or `USD` in `currency`, rather than adding symbols to numeric budgets.
- `rating_scale` is 10 for books and media, and 5 for recipes. A rating of 4 with a scale of 5 is different from a rating of 4 with a scale of 10. Keep the scale when sharing or aggregating notes.
- Daily-note `mood` and `energy` use 1 (low) to 5 (high). Travel-journal mood is free text.
- `week` uses the ISO week number (`WW`); `week_year` uses its ISO week-year (`GGGG`). Around New Year, that year can differ from the calendar year. Lecture `week` means the teaching week and is entered manually.

Leave unknown values empty. Do not put placeholder text such as `YYYY-MM-DD` into a date property.

## Status values

| Note | Values |
| --- | --- |
| Project (`project`) | `planning`, `active`, `on-hold`, `completed`, `cancelled` |
| Job application (`job-application`) | `saved`, `applied`, `interviewing`, `offer`, `rejected`, `declined` |
| Job dashboard (`job-applications-dashboard`) | `active`, `paused`, `completed` |
| Media (`media`) | `plan to watch`, `watching`, `finished` |
| Trip (`trip`) | `planning`, `booked`, `in-progress`, `completed`, `cancelled` |
| Subject (`subject`) | `active`, `completed`, `dropped` |
| Decision (`decision`) | `proposed`, `accepted`, `superseded` |

Project priority uses `low`, `medium`, or `high`. Recipe difficulty uses `easy`, `medium`, or `hard`. Media `type` uses `movie` or `tv`; it is separate from `note_type`.

## Edit each fact in one place

When a template has a property for a fact, update that property. Editing ordinary body text or a table does not update YAML automatically. Use the body for information without a corresponding property.

The compact Book Table and manual dashboards intentionally store their entries in body tables. Their rows do not create individual notes or queryable properties. Use the full Book or Job Application template when you want one structured note per item.

Titles containing `{{title}}` are filled from the filename at insertion time. Renaming the file later does not rewrite the heading automatically.

## Updating an existing vault

These changes affect templates and future notes. Existing notes are not migrated automatically.

- Change `created: ["2026-11-02 09:30"]` to a scalar such as `created: "2026-11-02T09:30:00"` if you want the new shape. Update queries that indexed `created[0]`.
- Add the matching `note_type` if you want to include older notes in dashboards that filter on that field.
- Weekly Review and Meal Prep Plan now use `week_year` instead of `year`. Check the ISO week-year when migrating notes near New Year.
- Move values out of old body tables into the corresponding properties before relying on queries. Keep your existing notes until you have checked their contents.
- Media notes use the filename as their title. Existing custom `title` properties can remain; these templates no longer add a second title field.
- Original template filenames are preserved, including People v1/v2 and Book log, so existing template selections keep working.

See [Obsidian Properties](https://obsidian.md/help/properties) and [Moment's date formats](https://momentjs.com/docs/#/displaying/format/) for the underlying formats.
