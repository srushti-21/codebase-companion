import uuid
from fastapi import APIRouter
from ..models.ingestion import IngestRepoRequest, IngestRepoResponse

router = APIRouter()

@router.post(
    "/ingest-repo",
    response_model=IngestRepoResponse,
    tags=["Ingestion"],
    summary="Ingest a GitHub repository",
    description="Clones a public GitHub repository, processes its files, and prepares it for Q&A.",
)
def ingest_repository(request: IngestRepoRequest):
    """
    This endpoint takes a GitHub URL, processes the repository,
    and returns a session ID for future interactions.
    (Currently, it's just a placeholder).
    """

    session_id = str(uuid.uuid4())

    return IngestRepoResponse(
        message=f"Successfully started ingestion for {request.url}",
        session_id=session_id
    )