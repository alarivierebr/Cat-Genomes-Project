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

# Set input csv file

input_file <- "/mnt/autofs/data/userdata/project0076/annalise/filtering/R_plots/multiqc_general_stats_edited.csv"
merged_output <- "/mnt/autofs/data/userdata/project0076/annalise/filtering/R_plots/multiqc_general_stats_merged.csv"
data <- read_csv(input_file, na = c("", "NA", "N/A", "NULL"))

#janitor function to tidy up the column names in csv
data <- clean_names(data)

# checking columns
cat("Columns", ncol(data), "\n\n")

#merging rows into one per sample
data <- data %>%
    mutate(
        Sample_ID = sample %>%
            str_remove("\\.(md|recal|deepvariant)$") %>%
            str_remove("_[0-9]+$") %>%
            str_remove("-*$")
    )

#setting the columns other than sample to metrics
metric_columns <- setdiff(
    names(data),
    c("sample", "Sample_ID")
)

data <- data %>%
    mutate(
        across(
            all_of(metric_columns),
            ~ suppressWarnings(as.numeric(.))
        )
    )

#merging data

#setting row priority because I want it to prioritize the recalibrated values over the markduplicates values.
data <- data %>%
    mutate(
        row_priority = case_when(
            str_detect(sample, "\\.recal$") ~1,
            str_detect(sample, "\\.md$") ~2,
            str_detect(sample, "\\.deepvariant$") ~3,
            TRUE ~ 4
        )
    )

data <- data %>%
    arrange(Sample_ID, row_priority)

merged_data <- data %>%
    group_by(Sample_ID) %>%
    summarise(
        across(
            all_of(metric_columns),
            ~ {
                x <- .x[!is.na(.x)]

                if (length(x) == 0) {
                    NA_real_
                } else {
                    x[1]

                }
            }
        ),
        .groups = "drop"
    )

merged_data <- remove_empty(merged_data)

print(merged_data, n = Inf)
write_csv(merged_data, merged_output)