from pydantic import BaseModel, HttpUrl

class IngestRepoRequest(BaseModel):
    """Request model for ingesting a repository."""
    url: HttpUrl  

class IngestRepoResponse(BaseModel):
    """Response model after successfully ingesting a repository."""
    message: str
    session_id: str