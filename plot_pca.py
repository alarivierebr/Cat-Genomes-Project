import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import colorcet as cc
from matplotlib.patches import Ellipse


# #--------------------- Full cohort-----------------#
# Read eigenvectors (PCA coordinates)

pca = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/filtered/filtered_cohort_pca.eigenvec", sep=r"\s+")
eigenval = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/filtered/filtered_cohort_pca.eigenval", header=None)


variance_explained = eigenval[0] / eigenval[0].sum() * 100

pc1_variance = variance_explained.iloc[0]
pc2_variance = variance_explained.iloc[1]

#loading metadata, includes information on Breed and Group
metadata = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/metadata2.csv")

#merge metadata and pca coordinates into one data frame
pca=pca.merge(metadata, on="IID", how="left")

sns.set_theme(style="white", context="paper", font_scale=1.3)

plt.figure(figsize=(8, 7))

groups = pca["Group"].unique()

palette = sns.color_palette("hls", len(groups))

sns.scatterplot(
    data=pca,
    x="PC1",
    y="PC2",
    hue="Group",
    palette=palette,
    s=35,
    alpha=0.8,
    linewidth=0.2,
    edgecolor="black"
    )

plt.xlabel(
    f"PC1 ({pc1_variance:.2f}%)", fontsize=14)
plt.ylabel(
    f"PC2 ({pc2_variance:.2f}%)", fontsize=14)
plt.title("Test4 PCA", fontsize=16, weight="bold")

plt.legend(
    title= "Breed",
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    frameon=True,
    fontsize=9,
    title_fontsize=10,
)

sns.despine()
plt.tight_layout()
plt.savefig("test4_base_pca.png", dpi=600, bbox_inches="tight")


#--------------------Domestic Only Set-------------------#

pca2 = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/test4_norm/test4_bcftools_filter/dom/t4_dom_only.eigenvec", sep=r"\s+")
eigenval = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/test4_norm/test4_bcftools_filter/dom/t4_dom_only.eigenval", header=None)


# variance calcs
variance_explained = eigenval[0] / eigenval[0].sum() * 100

pc1_variance = variance_explained.iloc[0]
pc2_variance = variance_explained.iloc[1]

#loading metadata, includes information on Breed and Group
metadata = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/metadata_domestic_grouped.csv")


pca2.columns = [
    "FID", "IID",
    "PC1", "PC2", "PC3", "PC4", "PC5",
    "PC6", "PC7", "PC8", "PC9", "PC10"
]

#merge metadata and pca coordinates into one data frame
pca2=pca2.merge(metadata, on="IID", how="left")

sns.set_theme(style="white", context="paper", font_scale=1.3)

plt.figure(figsize=(10, 8))

breeds = pca2["Breed"].unique()

palette = cc.glasbey_bw_minc_20_maxl_70[:pca2["Breed"].nunique()]
breed_palette = dict(zip(breeds, palette))

sns.scatterplot(
    data=pca2,
    x="PC1",
    y="PC2",
    hue="Breed",
    palette=breed_palette,
    s=30,
    alpha=0.8,
    linewidth=0.5,
    edgecolor="black"
    )


plt.xlabel(
    f"PC1 ({pc1_variance:.2f}%)", fontsize=14)
plt.ylabel(
    f"PC2 ({pc2_variance:.2f}%)", fontsize=14)
plt.title("Domestic Only PCA1-2, maf = 0.05, genotype = 0.1", fontsize=16, weight="bold")


handles, labels = plt.gca().get_legend_handles_labels()
order = sorted(zip(labels, handles), key = lambda x: x[0])

plt.legend(
    [h for l, h in order],
    [l for l, h in order],
    title= "Breed",
    bbox_to_anchor=(0.5, -0.15),
    loc="upper center",
    ncol=6,
    frameon=True,
    fontsize=8,
    title_fontsize=10,
)

sns.despine()
plt.tight_layout()
plt.subplots_adjust(bottom=0.25)
plt.savefig("T4_domestic_only_cohort_pca.png", dpi=600, bbox_inches="tight")


#--------------------Domestic Only Set PC3 and 4-------------------#

pca3 = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/test4_norm/test4_bcftools_filter/dom/t4_dom_only.eigenvec", sep=r"\s+")
eigenval = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/test4_norm/test4_bcftools_filter/dom/t4_dom_only.eigenval", header=None)


# variance calcs
variance_explained = eigenval[0] / eigenval[0].sum() * 100

pc3_variance = variance_explained.iloc[2]
pc4_variance = variance_explained.iloc[3]

#loading metadata, includes information on Breed and Group
metadata = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/metadata_domestic_grouped.csv")


pca3.columns = [
    "FID", "IID",
    "PC1", "PC2", "PC3", "PC4", "PC5",
    "PC6", "PC7", "PC8", "PC9", "PC10"
]

