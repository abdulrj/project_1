import os
import pandas as pd

os.chdir(r'C:\Users\Acer\Desktop\P1\Datasets')

decipher_1 = pd.read_table('Decipher_population_cnv.txt', sep='\t', comment='#', names=['population_cnv_id',
                                                                                        'chromosome', 'start', 'stop',
                                                                                        'deletion_observations',
                                                                                        'deletion_frequency',
                                                                                        'deletion_standard_error',
                                                                                        'duplication_observations',
                                                                                        'duplication_frequency',
                                                                                        'duplication_standard_error',
                                                                                        'variants', 'frequency',
                                                                                        'standard_error', 'type',
                                                                                        'num_unique_samples_tested',
                                                                                        'studies'])

# adding columns
decipher_1['data_source'] = 'decipher'
decipher_1['locus'] = ''
decipher_1['variant_sub_type'] = ''
decipher_1['ID'] = ''
decipher_1['name'] = ''
decipher_1['clinical_significance'] = ''
decipher_1['conditions'] = ''
decipher_1['genes'] = ''
decipher_1['gene_related_diseases'] = ''
decipher_1['population_summary'] = ''
decipher_1['platforms'] = ''
decipher_1['algorithms'] = ''
decipher_1['inner_rank'] = ''
decipher_1['review_status'] = ''
decipher_1['VariationID'] = ''
decipher_1['AlleleID(s)'] = ''
decipher_1['number_case_population'] = ''
decipher_1['number_case_individuals'] = ''

# making a copy so that you have the original as backup if you made a mistake plus deleting unnecessary fields
decipher_2 = decipher_1[['chromosome', 'start', 'stop', 'locus', 'variant_sub_type', 'ID', 'name',
                         'clinical_significance', 'conditions', 'genes', 'gene_related_diseases', 'variants',
                         'num_unique_samples_tested', 'population_summary', 'frequency', 'platforms', 'algorithms',
                         'studies', 'inner_rank', 'review_status', 'VariationID', 'AlleleID(s)',
                         'deletion_observations', 'deletion_frequency', 'deletion_standard_error',
                         'duplication_observations', 'duplication_frequency', 'duplication_standard_error',
                         'standard_error', 'number_case_population', 'number_case_individuals', 'data_source', 'type',
                         'population_cnv_id']].copy().reset_index()\
    .drop(['index', 'population_cnv_id', 'type'], axis=1)

decipher_2.to_excel('Decipher_population_cnv_new.xlsx', index=False, header=True)
