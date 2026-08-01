READ ME!!!!

Information about this code will go here!


# Configuration

The bash script `pysam_filter.sh` accepts the environment variables `WORK_DIR` and `OUTPUT_DIR` to set the working directory and output directory respectively.
There can be set in the `config` file in same folder as the bash script.

The `WORK_DIR` variable should be set to the filepath containing the `.vcf.gz` file you want to filter. The format should be as follows:

```bash

WORK_DIR="file/path/to/folder/containing/your/data"
OUTPUT_DIR="file/path/to/where/you/want/your/data/saved"

```
The `pysam_filter.sh` file executes the code contained in `filter_variants.py`, and is designed to operate on a SLURM High Power Computing Cluster. SLURM Settings are left blank, please edit them according to your HPC's requirements. An example of the settings that can be used is as follows:

```bash
#!/bin/bash -l

############# SLURM SETTINGS #############

#SBATCH --account=youraccountname
#SBATCH --job-name=filter
#SBATCH --time=48:00:00
#SBATCH --partition=hpc_partition_name
#SBATCH --cpus-per-task=4
#SBATCH --mem=256G

#SBATCH --output=<filepath_to_logs_folder>/%x-%A_%a.out
#SBATCH --error=<filepath_to_errorlogs_folder>/%x-%A_%a.err

```

