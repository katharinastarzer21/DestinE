# DEDL Notebook Gallery

::::{tab-set}
:::{tab-item} Introduction
:sync: tab1

<!--
```{card} Card title
:header: The _Header_
:footer: Footer
Card content

![EUMETSAT Logo](img/EUMETSAT-logo.png)
hallo
```
-->


<img style="float:left; width:5%" src="./img/EUMETSAT-icon.png"/>  
<br>

Destination Earth Data Lake Laboratory, which contains additional information for working with DestinE Data Lake services:
- [Harmonised Data Access](https://github.com/destination-earth/DestinE-DataLake-Lab/tree/main/HDA) (Juypter notebooks examples + Python Tools)
- [STACK service](https://github.com/destination-earth/DestinE-DataLake-Lab/tree/main/STACK) (Juypter Notebook examples on how to use DASK for near data processing)
- [HOOK service](https://github.com/destination-earth/DestinE-DataLake-Lab/tree/main/HOOK) (Juypter Notebook examples on how to use HOOK for workflows)


Further information available in DestinE Data Lake documentation: https://destine-data-lake-docs.data.destination-earth.eu/en/latest/index.html


>**Additional ressources:**
>- DestinE Data Portfolio: https://hda.data.destination-earth.eu/ui/catalog
>- DataLake Priority services: https://hda.data.destination-earth.eu/ui/services 
>- HDA SWAGGER UI: https://hda.data.destination-earth.eu/docs/

:::
:::{tab-item} Overview
:sync: tab2

## Notebook Filter

<div style="display: flex; flex-direction: column; gap: 20px; max-width: 800px;">

<!-- HDA Tutorial -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>HDA Tutorial</strong><br>
      This notebook demonstrates the first steps using the Harmonised Data access API.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">Core API</span>
      </div>
      <a href="production/HDA/REST/HDA-REST-full-version.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- HDA Tutorial - quick start -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>HDA Tutorial - Quick start</strong><br>
      This notebook demonstrates how to use the HDA (Harmonized Data Access) API by sending a few HTTP requests to the API, using Python code.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">HTTP requests</span>
      </div>
      <a href="production/HDA/REST/HDA-REST-quick-start.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- HDA Tutorial - Queryables -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>HDA Tutorial - Queryables</strong><br>
      This notebook demonstrates how to use the queryables API to filter C3S and DestinE digital twin collections by leveraging variable terms that dynamically adjust based on user selections.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">C3S</span><span class="tag">Digital twin</span><span class="tag">Authentification</span>
      </div>
      <a href="production/HDA/REST/HDA-REST-Queryables.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>



<!-- HDA PySTAC-Client Introduction -->
<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>PySTAC-Client Introduction</strong><br>
      This notebook shows the basic use of DestinE Data Lake Harmonised Data Access using pystac-client.
      <div style="margin: 6px 0;">
        <span class="tag">HDA</span><span class="tag">Authentication</span><span class="tag">STAC</span>
        <span class="tag">Access Token</span>
      </div>
      <a href="production/HDA/PySTAC/HDA-PyStac-Client.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<!-- Extreme DT Data Availability -->
<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Extreme DT Data Availability</strong><br>
      This notebook shows how to check the data availablility for the Weather-Induced Extremes Digital Twin (Extremes DT) using the ECMWF Aviso package.
      <div style="margin: 6px 0;">
        <span class="tag">HDA</span><span class="tag">pyaviso</span>
        <span class="tag">Digital Twin</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/ExtremeDT-dataAvailability.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

