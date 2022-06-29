import requests

url = 'https://api.github.com/users/ProjectPythiaCookbooks/repos'
response = requests.get(url).json()

unwanted_repos = ['.github', 'projectpythiacookbooks.github.io', 'cookbook-template', 'test-cookbook']
repos = []
for repo in response:
    name = repo['name']
    if name not in unwanted_repos:
        repos.append(name)

print(repos)