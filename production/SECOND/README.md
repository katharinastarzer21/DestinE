# Notebook Template

This repository serves as a template for submitting notebooks to the [DEDL Notebook Gallery](https://destination-earth.github.io/DestinE-DataLake-Gallery).

## How to use

1. Clone this repository to your GitHub account:

   ```bash
   git clone https://github.com/destination-earth/DestinE-DataLake-NotebookTemplate.git
   ```

   or simply use the **"Use this template"** button on GitHub.
2. Add your Jupyter Notebooks to the `notebooks/` folder.
3. Follow the example provided in `notebooks/template.ipynb`.
   Pay special attention to the first Markdown cell, where metadata such as title, tags, thumbnail, etc. must be included using **YAML front matter**. Please note that every notebook has to include this fist markdown cell in the very beginning!
4. Add a thumbnail image for each notebook, place it in the `img/` folder, and reference it in the notebook’s metadata.
5. Enable GitHub Pages
   - Go to Settings → Pages.
   - Under Build and deployment, set Source to GitHub Actions.
6. Enable Required GitHub Actions Permissions
   - Go to Settings → Actions → General.
   - Scroll down to the Workflow permissions section.
   - Select Read and write permissions.
   - Click Save if you made any changes. 
7. Submit the link to your repository via the [Gallery submission issue form](https://github.com/destination-earth/DestinE-DataLake-Gallery/issues).

### Attention!

Once your repository is successfully reviewed and included in the DestinE Notebook Gallery, **any changes** you push to your repository will **automatically** be reflected on the website.
Please make sure your repository remains clean, well-maintained and up to date.
