import yaml
from gallery_generator import build_from_repos, generate_menu, generate_repo_dicts


def main(app):

    with open('cookbook_gallery.yaml') as fid:
        all_items = yaml.safe_load(fid)[0]['repos']

    title = 'Cookbooks Gallery'
    subtext = 'Pythia Cookbooks provide example workflows on more advanced and domain-specific problems developed by the Pythia community. Cookbooks build on top of skills you learn in Pythia Foundations.'
    
    repo_dicts = generate_repo_dicts(all_items)
    menu_html = generate_menu(repo_dicts)
    build_from_repos(repo_dicts, 'index', title=title, subtext=subtext, menu_html=menu_html)


def setup(app):
    app.connect('builder-inited', main)
