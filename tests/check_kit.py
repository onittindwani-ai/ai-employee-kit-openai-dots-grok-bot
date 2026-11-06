"""Checks that the AI Employee Kit is complete and clean.

Standard library only. Run from anywhere:

    python3 tests/check_kit.py

Exit code 0 means every check passed. Exit code 1 lists each problem found.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

EXPECTED_GROUPS = {"sales": 9, "hiring": 8, "operations": 8}
MIN_TEAM_RECIPES = 5
EXPECTED_TEMPLATES = [
    "candidate-scorecard.md",
    "ideal-customer-profile.md",
    "crm-field-map.md",
    "weekly-report.md",
]
REQUIRED_SECTIONS = [
    "## Job in one line",
    "## What it does for you",
    "## Best tool for this job",
    "## Apps it needs connected",
    "## Setup prompt for OpenAI Dots",
    "## Setup prompt for Grok Bot",
    "## Rules and permission points",
    "## Daily or weekly output format",
    "## Sample output (example, synthetic)",
    "## How to check its work in 2 minutes",
]
REQUIRED_TOP_FILES = [
    "README.md",
    "CHOOSER.md",
    "SAFETY-AND-PERMISSIONS.md",
    "SOURCES.md",
    "CHANGELOG.md",
    "LICENSE",
]
VALID_TOOLS = ("OpenAI Dots", "Grok Bot", "Either")

# Dash characters that must never appear (written as escapes so this file stays clean).
BANNED_DASHES = {
    chr(0x2014): "an em dash",
    chr(0x2013): "an en dash",
    chr(0x2012): "a figure dash",
    chr(0x2015): "a horizontal bar",
    chr(0x2212): "a minus sign",
}

# Patterns that look like real keys or tokens. Built from parts so this file does not match itself.
SECRET_PATTERNS = [
    ("OpenAI style key", re.compile("s" + r"k-[A-Za-z0-9_\-]{20,}")),
    ("GitHub token", re.compile("gh" + r"[pousr]_[A-Za-z0-9]{30,}")),
    ("AWS access key", re.compile("AK" + r"IA[0-9A-Z]{16}")),
    ("Slack token", re.compile("xo" + r"x[abpr]-[A-Za-z0-9\-]{10,}")),
    ("Private key block", re.compile("-----BEGIN " + r"[A-Z ]*PRIVATE KEY-----")),
    ("Generic assigned key", re.compile(r"(?i)(api[_ ]?key|secret|token|password)\s*[:=]\s*['\"][A-Za-z0-9_\-]{12,}['\"]")),
]
EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
ALLOWED_EMAIL_DOMAINS = ("example.com", "example.org", "example.net")

TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".txt", ".json", ""}
SKIP_DIRS = {".git", "__pycache__"}


def text_files() -> list[pathlib.Path]:
    files = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return files


def employee_files() -> dict[str, list[pathlib.Path]]:
    found = {}
    for group in EXPECTED_GROUPS:
        folder = ROOT / "employees" / group
        found[group] = sorted(folder.glob("*.md")) if folder.is_dir() else []
    return found


def check_counts(errors: list[str]) -> None:
    for group, expected in EXPECTED_GROUPS.items():
        actual = len(employee_files()[group])
        if actual != expected:
            errors.append(f"employees/{group}: expected {expected} files, found {actual}")
    extra = [p for p in (ROOT / "employees").glob("*") if p.is_dir() and p.name not in EXPECTED_GROUPS]
    for folder in extra:
        errors.append(f"employees/{folder.name}: unexpected group folder")


def section_body(text: str, heading: str) -> str:
    start = text.find(heading)
    if start == -1:
        return ""
    rest = text[start + len(heading):]
    nxt = re.search(r"\n## ", rest)
    return rest[: nxt.start()] if nxt else rest


def check_employee(path: pathlib.Path, errors: list[str]) -> str:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    title_match = re.match(r"# (.+)", text)
    if not title_match:
        errors.append(f"{rel}: missing a '# Title' first line")
        title = ""
    else:
        title = title_match.group(1).strip()
    if not re.match(r"\d{2}-[a-z0-9-]+\.md$", path.name):
        errors.append(f"{rel}: file name should look like 01-some-name.md")
    for heading in REQUIRED_SECTIONS:
        if heading not in text:
            errors.append(f"{rel}: missing section '{heading}'")
        elif len(section_body(text, heading).strip()) < 40:
            errors.append(f"{rel}: section '{heading}' looks empty")
    for heading in ("## Setup prompt for OpenAI Dots", "## Setup prompt for Grok Bot"):
        body = section_body(text, heading)
        if "```text" not in body:
            errors.append(f"{rel}: '{heading}' has no paste in prompt block")
        for part in ("ROLE", "HOW TO DO THE JOB", "RULES YOU MUST ALWAYS FOLLOW", "REPORT FORMAT"):
            if part not in body:
                errors.append(f"{rel}: '{heading}' prompt is missing its {part} part")
    tool_body = section_body(text, "## Best tool for this job")
    if not any(f"**{tool}" in tool_body for tool in VALID_TOOLS):
        errors.append(f"{rel}: best tool must start with one of {VALID_TOOLS}")
    rules_body = section_body(text, "## Rules and permission points").lower()
    for verb in ("send", "post", "pay", "delete", "contact"):
        if verb not in rules_body:
            errors.append(f"{rel}: rules do not mention asking before it will {verb}")
    sample_body = section_body(text, "## Sample output (example, synthetic)").lower()
    if "example" not in sample_body:
        errors.append(f"{rel}: sample output is not labelled as an example")
    return title


def check_teams(errors: list[str]) -> None:
    recipes = [p for p in sorted((ROOT / "teams").glob("*.md")) if p.name != "README.md"]
    if len(recipes) < MIN_TEAM_RECIPES:
        errors.append(f"teams: expected at least {MIN_TEAM_RECIPES} recipes, found {len(recipes)}")
    for path in recipes:
        text = path.read_text(encoding="utf-8")
        links = set(re.findall(r"\(\.\./employees/[a-z]+/[0-9a-z-]+\.md\)", text))
        if len(links) < 2:
            errors.append(f"{path.relative_to(ROOT)}: a team needs at least 2 employees, found {len(links)}")
        if "## Hand off table" not in text:
            errors.append(f"{path.relative_to(ROOT)}: missing '## Hand off table'")
        if "Grok Bot" not in text or "Dots" not in text:
            errors.append(f"{path.relative_to(ROOT)}: should explain how to run it in both tools")


def check_chooser(titles: list[str], errors: list[str]) -> None:
    path = ROOT / "CHOOSER.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for title in titles:
        if title and f"[{title}]" not in text:
            errors.append(f"CHOOSER.md: does not list '{title}'")
    if "Claude Code" not in text:
        errors.append("CHOOSER.md: should cover when Claude Code is the better choice")


def check_links(errors: list[str]) -> None:
    for path in text_files():
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            resolved = (path.parent / target.split("#")[0]).resolve()
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link to '{target}'")


def check_clean_text(errors: list[str]) -> None:
    for path in text_files():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            for char, name in BANNED_DASHES.items():
                if char in line:
                    errors.append(f"{rel}:{lineno}: contains {name}")
            if path.suffix == ".md" and " - " in line.lstrip("- ").strip():
                errors.append(f"{rel}:{lineno}: a spaced hyphen is used as a dash")
            for name, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    errors.append(f"{rel}:{lineno}: looks like a {name}")
            for email in EMAIL_PATTERN.findall(line):
                if not email.lower().endswith(ALLOWED_EMAIL_DOMAINS):
                    errors.append(f"{rel}:{lineno}: contains an email address ({email})")


def check_files(errors: list[str]) -> None:
    for name in REQUIRED_TOP_FILES:
        if not (ROOT / name).exists():
            errors.append(f"missing {name}")
    for name in EXPECTED_TEMPLATES:
        if not (ROOT / "templates" / name).exists():
            errors.append(f"missing templates/{name}")


def main() -> int:
    errors: list[str] = []
    check_files(errors)
    check_counts(errors)
    titles = [check_employee(p, errors) for files in employee_files().values() for p in files]
    check_teams(errors)
    check_chooser(titles, errors)
    check_links(errors)
    check_clean_text(errors)

    counts = {g: len(f) for g, f in employee_files().items()}
    recipes = len([p for p in (ROOT / "teams").glob("*.md") if p.name != "README.md"])
    templates = len(list((ROOT / "templates").glob("*.md")))
    print(f"Employees: {sum(counts.values())} ({', '.join(f'{g} {n}' for g, n in counts.items())})")
    print(f"Team recipes: {recipes}")
    print(f"Templates: {templates}")
    print(f"Text files scanned: {len(text_files())}")
    if errors:
        print(f"\nFAILED with {len(errors)} problem(s):")
        for err in errors:
            print(f"  {err}")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
