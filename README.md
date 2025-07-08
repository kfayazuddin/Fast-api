# Fast API importance :

🚀 1. High Performance
Built on Starlette (for web handling) and Pydantic (for data validation).
Uses asynchronous programming (async/await), making it fast and suitable for high-performance APIs.
Comparable in speed to Node.js and Go for I/O-bound operations.

🧠 2. Automatic Documentation
Swagger UI and ReDoc are auto-generated from your code.
Provides interactive API documentation with no extra effort.

✅ 3. Data Validation and Serialization
Powered by Pydantic for parsing and validating request/response data using Python type hints.
Catches errors early and improves code reliability.

✍️ 4. Pythonic and Type-Hint Friendly
Designed to work naturally with Python 3.6+ type hints.
Type hints improve editor support (e.g., autocompletion, linting, and refactoring).

📦 5. Easy to Use
Simple and minimal syntax.
Clear and concise structure even for complex applications.
Great for beginners and experts alike.

🛠️ 6. Dependency Injection
Built-in dependency injection system makes it easy to manage reusable components, e.g., DB connections, auth logic.

🔐 7. Built-in Security
Tools for OAuth2, JWT, and basic HTTP authentication.
Easy to integrate with external security systems.

⚙️ 8. Production-Ready
Used in production by companies like Uber, Microsoft, and Netflix.
Supports tools like Gunicorn, Uvicorn, and Docker out-of-the-box.

👥 9. Asynchronous Support
First-class support for async def, making it ideal for applications with concurrent API calls (e.g., microservices).

🔄 10. OpenAPI Support
Built-in support for OpenAPI and JSON Schema standards.
Enables integration with other tools and services easily.
Let me know if you want a comparison between FastAPI and another framework (like Flask, Express.js, etc.).

# Flow of Fastapi on client request :
                          ┌────────────────────────────┐
                          │        Client (Browser)    │
                          └─────────────┬──────────────┘
                                        │ HTTP Request
                                        ▼
                           ┌──────────────────────────┐
                           │        Uvicorn           │
                           │ (ASGI web server)        │
                           └─────────────┬────────────┘
                                         │ ASGI interface
                                         ▼
                          ┌───────────────────────────┐
                          │         FastAPI           │
                          │  (built on Starlette)     │
                          └─────────────┬─────────────┘
                                        │
                                        ▼
                           ┌─────────────────────────┐
                           │       Starlette         │
                           │ (ASGI toolkit/routing)  │
                           └────────────┬────────────┘
                                        │
                                        ▼
                           ┌─────────────────────────┐
                           │     Python Code (Your   │
                           │    endpoints/business   │
                           │         logic)          │
                           └─────────────────────────┘


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
https://drive.google.com/file/d/1sH7Ajatygf4Z5y9AjtDZ3wpFidS4Rfia/view?usp=drive_link

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
