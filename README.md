# Bunch of Obsidian Templates

A collection of Markdown templates for [Obsidian](https://obsidian.md): planning, journaling, studying, reading, and organizing everyday life. Pick the templates you need and adapt them to your vault.

**No community plugins are required.** Automatic date, time, and title insertion uses Obsidian's built-in template variables. Plain Markdown sections, tables, links, and checklists work without an insertion plugin.

## Quick start

1. Download or clone this repository.
2. Create a `Templates` folder in your vault. Copy the category folders you want into it. Keep documentation and examples outside that folder.
3. Enable **Settings → Core plugins → Templates**. Set **Templates → Template folder location** to `Templates`.
4. Create and name a new note, then run **Templates: Insert template** from the command palette.
5. Fill the note's Properties and replace manual prompts such as `[Topic]`. These prompts are not automatic variables.

For daily notes, you can instead select a template directly in **Daily notes → Template file location**, even with the Templates plugin disabled. Unique note creator also supports a configured template. See [setup and plugin-free options](docs/usage.md).

The `{{date}}`, `{{time}}`, and `{{title}}` syntax belongs to core Templates. Templater uses a different syntax and is optional. Dates are filled once at insertion, rather than continuously updated.

## Guides

- [Setup, automatic values, and troubleshooting](docs/usage.md)
- [How to use each template and name your notes](docs/template-guide.md)
- [People templates: setup, contact links, and completed examples](docs/people.md)
- [Properties, status values, and migration notes](docs/properties.md)
- [Connected project workflow and completed examples](docs/workflows/project-workflow.md)
- [Contributing a template or improvement](CONTRIBUTING.md)

Start a connected workflow with **Project → Meeting → Decision → Retrospective**, and review it from a Project Dashboard. The [completed example](examples/README.md) includes a contact note and works without community plugins.

## Template catalog

All templates below use core-compatible variables and need no community plugins. Suggested filenames and editing instructions are in the [template guide](docs/template-guide.md).

| Category | Template | Use it for |
| --- | --- | --- |
| Daily & Weekly | [Daily Note](Daily%20%26%20Weekly/Daily%20Note%20Template.md) | Daily focus, tasks, meals, gratitude, and reflection |
| Daily & Weekly | [Weekly Review](Daily%20%26%20Weekly/Weekly%20Review%20Template.md) | Wins, lessons, and next week's priorities |
| Monthly & Yearly | [Month](Monthly%20%26%20Yearly/Month%20Template.md) | Monthly goals, events, and reflection |
| Monthly & Yearly | [Year](Monthly%20%26%20Yearly/Year%20Template.md) | Annual review and next year's goals |
| Books | [Book](Books/Book%20Template.md) | One structured note per book, with quotes and takeaways |
| Books | [Book Table](Books/Book%20Table%20Template.md) | Compact, manually filled book information |
| Books | [Book Log](Books/Book%20log%20Template.md) | A manual annual reading log |
| People | [Personal Contact](People/People%20v1%20Template.md) | Friends, family, and personal connections; original filename: People v1 |
| People | [Professional Contact](People/People%20v2%20Template.md) | Work contacts and networking; original filename: People v2 |
| Projects & Goals | [Goal Setting](Projects%20%26%20Goals/Goal%20Setting%20Template.md) | Goals across life areas and quarterly checkpoints |
| Projects & Goals | [Project](Projects%20%26%20Goals/Project%20Template.md) | Objectives, milestones, tasks, and progress |
| Projects & Goals | [Meeting Notes](Projects%20%26%20Goals/Meeting%20Notes%20Template.md) | Agenda, discussion, and action items |
| Projects & Goals | [Decision Log](Projects%20%26%20Goals/Decision%20Log%20Template.md) | Options, reasoning, consequences, and follow-up |
| Projects & Goals | [Project Retrospective](Projects%20%26%20Goals/Project%20Retrospective%20Template.md) | Outcomes, lessons, and improvements for next time |
| Projects & Goals | [Project Dashboard](Projects%20%26%20Goals/Project%20Dashboard%20Template.md) | Project links, next actions, and review reminders |
| Habits | [Habit Tracker](Habits/Habit%20Tracker%20Template.md) | A manual monthly grid with daily marks |
| Career | [Job Applications Dashboard](Career/Job%20Applications%20List%20Template.md) | A manual overview of your job search |
| Career | [Job Application](Career/Job%20Application%20Tracker%20Template.md) | One application, with contacts, timeline, and interview preparation |
| Travel | [Trip Planner](Travel/Trip%20Planner%20Template.md) | Itinerary, budget, transport, and packing |
| Travel | [Travel Journal](Travel/Travel%20Journal%20Template.md) | Daily memories, expenses, and reflections |
| Food | [Recipe](Food/Recipe%20Template.md) | Ingredients, cooking instructions, and notes |
| Food | [Meal Prep Plan](Food/Meal%20Prep%20Plan%20Template.md) | Weekly meals, groceries, and preparation |
| Food | [Grocery List](Food/Grocery%20List%20Template.md) | Categorized shopping checklist and budget |
| Media | [Movie / TV Log](Media/Movie%20TV%20Log%20Template.md) | One movie or series, with a review and viewing log |
| Study | [Lecture Notes](Study%20-%20University%20-%20School/Lecture%20Notes%20Template.md) | Key points, detailed notes, questions, and homework |
| Study | [Study Schedule](Study%20-%20University%20-%20School/Study%20Schedule%20Template.md) | Weekly timetable and assignment planning |
| Study | [University Subject](Study%20-%20University%20-%20School/University%20Subject%20Template.md) | Course information, assignments, dates, and lecture links |

## Plugin requirements

| Feature | What it needs |
| --- | --- |
| Edit copied Markdown, tables, checklists, and links | No plugins; replace variables manually |
| Insert a chosen template into an existing note | Built-in **Templates** |
| Create daily notes from a configured template | Built-in **Daily notes**; Templates can be disabled |
| Create timestamp-named notes from a configured template | Built-in **Unique note creator**; Templates can be disabled |
| Prompts, date arithmetic, and custom creation scripts | Optional [Templater](https://silentvoid13.github.io/Templater/) |
| Queries that aggregate note properties | Optional [Dataview](https://blacksmithgu.github.io/obsidian-dataview/); ordinary tables remain manual |

Calendar and Tasks are optional additions to your own workflow. The supplied templates do not depend on them.

## Contributing and license

Template ideas, fixes, and clearer examples are welcome. Follow the [contribution checklist](CONTRIBUTING.md) and keep templates easy to adapt.

Run the [repository checks](CONTRIBUTING.md#automated-checks) before submitting changes. User-facing changes are recorded in the [changelog](CHANGELOG.md).

This collection is available under the [MIT License](LICENSE).

