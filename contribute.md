
## Contribute to the Gallery

If you’ve developed a Jupyter notebook that works with the **DestinE Data Lake** services and would like to share it with others, follow the steps below to add your repository to the Gallery:

### Step-by-Step: Upload Your Repository

1. **Use the template repository**
   - Clone the official template repository to your own GitHub account:
     ```bash
     git clone https://github.com/your-username/your-new-repo.git
     ```
   - Or use the 'Use this repository" button.

2. **Add your content**
   - Add your Jupyter notebooks to the `notebooks/` folder.
   - Follow the format from the example `notebooks/template.ipynb`, especially the **first Markdown cell**, which must contain a YAML frontmatter block:
     ````markdown
     ---
     title: "Your Notebook Title"
     subtitle: "Brief description of what this notebook does."
     authors: ["Your Name"]
     tags: ["HDA", "Dask", "Workflow"]
     thumbnail : /img/example.png
     license: MIT
     copyright: "© 2024 EUMETSAT"
     ---
     ````
   - Add any relevant images and the thumbnail for the gallery to the `img/` folder.

3. **Submit your repository**
   - Go to the [DestinE GitHub repository](https://github.com/destination-earth/DestinE).
   - Open a [new issue](https://github.com/destination-earth/DestinE/issues/new?template=cookbook_submission.md) using the `Add Cookbook Repository` template.
   - Fill in the template with:
     - Repository URL
     - Short Title in capital letters for folder structure

4. **Review process**
   - The DestinE team will review your submission.
   - If accepted, your repository will be integrated into the official gallery and published on the site automatically.

### Best Practices
- Use clear titles and headings in your notebooks.
- Tag your notebooks meaningfully (e.g. `sentinel-1`, `openEO`, `access-token`, etc.).
- Keep dependencies minimal and well-documented.
- Test your code to ensure it runs from top to bottom.