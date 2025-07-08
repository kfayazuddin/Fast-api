# GitHub Fast API

A FastAPI-based app that lets users search public GitHub repositories by topic (e.g., Python, Java, ML). It fetches real-time data from the GitHub API and displays repository info like name, description, stars, language, and GitHub link.

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
   
## FastAPI Endpoint Preview
![Screenshot 2025-07-08 134854](https://github.com/user-attachments/assets/d2c51cd9-369c-4b10-bb27-d1ae86f8d2d7)

## Video

## Usage
- Query endpoint(Tried running locally): `http://localhost:8000/search`
- Payload: 
### 📦 Payload
```json
{
  "prompt": "Data-science"
}


## Notes
- Using a GitHub token increases your API rate limit.
