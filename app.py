from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from name_matcher import NameMatcher, load_names
from recipe_finder import get_recipes, simple_suggestion
import os, threading
from pydantic import BaseModel
from typing import List, Optional

DATA_DIR = "data"
MODEL_DIR = "output_model"

app = FastAPI(title="AI Assignment - Ritik Verma")
app.mount("/static", StaticFiles(directory="static"), name="static")

names = load_names(os.path.join(DATA_DIR, "names.json"))
matcher = NameMatcher(names)

class NameQuery(BaseModel):
    name: str
    limit: Optional[int] = 10

class IngredientsQuery(BaseModel):
    ingredients: List[str]
    max_length: Optional[int] = 200

@app.get("/", response_class=HTMLResponse)
def home():
    return FileResponse("static/index.html")

@app.post("/api/match_name")
def api_match_name(q: NameQuery):
    out = matcher.match(q.name, limit=q.limit or 10)
    return JSONResponse(content=out)

@app.post("/api/get_recipes")
def api_get_recipes(q: IngredientsQuery):
    ingredients = [i.strip().lower() for i in q.ingredients if i.strip()]
    if not ingredients:
        raise HTTPException(status_code=400, detail="Provide at least one ingredient")
    matches = get_recipes(ingredients)
    suggestion = simple_suggestion(ingredients)
    return JSONResponse(content={"retrieved": matches, "suggestion": suggestion})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
