```markdown
# Git Clone Script

This repository contains a Python script that provides functions to clone both private and public GitHub repositories. The script uses the `git` and `requests` libraries to accomplish this.

## Features

- Clone private GitHub repositories using a personal access token.
- Clone public GitHub repositories.
- Customizable local directory and branch.

## Requirements

- Python 3.6+
- `GitPython` library
- `requests` library

## Installation

1. Install Python 3.6 or higher.
2. Install the required libraries:
    ```bash
    pip install gitpython requests
    ```

## Usage

### Cloning a Private Repository

To clone a private repository, use the `gitClonePrivateRepo` function. You need to provide the GitHub repository URL, a personal access token, the local directory where the repository will be cloned, and optionally the branch to clone (default is `main`).

```python
from git import Repo, GitCommandError
import requests

def gitClonePrivateRepo(githuburl, private_token, local_dir, branch='main'):
    repo_url = f"https://{private_token}:x-oauth-basic@{githuburl}"
    try:
        Repo.clone_from(repo_url, f"./repository/{local_dir}", branch=branch)
        response = {
            "error": [],
            "msg": "Repository cloned successfully."
        }
    except GitCommandError as e:
        error_message = e.stderr.strip()
        if "already exists" in error_message:
            response = {
                "error": f"Project already exists: {local_dir}",
                "msg": []
            }, 404
        else:
            response = {
                "error": f"Repository or branch not found: {repo_url}",
                "msg": []
            }, 404
    except Exception as e:
        response = {
            "error": f"Some error occurred: {str(e)}",
            "msg": []
        }, 404
    return response
```

## Example

```python
private_repo_url = "github.com/username/private-repo"
public_repo_url = "github.com/username/public-repo"
private_token = "your_private_token"
local_dir = "local_directory_name"

# Clone a private repository
response = gitClonePrivateRepo(private_repo_url, private_token, local_dir)
print(response)

# Clone a public repository
response = gitClonePublicRepo(public_repo_url, local_dir)
print(response)
```
