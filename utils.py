import shutil
from git import Repo


def clone_repo(repo_url):

    folder = "temp_repo"

    shutil.rmtree(folder, ignore_errors=True)

    Repo.clone_from(repo_url, folder)

    return folder