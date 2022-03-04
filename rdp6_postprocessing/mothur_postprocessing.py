import pandas as pd
import argparse
import os
"""
We will normalize abundances in order for each column (subject) to sum up to 1. Additional string preprocessing is done 
in order for the final file to look like the original files from Franzosa et al.
"""

# save strings for file name
body_site = "feces"
classifier = "rdp6"
project = "moms-pi"
folder_name= "./unified_files_%s_%s"%(body_site,classifier)
output_folder = "./final_results_%s_%s_%s"%(body_site,project,classifier)

# create folder for unified files
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i in range(1, 12):
    input_file = "visit%s.final.summary" % (i)
    filename = "/intermediate-otus-%s-%s.pcl" % (body_site, i)
    summary = pd.read_csv(input_file, sep='\t')

    # format taxonomy
    summary['taxonomy'] = list(map(lambda x: x.replace('"', "").replace(";", "|")[5:len(x) - 3], summary['taxonomy']))
    taxonomy = summary['taxonomy']

    # compute relative abundances for each sample column
    summary = summary.drop(columns=["taxonomy"])
    summary = summary.astype(float, errors="ignore")
    total = summary.iloc[0]  # save total counts of abundances

    # save to final data frame
    final = pd.concat([taxonomy, summary.divide(total, axis="columns").round(9)], axis=1)

    # remove first row and first column
    final = final.iloc[1:, :]  # remove first row
    final = final.drop(columns=["total"])
    final.rename(columns={'taxonomy': 'subject_id'}, inplace=True)  # rename taxonomy to subject_id, row name
    print("%s has %s subjects and %s attributes" % (input_file, str(final.shape[0]), str(final.shape[1]-1)))

    final.to_csv(output_folder + filename, sep='\t', index=False)
