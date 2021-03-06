# AUTOGENERATED! DO NOT EDIT! File to edit: 01_GTEx.ipynb (unless otherwise specified).

__all__ = ['GTEX_URL', 'GTEXV8_TPM', 'GTEXV8_TPM_MED', 'GTEX_PHENO_DS', 'GTEX_PHENO_DD', 'GTEX_SAMPLE_DS',
           'GTEX_SAMPLE_DD', 'script_dir', 'cache_dir', 'GTEX_GENES_ENSG', 'GTEX_GENES_SYMBOL',
           'GTEX_GENES_SYMBOL_DUPLICATES']

# Cell
# default_exp gtex
# export

from logzero import logger
import pathlib
import pickle
import os
from tqdm import tqdm
import requests


# GTEx data from https://gtexportal.org/home/datasets
# Gene transcripts per million data

GTEX_URL =  "https://storage.googleapis.com/gtex_analysis_v8"

GTEXV8_TPM = os.path.join(GTEX_URL, "rna_seq_data", "GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct.gz")
GTEXV8_TPM_MED = os.path.join(GTEX_URL, "rna_seq_data", "GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct.gz")
GTEX_PHENO_DS = os.path.join(GTEX_URL, "annotations", "GTEx_Analysis_v8_Annotations_SubjectPhenotypesDS.txt")
GTEX_PHENO_DD = os.path.join(GTEX_URL, "annotations", "GTEx_Analysis_v8_Annotations_SubjectPhenotypesDD.xlsx")
GTEX_SAMPLE_DS = os.path.join(GTEX_URL, "annotations", "GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt")
GTEX_SAMPLE_DD = os.path.join(GTEX_URL, "annotations", "GTEx_Analysis_v8_Annotations_SampleAttributesDD.xlsx")

script_dir = pathlib.Path().resolve()
cache_dir = os.path.join(script_dir, "data")

if os.path.exists(cache_dir):
    logger.info(f"Found {cache_dir}")
else:
    os.mkdir(cache_dir)

for url in [GTEXV8_TPM_MED, GTEXV8_TPM, GTEX_PHENO_DS, GTEX_PHENO_DD, GTEX_SAMPLE_DS, GTEX_SAMPLE_DD]:
    dest = os.path.join(cache_dir, os.path.basename(url))
    if os.path.exists(dest):
        logger.info(f"found existing: {dest}")
    else:
        logger.info(f"Downloading {dest}")
        # Open a handle onto the GTEx expression data
        response = requests.get(url, stream=True)

        with open(dest, "wb") as fh:
            for data in tqdm(response.iter_content()):
                fh.write(data)
        logger.info(f"Completed {dest}")

# Cell

# just export the gene list constants for speed later
import os, pickle
GTEX_GENES_ENSG = pickle.load(open(os.path.join(cache_dir, "GTEX_GENES_ENSG.pkl"), "rb"))
GTEX_GENES_SYMBOL = pickle.load(open(os.path.join(cache_dir, "GTEX_GENES_SYMBOL.pkl"), "rb"))
GTEX_GENES_SYMBOL_DUPLICATES = pickle.load(open(os.path.join(cache_dir, "GTEX_GENES_SYMBOL_DUPLICATES.pkl"), "rb"))