import os
import json
import argparse
from pathlib import Path

try:
    from docx import Document
except ImportError:
    Document = None

try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

def extract_text(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {'.txt', '.md'}:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    elif ext == '.docx' and Document:
        doc = Document(path)
        return '\n'.join(p.text for p in doc.paragraphs)
    elif ext == '.pdf' and PyPDF2:
        text = ''
        with open(path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ''
        return text
    return ''

def main():
    parser = argparse.ArgumentParser(description='Ingest SOP files into knowledge_base.json')
    parser.add_argument('directory', nargs='?', default='backend/SOPs',
                        help='Directory containing SOP files')
    parser.add_argument('--kb', default='backend/knowledge_base.json',
                        help='Path to knowledge base JSON')
    args = parser.parse_args()

    sop_dir = Path(args.directory)
    kb_path = Path(args.kb)

    if not sop_dir.exists():
        print(f'Directory {sop_dir} does not exist.')
        return

    if kb_path.exists():
        with open(kb_path, 'r', encoding='utf-8') as f:
            kb = json.load(f)
    else:
        kb = {}

    kb.setdefault('sops', {})

    for file in sop_dir.iterdir():
        if file.is_file():
            text = extract_text(file).strip()
            if text:
                kb['sops'][file.stem.lower()] = text

    with open(kb_path, 'w', encoding='utf-8') as f:
        json.dump(kb, f, indent=2, ensure_ascii=False)

    print(f'Ingested {len(kb.get("sops", {}))} SOP files into {kb_path}')

if __name__ == '__main__':
    main()
