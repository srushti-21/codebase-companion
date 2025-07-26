# app/models/qa.py

from pydantic import BaseModel

class AskRequest(BaseModel):
    """Request model for asking a question."""
    question: str
    session_id: str
    
class AskResponse(BaseModel):
    """Response model for an answer"""
    answer: str
    relevant_sources: list[str] # List of file paths used as context
