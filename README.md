# Ziggy Chatbot
Ziggy is a Hotel Indigo staff chatbot powered by Flask + React.

## Ingesting SOP files

Place your SOP documents inside `backend/SOPs`. Supported formats are TXT and MD by default. For DOCX and PDF files install `python-docx` and `PyPDF2`.

Run the ingestion script to merge all SOP files into `backend/knowledge_base.json`:

```bash
python backend/ingest_sops.py
```
