import pandas as pd
import matplotlib.pyplot as plt

# Read eigenvectors
pca = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/cohort_pca.eigenvec", sep=r"\s+")

plt.figure(figsize=(8,6))
plt.scatter(pca["PC1"], pca["PC2"], s=12)

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Unfiltered cohort PCA")

plt.tight_layout()
plt.savefig("cohort_pca.png", dpi=300)
