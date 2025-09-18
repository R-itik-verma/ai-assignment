# recipe_finder.py
from typing import List, Dict
import os

# Small recipes dataset for retrieval
RECIPES = [
    {
        "title": "Simple Scrambled Eggs with Onions",
        "ingredients": ["eggs", "onion", "salt", "pepper", "butter"],
        "steps": [
            "Chop the onions finely.",
            "Heat a pan with butter over medium heat; sauté onions until soft.",
            "Beat eggs with salt and pepper.",
            "Pour eggs into pan with onions. Stir gently until just cooked.",
            "Serve hot with bread or rice."
        ]
    },
    {
        "title": "Onion-Egg Fried Rice (Quick)",
        "ingredients": ["cooked rice", "eggs", "onion", "soy sauce", "oil"],
        "steps": [
            "Heat oil, sauté chopped onions until translucent.",
            "Push onions aside, scramble eggs in the same pan.",
            "Add cooked rice and soy sauce; toss with onions and eggs.",
            "Garnish and serve."
        ]
    },
    {
        "title": "Omelette with Caramelized Onions",
        "ingredients": ["eggs", "onion", "salt", "pepper", "oil", "cheese"],
        "steps": [
            "Slice onions thinly and caramelize over low heat until golden.",
            "Beat eggs with salt and pepper. Pour into nonstick pan.",
            "Add caramelized onions and cheese to one half, fold and serve."
        ]
    },
    {
        "title": "Egg-Onion Curry (Simple)",
        "ingredients": ["eggs", "onion", "tomato", "turmeric", "cumin", "oil"],
        "steps": [
            "Chop onion and tomato. Fry onions until golden.",
            "Add spices and tomato; cook to a paste.",
            "Add water, halved boiled eggs; simmer 5 minutes."
        ]
    }
]

def _score_recipe(ingredients: List[str], recipe: Dict) -> int:
    s = 0
    lower_req = [i.lower() for i in recipe['ingredients']]
    for ing in ingredients:
        # count presence
        if ing in lower_req or any(ing in r for r in lower_req):
            s += 1
    return s

def get_recipes(ingredients: List[str], top_k: int = 5):
    scored = []
    for r in RECIPES:
        score = _score_recipe(ingredients, r)
        if score>0:
            scored.append((score, r))
    scored.sort(key=lambda x: (-x[0], x[1]['title']))
    return [ { "title": r['title'], "score": int(s), "ingredients": r['ingredients'], "steps": r['steps'] } for s,r in scored[:top_k] ]

def simple_suggestion(ingredients: List[str]):
    # very simple template-based suggestion
    title = "Quick " + " & ".join([i.capitalize() for i in ingredients if i])
    steps = [
        "1. Prepare ingredients: wash and chop as needed.",
        "2. Heat a pan with oil. Sauté onions (if present) until soft.",
    ]
    if any('egg' in i for i in ingredients):
        steps.append("3. If eggs are present, beat them and scramble or add to the pan.")
    steps.append("4. Season with salt and pepper. Serve hot.")
    return {"title": title, "ingredients": ingredients, "steps": steps}
