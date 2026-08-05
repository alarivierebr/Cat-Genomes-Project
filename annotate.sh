#!/bin/bash -l

############# SLURM SETTINGS #############

#SBATCH --account=project0076
#SBATCH --job-name=annotate
#SBATCH --time=12:00:00
#SBATCH --partition=nodes,smp
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G

#SBATCH --output=/mnt/autofs/data/userdata/project0076/annalise/filtering/logs/%x-%j.out
#SBATCH --error=/mnt/autofs/data/userdata/project0076/annalise/filtering/logs/%x-%j.err

#SBATCH --mail-user=3175404l@student.gla.ac.uk
#SBATCH --mail-type=BEGIN,END,FAIL

set -euo pipefail

COHORT="/mnt/autofs/data/userdata/project0076/annalise/filtering/filtered.noOutlier.vcf.gz"

OUT_DIR="/mnt/autofs/data/userdata/project0076/annalise/filtering/mutyper"

bcftools +fill-tags \
    "${COHORT}" \
	--threads "${SLURM_CPUS_PER_TASK}" \
    -Oz \
    -o "${OUT_DIR}/noOutlier.ann.all.chromosomes.tags.vcf.gz" \
    -- -t AC,AN