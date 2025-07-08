# GitHub MCP Server

This is a FastAPI-based MCP server that queries GitHub repositories related to a user-provided topic.

## Setup
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Add your GitHub personal access token to the `.env` file:
   ```
   GITHUB_TOKEN=your_personal_access_token_here
   ```
3. Run the server:
   ```sh
   uvicorn main:app --reload
   ```

## Usage
- Query endpoint: `http://localhost:8000/search`
- Payload: 
### 📦 Payload
```json
{
  "prompt": "Data-science"
}


## Notes
- Using a GitHub token increases your API rate limit.
