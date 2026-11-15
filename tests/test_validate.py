from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.validate import validate_repository


TEMPLATE = '''---
note_type: project
created: "{{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}"
tags:
  - project
---
# {{title}}
'''


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.template = self.write("Projects/Project Template.md", TEMPLATE)
        self.write("README.md", "[Project](Projects/Project%20Template.md)\n")
        self.write("docs/template-guide.md", "[Project](../Projects/Project%20Template.md)\n")

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_repository_accepts_encoded_paths_and_ignores_code_examples(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n```markdown\n[illustration](missing.md)\n```\n")
        self.assertEqual(validate_repository(self.root), [])

    def test_invalid_metadata_is_rejected(self):
        cases = {
            "created": TEMPLATE.replace('"{{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}"', '["2026-11-15"]'),
            "note_type": TEMPLATE.replace("note_type: project", "note_type: 42"),
            "tags": TEMPLATE.replace("tags:\n  - project", "tags: project"),
            "duplicate": TEMPLATE.replace("note_type: project", "note_type: project\nnote_type: book"),
            "YAML": TEMPLATE.replace("note_type: project", "note_type: ["),
        }
        for name, text in cases.items():
            with self.subTest(name=name):
                self.template.write_text(text, encoding="utf-8")
                self.assertTrue(validate_repository(self.root))

    def test_broken_relative_documentation_link_is_rejected(self):
        self.write("docs/help.md", "[Missing](../Missing%20Note.md)\n")
        self.assertTrue(validate_repository(self.root))

    def test_each_catalog_must_include_every_template(self):
        for name in ("README.md", "docs/template-guide.md"):
            with self.subTest(name=name):
                path = self.root / name
                original = path.read_text(encoding="utf-8")
                path.write_text("# Catalog\n", encoding="utf-8")
                self.assertTrue(validate_repository(self.root))
                path.write_text(original, encoding="utf-8")

    def test_unsupported_variables_and_date_arithmetic_are_rejected(self):
        for expression in ("{{company}}", "{{date:MM-1M}}", "{{date:MM+1M}}", "<% tp.file.title %>"):
            with self.subTest(expression=expression):
                self.template.write_text(TEMPLATE + expression, encoding="utf-8")
                self.assertTrue(validate_repository(self.root))

    def test_iso_week_requires_the_matching_week_year(self):
        invalid = TEMPLATE.replace("---\n#", 'week: "{{date:WW}}"\nyear: "{{date:YYYY}}"\n---\n#')
        self.template.write_text(invalid, encoding="utf-8")
        self.assertTrue(validate_repository(self.root))
        valid = invalid.replace('year: "{{date:YYYY}}"', 'week_year: "{{date:GGGG}}"')
        self.template.write_text(valid, encoding="utf-8")
        self.assertEqual(validate_repository(self.root), [])

    def test_completed_example_requires_resolved_values_and_wiki_links(self):
        example = TEMPLATE.replace('"{{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}"', '"2026-11-15T09:30:00"').replace("{{title}}", "Garden")
        self.write("examples/Garden.md", example + "\n[[Missing Person]]\n")
        self.assertTrue(validate_repository(self.root))
        self.write("examples/Missing Person.md", example.replace("Garden", "Missing Person"))
        self.assertEqual(validate_repository(self.root), [])
        self.write("examples/Garden.md", TEMPLATE)
        self.assertTrue(validate_repository(self.root))

    def test_rating_must_fit_its_declared_scale(self):
        self.template.write_text(TEMPLATE.replace("---\n#", "rating: 8\nrating_scale: 5\n---\n#"), encoding="utf-8")
        self.assertTrue(validate_repository(self.root))


if __name__ == "__main__":
    unittest.main()
