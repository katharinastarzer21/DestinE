import requests
import yaml

def _get_cookbook_repo_names(url):
    response = requests.get(url).json()

    unwanted_repos = ['.github', 'projectpythiacookbooks.github.io', 'cookbook-template', 'test-cookbook']
    repos = []
    for repo in response:
        name = repo['name']
        if name not in unwanted_repos:
            repos.append(name)
    
    return repos


#def generate_cookbook_gallery_yaml(repo_url, yaml_filepath='cookbook_gallery.yaml'):
yaml_filepath='cookbook_gallery.yaml'
repo_url = 'https://api.github.com/users/ProjectPythiaCookbooks/repos'
repos = _get_cookbook_repo_names(repo_url)

yaml_dict = {}
for repo in repos:
    title = repo.replace('-', ' ').title()
    cookbook_url = f'https://cookbooks.projectpythia.org/{repo}/README.html'
    github_url = f'https://github.com/ProjectPythiaCookbooks/{repo}'
    description = '' #grab this from github README.md
    names = [] #grab this from github README.md
    thumbnail = f'{github_url}/thumbnail.svg'
    domains = [] #grab this from github README.md
    packages = [] #grab this from github README.md

    authors_dict = {'names':names} #this needs some work
    tags_dict = {'domains': domains, 'packages': packages}

    yaml_dict_item = {'repo':repo, 'url': cookbook_url, 'description': description, 'authors': authors_dict, 'thumbnail': thumbnail, 'tags': tags_dict}
    yaml_dict[title] = yaml_dict_item


with open(yaml_filepath, 'w') as outfile:
    yaml.dump(yaml_dict, outfile, default_flow_style=False)


#url = 'https://api.github.com/users/ProjectPythiaCookbooks/repos'
#generate_cookbook_gallery_yaml(url)
