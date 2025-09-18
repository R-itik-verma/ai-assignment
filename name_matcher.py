# name_matcher.py
from rapidfuzz import process, fuzz
import json
from typing import List, Dict

def load_names(path: str = "data/names.json") -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

class NameMatcher:
    def __init__(self, names: List[str]):
        self.names = names

    def match(self, query: str, limit: int = 10) -> Dict:
        results = process.extract(query, self.names, scorer=fuzz.WRatio, limit=limit)
        ranked = [{ "name": r[0], "score": float(r[1]) } for r in results]
        best = ranked[0] if ranked else None
        return {"query": query, "best_match": best, "ranked": ranked}

if __name__ == '__main__':
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Name to match')
    args = parser.parse_args()
    names = load_names()
    nm = NameMatcher(names)
    print(json.dumps(nm.match(args.name, limit=10), indent=2))
