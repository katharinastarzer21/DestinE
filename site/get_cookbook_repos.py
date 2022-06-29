import requests

url = 'https://api.github.com/users/ProjectPythiaCookbooks/repos'

def _get_cookbook_repo_names(url):
    response = requests.get(url).json()

    unwanted_repos = ['.github', 'projectpythiacookbooks.github.io', 'cookbook-template', 'test-cookbook']
    repos = []
    for repo in response:
        name = repo['name']
        if name not in unwanted_repos:
            repos.append(name)
    
    return repos


def _generate_cookbook_gallery_yaml(repos, filepath='../cookbook_gallery.yaml'):
    yaml_dict = []
    for repo in repos:
        title = deslug(repo).capitalize() #need to create a deslug fx
        cookbook_url = f'https://cookbooks.projectpythia.org/{repo}/README.html'
        github_url = f'https://github.com/ProjectPythiaCookbooks/{repo}'
        description = ''
        names = []
        thumbnail = f'{github_url}/thumbnail.svg'
        domains = []
        packages = []

        authors_dict = {'names':names} #this needs some work
        tags_dict = {'domains': domains, 'packages': packages}

        yaml_dict_item = {'title': title, 'repo':repo, 'url': cookbook_url, 'description': description, 'authors': authors_dict, 'thumbnail': thumbnail, 'tags': tags_dict}
        yaml_dict.append(yaml_dict_item)

        yaml_dict.to_yaml(filepath)
        return



