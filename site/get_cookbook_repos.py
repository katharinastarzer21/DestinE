import requests
import yaml
import urllib


def generate_cookbook_gallery_yaml(url='https://api.github.com/users/ProjectPythiaCookbooks/repos', yaml_filepath='cookbook_gallery.yaml'):
    response = requests.get(url).json()

    repos_list = []
    for repo in response:
        if "accepted" in repo['topics']:
            root = repo['name']
            description = repo['description']

            github_url = f'https://github.com/ProjectPythiaCookbooks/{root}'
            cookbook_url = f'https://cookbooks.projectpythia.org/{root}/README.html'
            
            config_url = f'https://raw.githubusercontent.com/ProjectPythiaCookbooks/{root}/main/_config.yml'
            config = urllib.request.urlopen(config_url)
            config_dict = yaml.safe_load(config)

            title = config_dict['title']
            authors = config_dict['author']
            thumbnail = config_dict['thumbnail']
            thumbnail_path = f'https://raw.githubusercontent.com/ProjectPythiaCookbooks/{root}/main/{thumbnail}'
            
            tags = config_dict['tags']
            tag_dict = {k: v for k, v in tags.items() if v[0] != None}

            repo_dict = {'title': title, 'repo': root, 'url': cookbook_url, 'github_url': github_url, 'description': description, 'thumbnail': thumbnail_path, 'authors': authors, 'tags': tag_dict}
            repos_list.append(repo_dict)
            
    with open(yaml_filepath, 'w') as outfile:
        yaml.dump(repos_list, outfile, default_flow_style=False, sort_keys=False)

    return


generate_cookbook_gallery_yaml()
