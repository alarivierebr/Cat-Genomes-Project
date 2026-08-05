#!/bin/bash -l

############# SLURM SETTINGS #############

#SBATCH --account=project0076
#SBATCH --job-name=mutyperS
#SBATCH --time=12:00:00
#SBATCH --partition=nodes,smp
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G

#SBATCH --output=/mnt/autofs/data/userdata/project0076/annalise/filtering/mutyper/logs/%x-%j.out
#SBATCH --error=/mnt/autofs/data/userdata/project0076/annalise/filtering/mutyper/logs/%x-%j.err

#SBATCH --mail-user=3175404l@student.gla.ac.uk
#SBATCH --mail-type=BEGIN,END,FAIL
set -euo pipefail

OUT_DIR="/mnt/autofs/data/userdata/project0076/annalise/filtering/mutyper/spectra"

mkdir -p "${OUT_DIR}"

FELIDAE_VCF="/mnt/autofs/data/userdata/project0076/annalise/filtering/mutyper/cohort_felidae_var.vcf.gz"
FELIS_VCF="/mnt/autofs/data/userdata/project0076/annalise/filtering/mutyper/cohort_felis_var.vcf.gz"

OUTPUT_FELIDAE="felidae_mut.tsv"
OUTPUT_FELIS="felis_mut.tsv"

[[ -f "${FELIDAE_VCF}" ]] || {
    echo "ERROR: Missing input file: ${FELIDAE_VCF}" >&2
    exit 1
}

[[ -f "${FELIS_VCF}" ]] || {
    echo "ERROR: Missing input file: ${FELIS_VCF}" >&2
    exit 1
}

mutyper spectra "${FELIDAE_VCF}" \
    > "${OUT_DIR}/felidae_mut.tsv"

mutyper spectra "${FELIS_VCF}" \
    > "${OUT_DIR}/felis_mut.tsv"