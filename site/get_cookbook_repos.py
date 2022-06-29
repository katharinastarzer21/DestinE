import requests
import yaml


def generate_cookbook_gallery_yaml(url='https://api.github.com/users/ProjectPythiaCookbooks/repos', yaml_filepath='cookbook_gallery.yaml'):
    response = requests.get(url).json()

    unwanted_repos=['.github', 'projectpythiacookbooks.github.io', 'cookbook-template', 'test-cookbook']

    repos_list = []
    for repo in response:
        root = repo['name']
        if root not in unwanted_repos:  
            title = root.replace('-', ' ').title()
            cookbook_url = f'https://cookbooks.projectpythia.org/{root}/README.html'
            description = repo['description']

            github_url = f'https://github.com/ProjectPythiaCookbooks/{root}'
            thumbnail = f'{github_url}/thumbnail.svg'

            #author_names = [] #grab this from github README.md (add - before each one)
        
            #domains = [] #grab this from github README.md (add - before each one)
            #packages = [] #grab this from github README.md (add - before each one)

            #authors_dict = {'names':author_names} #this needs some work
            #tags_dict = {'domains': domains, 'packages': packages}

            repo_dict = {'title': title, 'repo': root, 'url': cookbook_url, 'github_url': github_url, 'description': description, 'thumbnail': thumbnail}# 'authors': authors_dict, , 'tags': tags_dict}
            repos_list.append(repo_dict)
            
    with open(yaml_filepath, 'w') as outfile:
        yaml.dump(repos_list, outfile, default_flow_style=False, sort_keys=False)

    return


generate_cookbook_gallery_yaml()