#merge metadata and pca coordinates into one data frame
pca3=pca3.merge(metadata, on="IID", how="left")

sns.set_theme(style="white", context="paper", font_scale=1.3)

plt.figure(figsize=(10, 8))

breeds = pca3["Breed"].unique()

palette = cc.glasbey_bw_minc_20_maxl_70[:pca3["Breed"].nunique()]
breed_palette = dict(zip(breeds, palette))

sns.scatterplot(
    data=pca3,
    x="PC3",
    y="PC4",
    hue="Breed",
    palette=breed_palette,
    s=30,
    alpha=0.8,
    linewidth=0.5,
    edgecolor="black"
    )


plt.xlabel(
    f"PC3 ({pc3_variance:.2f}%)", fontsize=14)
plt.ylabel(
    f"PC4 ({pc4_variance:.2f}%)", fontsize=14)
plt.title("Domestic Only PCA3-4, maf = 0.05, genotype = 0.1", fontsize=16, weight="bold")


handles, labels = plt.gca().get_legend_handles_labels()
order = sorted(zip(labels, handles), key = lambda x: x[0])

plt.legend(
    [h for l, h in order],
    [l for l, h in order],
    title= "Breed",
    bbox_to_anchor=(0.5, -0.15),
    loc="upper center",
    ncol=6,
    frameon=True,
    fontsize=8,
    title_fontsize=10,
)

sns.despine()
plt.tight_layout()
plt.subplots_adjust(bottom=0.25)
plt.savefig("T4_domestic_only_cohort_pca_3_4.png", dpi=600, bbox_inches="tight")





#--------------------Wild Only Set-------------------#

pca4 = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/test4_norm/test4_bcftools_filter/wild/t4_wild_only.eigenvec", sep=r"\s+", header=0)
eigenval = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/test4_norm/test4_bcftools_filter/wild/t4_wild_only.eigenval", header=None)

variance_explained = eigenval[0] / eigenval[0].sum() * 100

pc1_variance = variance_explained.iloc[0]
pc2_variance = variance_explained.iloc[1]

pca4.columns = [
    "FID", "IID",
    "PC1", "PC2", "PC3", "PC4", "PC5",
    "PC6", "PC7", "PC8", "PC9", "PC10"
]

#loading metadata, includes information on Breed and Group
metadata = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/metadata_wild.csv")

pca4["IID"] = pca4["IID"].astype(str).str.strip()
metadata["IID"] = metadata["IID"].astype(str).str.strip()

#merge metadata and pca coordinates into one data frame
pca4=pca4.merge(metadata, on="IID", how="left")


sns.set_theme(style="white", context="paper", font_scale=1.3)

plt.figure(figsize=(8, 7))

breeds = pca4["Breed"].unique()

palette = sns.color_palette("hls", len(breeds))

sns.scatterplot(
    data=pca4,
    x="PC1",
    y="PC2",
    hue="Breed",
    palette=palette,
    s=35,
    alpha=0.8,
    linewidth=0.2,
    edgecolor="black"
    )


plt.xlabel(
    f"PC1 ({pc1_variance:.2f}%)", fontsize=14)
plt.ylabel(
    f"PC2 ({pc2_variance:.2f}%)", fontsize=14)
plt.title("Wild Only PCA, maf = 0.05, genotype = 0.1", fontsize=16, weight="bold")


plt.legend(
    title= "Breed",
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    frameon=True,
    fontsize=9,
    title_fontsize=10,
)

sns.despine()
plt.tight_layout()
plt.savefig("t4_wild_only_cohort_pca.png", dpi=600, bbox_inches="tight")




#--------------------Wild Only Set PCs 3-4 -------------------#

pca5 = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/test4_norm/test4_bcftools_filter/wild/t4_wild_only.eigenvec", sep=r"\s+", header=0)
eigenval = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/test4_norm/test4_bcftools_filter/wild/t4_wild_only.eigenval", header=None)

variance_explained = eigenval[0] / eigenval[0].sum() * 100

pc3_variance = variance_explained.iloc[2]
pc4_variance = variance_explained.iloc[3]

pca5.columns = [
    "FID", "IID",
    "PC1", "PC2", "PC3", "PC4", "PC5",
    "PC6", "PC7", "PC8", "PC9", "PC10"
]

#loading metadata, includes information on Breed and Group
metadata = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/metadata_wild.csv")

pca5["IID"] = pca5["IID"].astype(str).str.strip()
metadata["IID"] = metadata["IID"].astype(str).str.strip()

#merge metadata and pca coordinates into one data frame
pca5=pca5.merge(metadata, on="IID", how="left")


sns.set_theme(style="white", context="paper", font_scale=1.3)

plt.figure(figsize=(8, 7))

breeds = pca5["Breed"].unique()

