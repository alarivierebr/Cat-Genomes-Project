#!/bin/bash -l

############# SLURM SETTINGS #############

#SBATCH --account=
#SBATCH --job-name=
#SBATCH --time=48:00:00
#SBATCH --partition=
#SBATCH --cpus-per-task=4
#SBATCH --mem=256G

#SBATCH --output=%x-%A_%a.out
#SBATCH --error=%x-%A_%a.err

source config

WD="${WORK_DIR}"
OUT_DIR="${OUTPUT_DIR}"

INPUT_VCF="${WD}/cohort.full.vcf.gz"
INDEX="${WD}/cohort.full.vcf.gz.csi"
OUTPUT_VCF="${OUT_DIR}/filtered.vcf"

#List of Cat Genome chromosome names

chromosomes=(
"NC_058368.1"
"NC_058369.1"
"NC_058370.1"
"NC_058371.1"
"NC_058372.1"
"NC_058373.1"
"NC_058374.1"
"NC_058375.1"
"NC_058376.1"
"NC_058377.1"
"NC_058378.1"
"NC_058379.1"
"NC_058380.1"
"NC_058381.1"
"NC_058382.1"
"NC_058383.1"
"NC_058384.1"
"NC_058385.1"
"NC_058386.1"
"NC_001700.1"
)

CHR_VCF="${OUT_DIR}/${chromosome}.vcf.gz"
CHR_OUT="${OUT_DIR}/${chromosome}.filtered.vcf"

for chromosome in "${chromosomes[@]}"; do
	bcftools view -r "${chromosome}" "${INPUT_VCF}" | \
	python3 filter_variants.py \
		-i - \
		-o "${OUT_DIR}/${chromosome}.filtered.vcf.gz"
done

bcftools concat \
    ${OUT_DIR}/NC_*.filtered.vcf.gz \
    -Oz \
    -o filtered.all.chromosomes.vcf.gz


