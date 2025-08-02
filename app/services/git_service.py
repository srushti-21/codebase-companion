# app/services/git_service.py
import git
import tempfile
import logging

# Set up a logger for this module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clone_repo(repo_url: str) -> str:
    """
    Clones a public GitHub repository to a temporary local directory.

    Args:
        repo_url (str): The HTTPS URL of the GitHub repository.

    Returns:
        str: The local path to the cloned repository.

    Raises:
        Exception: If the cloning process fails.
    """
    try:
        # Create a temporary directory to clone the repo into
        temp_dir = tempfile.mkdtemp()
        logger.info(f"Cloning {repo_url} into temporary directory: {temp_dir}")

        # Use GitPython to clone the repository
        git.Repo.clone_from(repo_url, temp_dir)

        logger.info(f"Successfully cloned repository.")
        return temp_dir

    except git.exc.GitCommandError as e:
        logger.error(f"Failed to clone repository: {e}")
        # In a real app, you might want to clean up the temp_dir here
        raise Exception(f"Could not clone repository. Is the URL correct and the repository public?")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise Exception("An unexpected error occurred during the cloning process.")