# app/main.py
from fastapi import FastAPI
from .routers import ingestion, qa

# Create the main FastAPI application instance
app = FastAPI(
    title="Codebase Companion API",
    description="An API to ingest and chat with any GitHub repository.",
    version="0.1.0",
)

# A simple "hello world" endpoint at the root URL
@app.get("/", tags=["Health Check"])
def read_root():
    """A simple health check endpoint to confirm the server is running."""
    return {"status": "ok", "message": "Welcome to the Codebase Companion API!"}

app.include_router(ingestion.router, prefix="/api")
app.include_router(qa.router, prefix="/api")  