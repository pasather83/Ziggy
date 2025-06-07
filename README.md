# Ziggy Chatbot
Ziggy is a Hotel Indigo staff chatbot powered by Flask + React.

## Handbook Integration
A helper script `backend/import_handbook.py` is provided to load sections from a
PDF staff handbook into `backend/knowledge_base.json`. The script relies on the
`PyPDF2` package. Install dependencies and run:

```bash
pip install -r backend/requirements.txt
python backend/import_handbook.py /path/to/handbook.pdf
```

The script extracts sections titled **Front Office**, **Housekeeping**,
**Engineering**, **Food & Beverage**, and **Human Resources**. Extracted text is
saved under a new `handbook` category in the knowledge base.
