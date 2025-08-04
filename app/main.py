from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from dotenv import load_dotenv

# Load environment variables from a .env file for local development
# In a deployed Cloud Run environment, this line does nothing.
load_dotenv()

app = FastAPI()

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "..", "templates"))

# --- Configuration ---
# This is the key to making the app work in any environment.
# In Cloud Run, you will set the BACKEND_API_URL environment variable during deployment.
# For local testing, it falls back to the value in your .env file.
BACKEND_URL = os.getenv("BACKEND_API_URL")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    This endpoint serves the main index.html file and injects the
    backend URL into the template.
    """
    if not BACKEND_URL:
        # This provides a clear error if the environment variable is not set.
        return HTMLResponse(content="<h1>Error: BACKEND_API_URL environment variable is not set.</h1>", status_code=500)

    print(f"Serving frontend and connecting to backend at: {BACKEND_URL}")
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,
            "backend_url": BACKEND_URL
        }
    )
