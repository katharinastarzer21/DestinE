
# Cookbooks Gallery


Pythia Cookbooks provide example workflows on more advanced and domain-specific problems developed by the Pythia community. Cookbooks build on top of skills you learn in Pythia Foundations.

<div class="d-sm-flex mt-3 mb-4">
<div class="d-flex gallery-menu">
</div>
<div class="ml-auto d-flex">
<div><button class="btn btn-link btn-sm mx-1" onclick="clearCbs()">Clear all filters</button></div>

<div class="dropdown">

<button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="domainsDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
Domains
</button>
<ul class="dropdown-menu" aria-labelledby="domainsDropdown">
<li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=climate onchange="change();">&nbsp;Climate</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=intake-esm onchange="change();">&nbsp;Intake-esm</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=oceanography onchange="change();">&nbsp;Oceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=packages onchange="change();">&nbsp;Packages</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=py-art onchange="change();">&nbsp;Py-art</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=radar onchange="change();">&nbsp;Radar</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=visualization onchange="change();">&nbsp;Visualization</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=xgcm onchange="change();">&nbsp;Xgcm</label></li>
</ul>
</div>


<div class="dropdown">

<button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="packagesDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
Packages
</button>
<ul class="dropdown-menu" aria-labelledby="packagesDropdown">

</ul>
</div>

</div>
</div>
<script>$(document).on("click",function(){$(".collapse").collapse("hide");}); </script>


````{panels}
:column: col-12
:card: +mb-4 w-100
:header: d-none
:body: p-3 m-0
:footer: p-1

---
:column: + tagged-card climate intake-esm

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythiaCookbooks/cmip6-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://cookbooks.projectpythia.org/cmip6-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">cmip6 cookbook</h4></a>
<p class="my-2">Examples of analysis of Google Cloud CMIP6 data using Pangeo tools</p>
</div>
</div>


+++
<div class="tagsandbadges">
<span class="badge bg-primary mybadges">climate</span>
<span class="badge bg-primary mybadges">intake-esm</span>
<div
    <a class="reference external" href="https://github.com/ProjectPythiaCookbooks/cmip6-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythiaCookbooks/cmip6-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
    <a class="reference external" href="https://binder-staging.2i2c.cloud/v2/gh/ProjectPythiaTutorials/cmip6-cookbook.git/main"><img alt="Binder" src="https://binder-staging.2i2c.cloud/badge_logo.svg" /></a>
    </div>
</div>


---
:column: + tagged-card visualization

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythiaCookbooks/HRRR-AWS-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://cookbooks.projectpythia.org/HRRR-AWS-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">HRRR AWS cookbook</h4></a>
<p class="my-2">A cookbook for working with AWS-served HRRR model output data</p>
</div>
</div>


+++
<div class="tagsandbadges">
<span class="badge bg-primary mybadges">visualization</span>
<div
    <a class="reference external" href="https://github.com/ProjectPythiaCookbooks/HRRR-AWS-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythiaCookbooks/HRRR-AWS-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
    <a class="reference external" href="https://binder-staging.2i2c.cloud/v2/gh/ProjectPythiaTutorials/HRRR-AWS-cookbook.git/main"><img alt="Binder" src="https://binder-staging.2i2c.cloud/badge_logo.svg" /></a>
    </div>
</div>


---
:column: + tagged-card visualization

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythiaCookbooks/mpl-colorbar-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://cookbooks.projectpythia.org/mpl-colorbar-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">mpl colorbar cookbook</h4></a>
<p class="my-2">This Project Pythia Cookbook covers colorbars.</p>
</div>
</div>


+++
<div class="tagsandbadges">
<span class="badge bg-primary mybadges">visualization</span>
<div
    <a class="reference external" href="https://github.com/ProjectPythiaCookbooks/mpl-colorbar-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythiaCookbooks/mpl-colorbar-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
    <a class="reference external" href="https://binder-staging.2i2c.cloud/v2/gh/ProjectPythiaTutorials/mpl-colorbar-cookbook.git/main"><img alt="Binder" src="https://binder-staging.2i2c.cloud/badge_logo.svg" /></a>
    </div>
</div>


---
:column: + tagged-card packages

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythiaCookbooks/packaging-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://cookbooks.projectpythia.org/packaging-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">packaging cookbook</h4></a>
<p class="my-2">This Project Pythia Cookbook covers Python packaging.</p>
</div>
</div>


+++
<div class="tagsandbadges">
<span class="badge bg-primary mybadges">packages</span>
<div
    <a class="reference external" href="https://github.com/ProjectPythiaCookbooks/packaging-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythiaCookbooks/packaging-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
    <a class="reference external" href="https://binder-staging.2i2c.cloud/v2/gh/ProjectPythiaTutorials/packaging-cookbook.git/main"><img alt="Binder" src="https://binder-staging.2i2c.cloud/badge_logo.svg" /></a>
    </div>
</div>


---
:column: + tagged-card oceanography

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythiaCookbooks/physical-oceanography-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://cookbooks.projectpythia.org/physical-oceanography-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">physical oceanography cookbook</h4></a>
<p class="my-2">Examples of how to use Xarray, Dask, and Holoviews to load, process, and visualize cloud-based ocean data. Datasets include satellite observations (gridded sea-surface height) and ocean model output (POP, MOM6).</p>
</div>
</div>


+++
<div class="tagsandbadges">
<span class="badge bg-primary mybadges">oceanography</span>
<div
    <a class="reference external" href="https://github.com/ProjectPythiaCookbooks/physical-oceanography-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythiaCookbooks/physical-oceanography-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
    <a class="reference external" href="https://binder-staging.2i2c.cloud/v2/gh/ProjectPythiaTutorials/physical-oceanography-cookbook.git/main"><img alt="Binder" src="https://binder-staging.2i2c.cloud/badge_logo.svg" /></a>
    </div>
</div>


---
:column: + tagged-card py-art radar

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythiaCookbooks/radar-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://cookbooks.projectpythia.org/radar-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">radar cookbook</h4></a>
<p class="my-2">A cookbook meant to work with various weather radar data</p>
</div>
</div>


+++
<div class="tagsandbadges">
<span class="badge bg-primary mybadges">py-art</span>
<span class="badge bg-primary mybadges">radar</span>
<div
    <a class="reference external" href="https://github.com/ProjectPythiaCookbooks/radar-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythiaCookbooks/radar-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
    <a class="reference external" href="https://binder-staging.2i2c.cloud/v2/gh/ProjectPythiaTutorials/radar-cookbook.git/main"><img alt="Binder" src="https://binder-staging.2i2c.cloud/badge_logo.svg" /></a>
    </div>
</div>


---
:column: + tagged-card xgcm

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythiaCookbooks/xgcm-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://cookbooks.projectpythia.org/xgcm-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">xgcm cookbook</h4></a>
<p class="my-2">The cookbook for xgcm examples and use cases that were originally housed by Pangeo Gallery.</p>
</div>
</div>


+++
<div class="tagsandbadges">
<span class="badge bg-primary mybadges">xgcm</span>
<div
    <a class="reference external" href="https://github.com/ProjectPythiaCookbooks/xgcm-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythiaCookbooks/xgcm-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
    <a class="reference external" href="https://binder-staging.2i2c.cloud/v2/gh/ProjectPythiaTutorials/xgcm-cookbook.git/main"><img alt="Binder" src="https://binder-staging.2i2c.cloud/badge_logo.svg" /></a>
    </div>
</div>


````

<div class="modal-backdrop"></div>
<script src="/_static/custom.js"></script>
