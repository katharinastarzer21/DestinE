import requests
import yaml


def generate_cookbook_gallery_yaml(url='https://api.github.com/users/ProjectPythiaCookbooks/repos', yaml_filepath='cookbook_gallery.yaml'):
    response = requests.get(url).json()

    unwanted_repos=['.github', 'projectpythiacookbooks.github.io', 'cookbook-template', 'test-cookbook', 'cookbook-actions']

    repos_list = []
    for repo in response:
        root = repo['name']
        if root not in unwanted_repos:  
            cookbook_url = f'https://cookbooks.projectpythia.org/{root}/README.html'
            description = repo['description']

            github_url = f'https://github.com/ProjectPythiaCookbooks/{root}'

            #configuration_url = f'{github_url}/blob/main/_config.yml'
            #config = response = requests.get(configuration_url).json()
            #title = config['title']
            title = root.replace('-', ' ')

            thumbnail = f'https://raw.githubusercontent.com/ProjectPythiaCookbooks/{root}/main/thumbnail.png'

            domains = repo['topics']
            packages = []
            tag_dict = {'domains': domains, 'packages': packages}

            repo_dict = {'title': title, 'repo': root, 'url': cookbook_url, 'github_url': github_url, 'description': description, 'thumbnail': thumbnail, 'tags': tag_dict}
            repos_list.append(repo_dict)
            
    with open(yaml_filepath, 'w') as outfile:
        yaml.dump(repos_list, outfile, default_flow_style=False, sort_keys=False)

    return


generate_cookbook_gallery_yaml()