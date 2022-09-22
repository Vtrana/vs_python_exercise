# import package
import pandas as pd

# Convert csv to a dataframe in pandas
df = pd.read_csv("brca_cnvs_tcga-1.csv")
print(df.head())

# Create new column "lenght" and calculate lenght of the segment
df["lenght"]=df["loc.end"]-df["loc.start"]   
print(df.head())

# Save file with hew data
df.to_csv('brca_cnvs_tcga-1_new.csv', index=False)
