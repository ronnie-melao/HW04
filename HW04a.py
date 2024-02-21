import requests
import modules

def getUserRepoCommits(username):
    repos_url = f"https://api.github.com/users/{username}/repos"

    user_data = requests.get(repos_url).json()

    repo_info = []

    for repo in user_data:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
        commits_data = requests.get(commits_url).json()
        num_commits = len(commits_data)
        repo_info.append(f"Repo: {repo_name} Number of commits: {num_commits}")

    return '\n'.join(repo_info)

print(getUserRepoCommits('ronnie-melao'))