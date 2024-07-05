from git import Repo, GitCommandError
import requests


def gitClonePrivateRepo(githuburl,private_token,local_dir,branch='main'):
        repo_url= f"https://{private_token}:x-oauth-basic@{githuburl}"
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
                "error": f"Project already exits: {local_dir}",
                "msg": []
                },404
            else:
                response = {
                "error": f"Repository or branch not found: {repo_url}",
                "msg": []
                },404
        except Exception as e:
             response = {
            "error": f"some error occured: {str(e)}",
            "msg": []
            },404
        return response

def gitClonePublicRepo(githuburl,local_dir,branch='main'):
        print(githuburl)
        repo_url = f"https://{githuburl}"
        try:
            response = requests.get(repo_url)
            print(response)

            if response.status_code == 200:
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
                        "error": f"Project already exits: {local_dir}",
                        "msg": []
                        },404
                    else:
                        response = {
                        "error": f"Repository or branch not found: {repo_url}",
                        "msg": []
                        },404
            else:
                response = {
                "error": f"Repository or branch not found: {repo_url}",
                "msg": []
                },404
        except requests.exceptions.MissingSchema as e:
            response = {
            "error": str(e),
            "msg": ""
            },404
        except Exception as e:
            response = {
            "error": str(e),
            "msg": []
            },404
        return response
