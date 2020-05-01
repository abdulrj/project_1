import os
import pandas as pd

os.chdir(r'C:\Users\Acer\Desktop\P1\Datasets')

df_dgv_gold = pd.read_excel('DGV_GS_March2016_50percent_GainLossSep_Final_hg19_new.gff3.xlsx', header=0)

df_clinvar = pd.read_excel('Clinvar_copy_number_new.xlsx', header=0)

df_decipher = pd.read_excel('Decipher_population_cnv_new.xlsx', header=0)

df_sfari = pd.read_excel('SFARIGene_cnvs_10_31_2019_new.xlsx', header=0)

# merging the tables
df_main = pd.concat([df_dgv_gold, df_clinvar, df_decipher, df_sfari])

# dropping duplicate rows
df_main.drop_duplicates(inplace=True)

df_main.to_excel('main_database.xlsx', index=False, header=True)

# remember to 'x' and 'y' to 23 chromosome by using the find and replace in excel and don't forget to also change the
# .csv file since script can only read in this file type.

