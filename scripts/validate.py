"""Check template metadata, documentation links, and completed examples."""

from datetime import datetime
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


CREATED = "{{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}"


class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key in result:
                raise yaml.constructor.ConstructorError(
                    None, None, "duplicate or non-text property name", key_node.start_mark
                )
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def local_links(path, text):
    # Fenced examples illustrate syntax rather than link to repository files.
    text = re.sub(r"(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*(?:\n|$)", "", text)
    for target in re.findall(r"\]\(([^)\n]+)\)", text):
        url = urlsplit(target.strip().strip("<>"))
        if not url.scheme and not url.netloc and url.path:
            yield (path.parent / unquote(url.path)).resolve()


def validate_repository(root):
    root = root.resolve()
    contents = {}
    for folder, directories, filenames in os.walk(root):
        directories[:] = [d for d in directories if not d.startswith(".") and d not in {"node_modules", "__pycache__"}]
        for name in filenames:
            if name.endswith(".md"):
                path = Path(folder) / name
                contents[path] = path.read_text(encoding="utf-8-sig")

    templates = [p for p in contents if p.name.endswith("Template.md") and p.relative_to(root).parts[0] not in {"docs", "examples"}]
    examples = [p for p in contents if p.relative_to(root).parts[0] == "examples" and p.name != "README.md"]
    example_targets = {p.stem for p in examples} | {p.relative_to(root / "examples").with_suffix("").as_posix() for p in examples}
    errors = []
    links = {p: set(local_links(p, text)) for p, text in contents.items()}

    for path, targets in links.items():
        for target in sorted(targets):
            if not target.exists():
                errors.append(f"{path.relative_to(root)}: broken local link to {target}")

    for catalog in (root / "README.md", root / "docs/template-guide.md"):
        if catalog not in contents:
            errors.append(f"Missing catalog: {catalog.relative_to(root)}")
        else:
            for template in templates:
                if template not in links[catalog]:
                    errors.append(f"{catalog.relative_to(root)}: missing template {template.relative_to(root)}")

    for path in templates + examples:
        text = contents[path]
        label = path.relative_to(root)
        front = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.S)
        if not front:
            errors.append(f"{label}: missing frontmatter")
            continue
        try:
            props = yaml.load(front.group(1), Loader=UniqueKeyLoader)
        except yaml.YAMLError as error:
            errors.append(f"{label}: invalid YAML: {error}")
            continue
        if not isinstance(props, dict):
            errors.append(f"{label}: frontmatter must be a mapping")
            continue
        kind = props.get("note_type")
        if not isinstance(kind, str) or not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", kind):
            errors.append(f"{label}: note_type must be a lowercase identifier")
        tags = props.get("tags")
        if not isinstance(tags, list) or not tags or not all(isinstance(tag, str) and tag.strip() for tag in tags):
            errors.append(f"{label}: tags must be a nonempty list of text values")
        created = props.get("created")
        if created != CREATED:
            value = created.isoformat() if isinstance(created, datetime) else created
            try:
                if not isinstance(value, str) or "T" not in value:
                    raise ValueError
                datetime.fromisoformat(value)
            except ValueError:
                errors.append(f"{label}: created must be a scalar ISO timestamp")
        if "rating" in props:
            scale, rating = props.get("rating_scale"), props["rating"]
            if type(scale) not in (int, float) or scale <= 0:
                errors.append(f"{label}: rating_scale must be a positive number")
            elif rating is not None and (type(rating) not in (int, float) or not 0 <= rating <= scale):
                errors.append(f"{label}: rating must be between zero and rating_scale")
        if props.get("week") == "{{date:WW}}" and props.get("week_year") != "{{date:GGGG}}":
            errors.append(f"{label}: ISO week WW requires week_year GGGG")
        if "{{date:WW}}, {{date:YYYY}}" in text:
            errors.append(f"{label}: weekly heading must pair WW with GGGG")
        if path in templates:
            for variable in re.findall(r"\{\{([^{}]+)\}\}", text):
                if not re.fullmatch(r"title|(?:date|time)(?::[^{}\n]+)?", variable):
                    errors.append(f"{label}: unsupported variable {variable}")
                if re.search(r"MM[+-]\d+M", variable):
                    errors.append(f"{label}: formatting cannot perform month arithmetic")
            if "<%" in text:
                errors.append(f"{label}: core templates cannot require Templater expressions")
        else:
            if "{{" in text or "<%" in text:
                errors.append(f"{label}: completed examples must have resolved values")
            for target in re.findall(r"\[\[([^\]|#]+)[^\]]*\]\]", text):
                if target not in example_targets:
                    errors.append(f"{label}: unresolved example wiki link {target}")

    if not templates:
        errors.append("No templates found")
    return errors


if __name__ == "__main__":
    problems = validate_repository(Path(__file__).resolve().parents[1])
    if problems:
        print("\n".join(problems), file=sys.stderr)
    else:
        print("Repository checks passed.")
    raise SystemExit(bool(problems))
