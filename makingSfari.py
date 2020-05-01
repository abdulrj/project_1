import os
import pandas as pd

os.chdir(r'C:\Users\Acer\Desktop\P1\Datasets')

sfari_1 = pd.read_csv('SFARIGene_cnvs_10_31_2019.csv', names=['status', 'locus', 'variant_sub_type', 'deletion_values',
                                                              'duplication_values', 'animal_model', 'number_of_reports',
                                                              'number_case_population', 'number_case_individuals',
                                                              'basepair_range'])

# adding columns
sfari_1['data_source'] = 'sfari'
sfari_1['ID'] = ''
sfari_1['name'] = ''
sfari_1['clinical_significance'] = ''
sfari_1['conditions'] = ''
sfari_1['genes'] = ''
sfari_1['gene_related_diseases'] = ''
sfari_1['variants'] = ''
sfari_1['num_unique_samples_tested'] = ''
sfari_1['population_summary'] = ''
sfari_1['frequency'] = ''
sfari_1['platforms'] = ''
sfari_1['algorithms'] = ''
sfari_1['studies'] = ''
sfari_1['inner_rank'] = ''
sfari_1['review_status'] = ''
sfari_1['VariationID'] = ''
sfari_1['AlleleID(s)'] = ''
sfari_1['deletion_observations'] = ''
sfari_1['deletion_frequency'] = ''
sfari_1['deletion_standard_error'] = ''
sfari_1['duplication_observations'] = ''
sfari_1['duplication_frequency'] = ''
sfari_1['duplication_standard_error'] = ''
sfari_1['standard_error'] = ''

# extracting information from column to form new column
sfari_1['chromosome'] = sfari_1['locus'].str[:2]

sfari_1['start'] = sfari_1.basepair_range.str.split('-', expand=True)[0]
sfari_1['stop'] = sfari_1.basepair_range.str.split('-', expand=True)[1]

# remove certain characters from a string in column
sfari_1['chromosome'] = sfari_1.chromosome.str.replace(r'p', '', regex=True).str.strip()
sfari_1['chromosome'] = sfari_1.chromosome.str.replace(r'q', '', regex=True).str.strip()


# making a copy so that you have the original as backup if you made a mistake plus deleting unnecessary fields
sfari_2 = sfari_1[['chromosome', 'start', 'stop', 'locus', 'variant_sub_type', 'ID', 'name', 'clinical_significance',
                   'conditions', 'genes', 'gene_related_diseases', 'variants', 'num_unique_samples_tested',
                   'population_summary', 'frequency', 'platforms', 'algorithms', 'studies', 'inner_rank',
                   'review_status', 'VariationID', 'AlleleID(s)', 'deletion_observations', 'deletion_frequency',
                   'deletion_standard_error', 'duplication_observations', 'duplication_frequency',
                   'duplication_standard_error', 'standard_error', 'number_case_population', 'number_case_individuals',
                   'data_source', 'deletion_values', 'duplication_values',
                   'number_of_reports', 'status', 'animal_model', 'basepair_range']].copy().reset_index()\
    .drop(['index', 'deletion_values', 'duplication_values', 'number_of_reports', 'status', 'animal_model',
           'basepair_range'], axis=1)

sfari_2.to_excel('SFARIGene_cnvs_10_31_2019_new.xlsx', index=False, header=True)
