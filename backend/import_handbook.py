import json
import re
from pathlib import Path
from typing import Dict

try:
    from PyPDF2 import PdfReader
except ImportError:
    raise SystemExit("PyPDF2 is required to run this script. Please install it via pip.")

DEPARTMENTS = [
    "Front Office",
    "Housekeeping",
    "Engineering",
    "Food & Beverage",
    "Human Resources",
]


def extract_sections(text: str) -> Dict[str, str]:
    sections = {dept: "" for dept in DEPARTMENTS}
    current = None
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        for dept in DEPARTMENTS:
            if re.fullmatch(dept, line, re.IGNORECASE):
                current = dept
                break
        else:
            if current:
                sections[current] += line + " "
    # strip whitespace
    return {k: v.strip() for k, v in sections.items() if v.strip()}


def load_pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
        text += "\n"
    return text


def update_knowledge_base(sections: Dict[str, str], kb_path: Path) -> None:
    if kb_path.exists():
        with open(kb_path, "r", encoding="utf-8") as f:
            kb = json.load(f)
    else:
        kb = {}
    kb.setdefault("handbook", {})
    for dept, content in sections.items():
        kb["handbook"][dept.lower().replace(" ", "_")] = content
    with open(kb_path, "w", encoding="utf-8") as f:
        json.dump(kb, f, indent=2)


def main(pdf_path: str, kb_path: str = "backend/knowledge_base.json") -> None:
    text = load_pdf_text(Path(pdf_path))
    sections = extract_sections(text)
    update_knowledge_base(sections, Path(kb_path))
    print(f"Imported {len(sections)} sections into {kb_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Import handbook PDF into the knowledge base")
    parser.add_argument("pdf", help="Path to the handbook PDF")
    parser.add_argument("--kb", default="backend/knowledge_base.json", help="Knowledge base JSON path")
    args = parser.parse_args()
    main(args.pdf, args.kb)
