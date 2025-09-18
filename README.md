# AI Assignment - Ritik Verma

This repository contains two tasks:

## Task 1: Name Matching
- Uses `rapidfuzz` to compute similarity between an input name and a dataset of names.
- Endpoint: `POST /api/match_name` (JSON body: { "name": "...", "limit": 10 })

## Task 2: Recipe Chatbot (Local)
- A lightweight recipe retriever and template-based suggester.
- Endpoint: `POST /api/get_recipes` (JSON body: { "ingredients": ["eggs","onion"] })
- A static web UI is available at `/` which calls the endpoints.

## Files
- `app.py` - FastAPI app
- `name_matcher.py` - name matching logic (uses RapidFuzz)
- `recipe_finder.py` - recipe retrieval and suggestion logic
- `data/names.json` - name dataset (30+ names)
- `static/index.html` & `static/chat.js` - simple UI
- `requirements.txt` - packages to install

## Setup
```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Open http://127.0.0.1:8000 in your browser.

## Notes
- This implementation uses a small in-repo dataset and does not require heavy ML packages.
- Optional: add a fine-tuned model and extend app.py to load it for generation.
