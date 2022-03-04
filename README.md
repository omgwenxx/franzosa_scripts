# franzosa_scripts

## Introduction
We created several script for analyzing, processing and unifying data samples gathered from [Human Microbiome Project Data Portal](https://portal.hmpdacc.org/) (HMP Data Portal). It provides data samples from 18 studies from up to 48 different body sites. The collection provides a total of over 31.000 samples.

Goal of the scripts is to create files in order to have more data samples which can be used for experiments regarding data privacy, especially personal microbiome identification.

Based on the paper from [Franzosa et al.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4460507/), we tried to recreate a pipeline that follows the same preprocessing steps using mothur to compute the relative abundance of operational taxonomic units (OTU). We used 16S rRNA gene data gathered from the portal and computed the abundances for each visit and subject. 

The final files have the same naming convention given by Franzosa et al. (see [here](http://huttenhower.sph.harvard.edu/idability#preprocessed-metagenomics-datasets))

```
otus-anterior_nares-visit1.pcl
otus-anterior_nares-visit2.pcl
```

## Folder Structure
Each folder contains scripts for a certain purpose
<ul>
  <li>``</li>
  <li>``</li>
  <li>``</li>
  <li>``</li>
</ul>