#!/user/bin/env Rscript

#-------------
# Goals:
# 1. Input multiqc informartion csv and clean it up
# 2. Output barplot of statistics
# 3. Output or print summary statistics

# ------ Package install ------#

required_packages <- c(
    "tidyverse",
    "janitor"
)

for (pkg in required_packages) {
    if (!requireNamespace(pkg, quietly = TRUE)) {
        stop(
            "Required package '", pkg,
            "' is not installed in this environment."
        )
    }
}

library(tidyverse)
library(janitor)


