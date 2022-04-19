# franzosa_scripts

## Introduction
We created several scripts for analyzing, processing and unifying data samples gathered from [Human Microbiome Project Data Portal](https://portal.hmpdacc.org/) (HMP Data Portal). It provides data samples from 18 studies from up to 48 different body sites. The collection provides a total of over 31.000 samples.

Goal of the scripts is to create files in order to have more data samples which can be used for experiments regarding data privacy, especially personal microbiome identification.

Based on the paper from [Franzosa et al.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4460507/), we tried to recreate a pipeline that follows the same preprocessing steps using mothur to compute the relative abundance of operational taxonomic units (OTU). We used 16S rRNA gene data gathered from the portal and computed the abundances for each visit and subject. 

The final files have the same naming convention given by Franzosa et al. (see [here](http://huttenhower.sph.harvard.edu/idability#preprocessed-metagenomics-datasets))

```
otus-anterior_nares-visit1.pcl
otus-anterior_nares-visit2.pcl
```

## Folder Structure
Each folder contains scripts for a certain purpose.

`/data_managment`: contains `create_files.py` which creates a single `.tsv` file for metadata and download files per visit.

`/postprocessing`: Contains a mothur python script based on the mothur python library, that computes the abundances of the OTUs.
It needs to be run in a folder with extracted .fastq files that contain both RNA strings (R1,R2) and have a similar format
to ID*.R1.fastq/ID*.R2.fastq. Also, the script must be run in a folder contain the taxonomy files used for classification
trainset6_032010.fa/trainset6_032010.tax (rdp6) and trainset18_062020.rdp.fasta/trainset18_062020.rdp.tax (rdp18).
rdp6 is the version initially used in the Franzosa et al. paper and rdp18 is the newest release. More information
can be found [here](https://mothur.org/wiki/rdp_reference_files/).

`/postprocessing`: contains `reformat_taxonomy.py` which computes the relative abundances per sample and processes the taxonomy 
names of the mothur output files to fit the Franzosa et al. files. `unify_files.py` processes 