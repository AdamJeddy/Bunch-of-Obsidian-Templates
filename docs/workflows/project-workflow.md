# A connected project workflow

Use one project note as the home for an outcome. Link meetings, decisions, and retrospectives to it as work progresses. The whole workflow works with built-in Obsidian features; Dataview is an optional addition at the end of this guide.

## Set up the notes

Copy the project templates into your vault's `Templates` folder. Keep your actual notes elsewhere, for example:

```text
My Vault/
  Templates/Projects & Goals/    <- reusable templates
  Projects/                    <- project and workflow notes you create
  People/                      <- contact notes
```

Use any naming scheme you like, provided links point to your actual notes. To insert templates, follow the [setup guide](../usage.md).

## From planning to review

| Step | Create from | What to do |
| --- | --- | --- |
| 1. Define an outcome | [Project](../../Projects%20%26%20Goals/Project%20Template.md) | Name it `Community Garden`; set status, priority, and deadline; define success and the next tasks. |
| 2. Capture a discussion | [Meeting Notes](../../Projects%20%26%20Goals/Meeting%20Notes%20Template.md) | Name it `2026-11-02 Garden Planning`; set `project: "[[Community Garden]]"`; link attendees and assign actions. Add its link to the project. |
| 3. Preserve a choice | [Decision Log](../../Projects%20%26%20Goals/Decision%20Log%20Template.md) | Name it `Garden Watering Plan`; link the project and meeting; compare options, record reasoning, and set decision status. |
| 4. Learn from the result | [Project Retrospective](../../Projects%20%26%20Goals/Project%20Retrospective%20Template.md) | Name it `2026-11-14 Garden Retrospective`; link the project; compare intended and actual results; create follow-up actions. |
| 5. Review your projects | [Project Dashboard](../../Projects%20%26%20Goals/Project%20Dashboard%20Template.md) | Add links to projects and retrospectives; keep next actions and review reminders here. Set `last_reviewed` when reviewing. |

For standalone meetings, leave `project` empty. For project meetings, use the same parent link on every associated note. A YAML link must be quoted:

```yaml
project: "[[Community Garden]]"
attendees:
  - "[[Sam Rivera]]"
```

The `project` link connects child notes back to their parent. Add links from the project to the child notes for convenient forward navigation. Obsidian's built-in Backlinks pane can also show notes that link to the project. Templates do not create the other notes automatically.

## Try the completed example

Open the repository's [examples folder](../../examples/README.md) as a separate vault, or copy its `Project workflow` and `People` folders into your vault. Start at [Project Dashboard](../../examples/Project%20workflow/Project%20Dashboard.md). All people and events are fictional.

Follow the links from the dashboard to the garden project, planning meeting, watering decision, and retrospective. [Sam Rivera's contact note](../../examples/People/Sam%20Rivera.md) shows how a People template fits into the same workflow.

## Optional: a dashboard powered by Dataview

Install [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) only if you want query results. You can add this block to your dashboard to read current values directly from project Properties:

````markdown
```dataview
TABLE status AS "Status", deadline AS "Deadline", priority AS "Priority"
FROM "Projects"
WHERE note_type = "project" AND status != "completed" AND status != "cancelled"
SORT deadline ASC
```
````

This assumes your actual notes are under `Projects`, as in the layout above. Replace that source folder if yours differs; keep templates outside the query's source folder. The bundled examples use `Project workflow` instead. The example project is completed, so it is intentionally excluded from this active-project query.

To list the notes attached to one project, add a second optional query:

````markdown
```dataview
TABLE note_type AS "Kind", project AS "Project"
FROM "Projects"
WHERE project = [[Community Garden]]
SORT created ASC
```
````

Change the project link to yours. These queries display results; they do not create notes, assign owners, or update manual tables. See [Dataview sources and filters](https://blacksmithgu.github.io/obsidian-dataview/queries/data-commands/).
