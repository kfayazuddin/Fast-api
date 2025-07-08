import os
from fastapi import FastAPI, Request
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch token securely
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
print("Token from .env is:", GITHUB_TOKEN if GITHUB_TOKEN else "NOT FOUND")
app = FastAPI()

@app.post("/search")
async def search_repos(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return {"error": "Prompt is required."}

    headers = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    url = f"https://api.github.com/search/repositories?q={prompt}&sort=stars&order=desc"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": f"GitHub API returned status code {response.status_code}", "details": response.text}

    data = response.json()

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

    return {"recommended_repos": repos}
