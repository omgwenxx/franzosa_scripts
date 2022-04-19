import csv
import pandas as pd
import numpy as np
import os
import argparse

# create parser
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument("download_info")
parser.add_argument("metadata")

# parse the arguments
args = parser.parse_args()

download_info = pd.read_csv(args.download_info, sep='\t')
metadata = pd.read_csv(args.metadata, sep='\t')

mergedRes = pd.merge(download_info, metadata, validate ="one_to_one")
print("Body sites included in the dataset:%s"%(str(mergedRes["sample_body_site"].unique())))

def merge_files(name="total_info.csv"):
    """
    This methods merges the download .tsv file with the metadata by sample id.
    Saves it into a file called total_info.csv if not named otherwise
    """
    total = pd.merge(download_info, metadata, validate ="one_to_one") # merge both dataframes
    # puts subject id as first column
    subject_ids = total['subject_id']
    total = total.drop(columns=['subject_id'])
    total.insert(loc=0, column='subject_id', value=subject_ids)
    total.to_csv(name,index=False)
    return total
total = merge_files()

def export_visit(body_site, total):
    """
    Exports all visits separatly for given body site. The final .tsv files are saved in folders
    with names <body_site>_files and <body_site>_metadata_files
    :param body_site: string with body site to extract
    :param total: dataframe with samples
    :return:
    """
    filedir = body_site + "_files"
    metadatadir = body_site + "metadata_files"

    if not filedir:
        os.makedirs(filedir)
        print("Created folder : ", filedir)

    if not metadatadir:
        os.makedirs(metadatadir)
        print("Created folder : ", metadatadir)

    visits = total['visit_number'].unique()
    for i in visits:
        download_file_name = ("visit%s_%s_momspi_download.tsv" % (i,body_site)).replace(" ","_")
        metadata_file_name = ("visit%s_%s_momspi_metadata.tsv" % (i,body_site)).replace(" ","_")
        # print(download_file_name)
        filtered = total[(total['visit_number'] == i) & (total['sample_body_site'] == body_site)]
        download = filtered[["file_id","md5","size","urls","sample_id","subject_id"]]
        # print(filtered[["file_id","md5","size","urls","sample_id"]])
        download.to_csv(download_file_name, sep = '\t', index=False)
        filtered.to_csv(metadata_file_name, sep = '\t', index=False)

def export_body_site(total, numvisit = 12):
    """
    Creates for a total number of visits, a download and metadata file for each body site per visits. The files
    are then saved into folder of the format <body_site>_files and <body_site>_metadata_files
    :param total: dataframe with samples
    :param numvisit: number of visits to extract
    :return:
    """
    body_sites = total['sample_body_site'].unique()
    study_names = total['study_full_name'].unique()
    for body_site in body_sites:
        filedir = body_site + "_files"
        metadatadir = body_site + "_metadata_files"

        if not os.path.isdir(filedir):
            os.makedirs(filedir)
            print("Created folder : ", filedir)

        if not os.path.isdir(metadatadir):
            os.makedirs(metadatadir)
            print("Created folder : ", metadatadir)

    for i in range(1,numvisit):
        for body_site in body_sites:
            for study in study_names:
                filedir = body_site + "_files"
                metadatadir = body_site + "_metadata_files"

                download_file_name = ("visit%s_%s_%s_download.tsv" % (i,body_site,study)).replace(" ","_")
                metadata_file_name = ("visit%s_%s_%s_metadata.tsv" % (i,body_site,study)).replace(" ","_")

                # print(download_file_name)
                filtered = total[(total['visit_number'] == i) & (total['sample_body_site'] == body_site)]
                download = filtered[["file_id","md5","size","urls","sample_id","subject_id"]]

                # print(filtered[["file_id","md5","size","urls","sample_id"]])
                download.to_csv(filedir + "/" + download_file_name, sep = '\t', index=False)
                filtered.to_csv(metadatadir + "/" + metadata_file_name, sep = '\t', index=False)

export_body_site(total)
