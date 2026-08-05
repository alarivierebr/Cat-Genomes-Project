#!/bin/bash -l

############# SLURM SETTINGS #############

#SBATCH --account=project0076
#SBATCH --job-name=outlier_filter
#SBATCH --time=12:00:00
#SBATCH --partition=nodes,smp
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G

#SBATCH --output=/mnt/autofs/data/userdata/project0076/annalise/filtering/logs/%x-%j.out
#SBATCH --error=/mnt/autofs/data/userdata/project0076/annalise/filtering/logs/%x-%j.err

#SBATCH --mail-user=3175404l@student.gla.ac.uk
#SBATCH --mail-type=BEGIN,END,FAIL

#Input/output files
INPUT_VCF="/mnt/autofs/data/userdata/project0076/annalise/filtering/filtered.all.chromosomes.vcf.gz"
OUTPUT_VCF="/mnt/autofs/data/userdata/project0076/annalise/filtering/filtered.noOutlier.vcf.gz"

#Remove outlier sample, only keep only biallelic variant sites
bcftools view \
    --samples ^SAMN14425583 \
	-m 2 \
	-M 2 \
	-c 2:minor \
	-A \
	-a \
	--threads "${SLURM_CPUS_PER_TASK}" \
	-Oz \
	-o "${OUTPUT_VCF}" \
	--write-index=tbi \
	"${INPUT_VCF}"