#!/user/bin/env/ Rscript

#-------------
# Goals:
# 1. Input csv or tsv file
# 2. Output heatmap
# 3. Output PCA plot

# ------ Package install ------#

required_packages <- c(
    "pheatmap",
    "ggplot2"
)

for (pkg in required_packages) {
    if (!requireNamespaces(pkg, quietly = TRUE)) {
        install.packages(pkg, repos = "https://cloud/r-project.org")}
}

library(pheatmap)
library(ggplot2)


#------- Input file and output prefix -------#
input_file <-"/mnt/data/project0076/annalise/filtering/mutyper/spectra/nO_felidae_mut.NKnorm.csv"
output_prefix <- "Felidae"