palette = sns.color_palette("hls", len(breeds))

sns.scatterplot(
    data=pca5,
    x="PC3",
    y="PC4",
    hue="Breed",
    palette=palette,
    s=35,
    alpha=0.8,
    linewidth=0.2,
    edgecolor="black"
    )


plt.xlabel(
    f"PC3 ({pc3_variance:.2f}%)", fontsize=14)
plt.ylabel(
    f"PC4 ({pc4_variance:.2f}%)", fontsize=14)
plt.title("Wild Only PCA, maf = 0.05, genotype = 0.1", fontsize=16, weight="bold")


plt.legend(
    title= "Breed",
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    frameon=True,
    fontsize=9,
    title_fontsize=10,
)

sns.despine()
plt.tight_layout()
plt.savefig("t4_wild_only_cohort_pca_3_4.png", dpi=600, bbox_inches="tight")



#------------------------- Breed split plots ------- #

# Read eigenvectors (PCA coordinates)
#pca = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/filtered/filtered_cohort_pca.eigenvec", sep=r"\s+")
# pca = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/noOutlier_full/noOutlier_cohort_pca.eigenvec", sep=r"\s+")
# #loading metadata, includes information on Breed and Group
# metadata = pd.read_csv("/mnt/autofs/data/userdata/project0076/annalise/filtering/plink_files_pca/metadata.csv")

# #merge metadata and pca coordinates into one data frame
# pca=pca.merge(metadata, on="IID", how="left")

#Ordering breeds by sample size
# breed_order = (pca["Breed"].value_counts().sort_values(ascending=False).index)

# pca["Breed"] = pd.Categorical(pca["Breed"], categories=breed_order, ordered=True)

# sns.set_theme(style="white", context="paper", font_scale=1.4)

# group_palette = {
#     "Domestic": "#1b9e77",
#     "Chaus": "#d95f02",
#     "Margarita": "#ff0054",
#     "Nigripes": "#00b4d8",
#     "Silvestris": "#390099",
#     "Bieti": "#fb6f92",
#     "Lybica": "#008000",
#     "Ornata": "#9e0059",
#     "S.silvestris": "#ffba08",
#     "S.ornata": "#0a9396",
# }


# #Facet scatter plot

# g = sns.FacetGrid(
#     pca,
#     col="Breed",
#     col_wrap=5,
#     height=2.6,
#     margin_titles=True
# )

# g.map_dataframe(
#     sns.scatterplot,
#     x="PC1",
#     y="PC2",
#     hue="Group",
#     palette=group_palette,
#     s=18,
#     alpha=0.75,
#     linewidth=0,
# )

# g.set_titles(
#     "{col_name}",
#     size=11,
#     weight="bold"
# )

# g.set_axis_labels(
#     "PC1",
#     "PC2"
# )

# for ax in g.axes.flat:
#     sns.despine(ax=ax)

# #Add legend
# handles, labels = g.axes[0].get_legend_handles_labels()

# g.figure.legend(
#     handles,
#     labels,
#     title="Group",
#     loc="center right",
#     bbox_to_anchor=(1.00, 0.5),
#     frameon=True,
#     fontsize=10,
#     title_fontsize=11,
# )

# for ax in g.axes.flat:
#     if ax.legend_:
#         ax.legend_.remove()

# g.figure.suptitle(
#     "No Outlier Cohort PCA by Breed",
#     fontsize=15,
#     weight="bold",
#     y=1
# )

# plt.tight_layout()

# plt.savefig(
#     "no_outlier_cohort_by_breed_group.png",
#     dpi=600,
#     bbox_inches="tight"
# )

#------------------------#
# ax.set_title("No Outlier Cohort PCA", fontsize=16, weight="bold")
# ax.set_xlabel("PC1")
# ax.set_ylabel("PC2")


# sns.despine()

# ax.legend(title="Group", bbox_to_anchor=(1.02, 1), loc="upper left",
#         )

# plt.tight_layout()

# plt.savefig("no_outlier_cohort_pca.png",
#             dpi=600,
#             bbox_inches="tight",
# )

# plt.show()


#try to make plots with shapes AND colors, at least for domesti, merge the cross breeds into "cross breed" group


#FOR TSVS

# mutations (like AAA -> ATA) could be more present because there are more AAA in genome, and not cause they are significant changes) normalize by number of changes that you have in genome

# could make own python code that notes every three bases and then slides by one and counts

# canonical k mer AAT and TTA are same cause reverse strand 

# software kmc but smakcr is easier -c -k 3 and fasta file have to do that for the ancestral genomes, and that will give ancestral that are present and then can normalize with those values, normalise for initial triplet (AAA) not TTT use tht number then divide by number

# make heatmap to show variant changes

# could also use a k means admixture plot


# smackr aready installed on mars, so will point to that as it needs to be compiled (2nd link)

