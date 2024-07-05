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
