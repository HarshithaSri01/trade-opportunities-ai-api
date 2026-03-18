from duckduckgo_search import DDGS
import json

try:
    with DDGS() as ddgs:
        q = "technology sector India news 2026"
        data = list(ddgs.text(q, max_results=2))
        print(f"RESULTS_DEBUG: {json.dumps(data)}")
except Exception as e:
    print(f"RESULTS_ERROR: {str(e)}")
