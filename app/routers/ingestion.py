import uuid
from fastapi import APIRouter, HTTPException
from ..models.ingestion import IngestRepoRequest, IngestRepoResponse
from ..services import git_service # <-- IMPORT THE NEW SERVICE

# Create a new router object
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
    This endpoint takes a GitHub URL, clones the repository,
    and returns a session ID for future interactions.
    """
    try:
        # 1. Call the git_service to clone the repo
        repo_path = git_service.clone_repo(str(request.url)) # Use str() to convert from Pydantic's HttpUrl

        # 2. In the future, we will pass this 'repo_path' to other services
        #    for chunking, embedding, etc. For now, we just log it.
        print(f"Repository cloned to: {repo_path}")

        # 3. Generate a session ID
        session_id = str(uuid.uuid4())

        # NOTE: We need a plan to clean up the temporary directory later!
        # This is a task for a future day.

        return IngestRepoResponse(
            message=f"Successfully cloned repository from {request.url}. Ready for processing.",
            session_id=session_id
        )

    except Exception as e:
        # If the service raised an exception, catch it and return a proper HTTP error
        raise HTTPException(status_code=400, detail=str(e))