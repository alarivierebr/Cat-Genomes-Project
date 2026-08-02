import pandas as pd
import matplotlib.pyplot as plt

# Read eigenvectors
# pca = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/unfiltered/cohort_pca.eigenvec", sep=r"\s+")
# print(pca.columns.tolist())
# #exit()

# plt.figure(figsize=(8,6))
# #plt.scatter(pca["PC1"], pca["PC2"], s=12)

# metadata = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/metadata.csv")

# pca = pca.merge(metadata, on="IID")
# print(pca.columns.tolist())
# print(pca.groupby(by="Breed").groups)

# for IID, Breed in pca.groupby(pca.Breed):
#     plt.scatter(Breed["PC1"], Breed["PC2"], label="Breed")


# plt.xlabel("PC1")
# plt.ylabel("PC2")
# plt.title("Unfiltered cohort PCA")

# plt.tight_layout()
# plt.savefig("cohort_pca.png", dpi=300)

#--------------------------------

# Read eigenvectors
pca = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/filtered/filtered_cohort_pca.eigenvec", sep=r"\s+")
print(pca.columns.tolist())
#exit()

plt.figure(figsize=(8,6))
#plt.scatter(pca["PC1"], pca["PC2"], s=12)

metadata = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/metadata.csv")

pca = pca.merge(metadata, on="IID")
print(pca.columns.tolist())
print(pca.groupby(by="Breed").groups)

for IID, Breed in pca.groupby(pca.Breed):
    plt.scatter(Breed["PC1"], Breed["PC2"], label="Breed")
    print(IID)


plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Filtered cohort PCA")

plt.tight_layout()
plt.savefig("filtered_cohort_pca.png", dpi=300)

#Do I want it to be grouped by Breed, or ony colored by breed, but each point is still individual?????