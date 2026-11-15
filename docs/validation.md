# Validation notes

Checked on November 15, 2026 using Obsidian 1.15.0 on Windows, with the default theme and no community plugins in the test vault. The temporary vault contained copies of the repository's templates and fictional examples.

## Desktop checks

| Check | Result |
| --- | --- |
| Insert Professional Contact into an empty named note using core Templates | Title and creation timestamp expanded; no unresolved variables remained in the saved note. |
| Edit metadata through Properties | Contact fields remained available above the body. Setting `created` to Date & time enabled the date/time editor and preserved the ISO value. |
| Read a note with hidden editing tips | HTML editing comments did not appear in reading mode. They remained visible while editing in Live Preview. |
| Create a daily note with Templates disabled | Daily notes used its configured template and expanded date/time variables without the Templates plugin. The saved note contained no unresolved variables. |
| Follow the completed workflow | Dashboard → Community Garden → planning meeting → Sam Rivera opened the expected existing notes, including the attendee link stored in Properties. |
| Read in a narrow desktop window | Contact properties and body remained usable at a 602 × 800 window size with the sidebar collapsed. Wide tables can require horizontal scrolling. |

The [property guide](properties.md) includes the one-time type setup discovered during these checks.

## Automated checks

The repository validator passes for all 27 templates and seven completed example notes. Its 12 unit tests cover malformed metadata, missing catalog entries, broken links, unresolved example values, rating ranges, week-year pairing, documented status values, and date formats/calendar validity. Invalid unquoted dates produce validation errors rather than crashing the checker.

Run the checks using the commands in [Contributing](../CONTRIBUTING.md#automated-checks).

## Coverage limits

- A narrow desktop window is not native Android or iOS testing; neither mobile app was exercised.
- Unique note creator, optional Templater snippets, and Dataview queries were not exercised in the app during this desktop check.
- Updating templates does not migrate existing notes or change their property types automatically.
