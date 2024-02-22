import requests
import modules

def getUserRepoCommits(username):
    # get url using username input
    repos_url = f"https://api.github.com/users/{username}/repos"

    # use API to transform repo data in JSON file
    user_data = requests.get(repos_url).json()
    print(user_data)
    # empty array to store repo names and number of commits
    repo_info = []

    # finds repo names and number of commits, then adds to empty array above
    for repo in user_data:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
        commits_data = requests.get(commits_url).json()
        num_commits = len(commits_data)
        repo_info.append(f"Repo: {repo_name} Number of commits: {num_commits}")

    # joins all strings in array and makes new line after each one
    return '\n'.join(repo_info)

print(getUserRepoCommits('ronnie-melao'))