#!/bin/bash -l

############# SLURM SETTINGS #############

#SBATCH --account=project0076
#SBATCH --job-name=mutyperV
#SBATCH --time=12:00:00
#SBATCH --partition=nodes,smp
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G

#SBATCH --output=/mnt/autofs/data/userdata/project0076/annalise/filtering/logs/%x-%j.out
#SBATCH --error=/mnt/autofs/data/userdata/project0076/annalise/filtering/logs/%x-%j.err

#SBATCH --mail-user=3175404l@student.gla.ac.uk
#SBATCH --mail-type=BEGIN,END,FAIL

set -euo pipefail

FELIDAE_ANC="/mnt/data/project0076/Cats/ancestral_genomes/ANCESTRAL_GENOME_FELIDAE/ancestral/ancestral_genome/ancestral.fasta"
FELIS_ANC="/mnt/data/project0076/Cats/ancestral_genomes/ANCESTRAL_GENOME_FELIS/ancestral/ancestral_genome/ancestral.fasta"


OUT_DIR="/mnt/autofs/data/userdata/project0076/annalise/filtering/mutyper"

mkdir -p "${OUT_DIR}"

COHORT_ANN="${OUT_DIR}/noOutlier.ann.all.chromosomes.tags.vcf.gz"

[[ -f "${COHORT_ANN}" ]] || {
    echo "ERROR: Cannot find ${COHORT_ANN}" >&2
    exit 1
}

mutyper variants "${FELIDAE_ANC}" "${COHORT_ANN}" \
	| bcftools view \
	-Oz \
	--threads "${SLURM_CPUS_PER_TASK}" \
	--write-index=tbi \
	-o "${OUT_DIR}/nO_cohort_felidae_var.vcf.gz"

mutyper variants "${FELIS_ANC}" "${COHORT_ANN}" \
	| bcftools view \
	-Oz \
	--threads "${SLURM_CPUS_PER_TASK}" \
	--write-index=tbi \
	-o "${OUT_DIR}/nO_cohort_felis_var.vcf.gz"
