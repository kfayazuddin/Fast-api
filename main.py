import os
from fastapi import FastAPI, Request
import httpx
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

app = FastAPI()

@app.post("/search")
async def search_repos(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    search_query = prompt
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    url = f"https://api.github.com/search/repositories?q={search_query}&sort=stars&order=desc"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=headers)
        data = resp.json()
    repos = [
        {
            "name": item["name"],
            "full_name": item["full_name"],
            "html_url": item["html_url"],
            "description": item["description"],
            "stars": item["stargazers_count"]
        }
        for item in data.get("items", [])
    ]
    return {
        "recommended_repos": repos
    }