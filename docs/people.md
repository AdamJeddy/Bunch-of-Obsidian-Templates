# Using the People templates

Use one note per person and link to that note from meetings, projects, or your journal. The People templates need no community plugins, scripts, Dataview, or custom theme.

## Choose a template

| Template | Best for | What it includes |
| --- | --- | --- |
| [Personal Contact (People v1)](../People/People%20v1%20Template.md) | Friends, family, and everyday connections | How you met, likes/dislikes, connections, and interaction notes |
| [Professional Contact (People v2)](../People/People%20v2%20Template.md) | Colleagues, collaborators, and networking | Occupation/company, contact details, professional links, relationships, and important dates |

The names v1/v2 identify two alternatives. You can use either, or combine the sections you need into one template. You do not need to create two notes for the same person.

## Create your first contact

1. Copy the chosen template into your vault, for example `Templates/People/People v1 Template.md`.
2. Enable Obsidian's built-in **Templates** plugin and set its template folder to `Templates`. No community plugin is needed for this path.
3. Create an empty note named after the person, for example `Maya Chen`, in a folder such as `People` outside your template folder.
4. Run **Templates: Insert template** and choose the People template. It fills the creation timestamp and uses the filename for the heading.
5. Set birthday and location in Properties. For a professional contact, also set occupation and company there. Leave unknown values empty.
6. Fill the body sections you want to use and remove the rest. Keep birthdays in the birthday property; use Important Dates for other events.

For manual use, copy the template into a new note and replace every `{{...}}` variable yourself. For other built-in creation paths, see the [setup guide](usage.md).

## Properties and links

Use a date such as `1996-05-12` for a known birthday. Add nicknames to `aliases` if you want to find the person by those names. For example, this is a filled-in personal contact's property block:

```yaml
---
note_type: person-personal
created: "2026-11-02T08:45:00"
tags:
  - people
  - contact
aliases:
  - Maya
birthday: 1996-05-12
location: Fictional neighborhood
---
```

Link to the contact from another note with `[[Maya Chen]]`. In a meeting's YAML, use a quoted link:

```yaml
attendees:
  - "[[Maya Chen]]"
```

This creates a connection between the notes. It does not copy contact details into the meeting or create a contact note automatically. When two people share a name, give their notes distinct filenames and link to the correct one.

Add a dated bullet under Notes / Logs after an interaction, for example `2026-11-02 — Met through Sam at garden planning.` These logs, table entries, anniversaries, and follow-up dates are manual. The templates do not send reminders or sync contacts.

## Completed examples

The examples are fictional. Open the repository's `examples` folder as an Obsidian vault, or copy its `People` and `Project workflow` folders together into your vault:

- [Maya Chen — personal contact](../examples/People/Maya%20Chen.md)
- [Sam Rivera — professional contact](../examples/People/Sam%20Rivera.md)
- [A planning meeting linked to a contact](../examples/Project%20workflow/2026-11-02%20Garden%20Planning.md)

The [template guide](template-guide.md) covers the rest of the collection, and the [property guide](properties.md) explains formats and conventions.
