import os
import pandas as pd

os.chdir(r'C:\Users\Acer\Desktop\P1\Datasets')

clinvar_gain_1 = pd.read_table('Clinvar_copy_number_gain.txt', sep='\t', comment='#', names=['name_1', 'genes',
                                                                                             'protein_change',
                                                                                             'conditions',
                                                                                             'clinical_significance',
                                                                                             'review_status',
                                                                                             'ID',
                                                                                             'chromosome',
                                                                                             'GRCh37Location',
                                                                                             'GRCh38Chromosome',
                                                                                             'GRCh38Location',
                                                                                             'VariationID',
                                                                                             'AlleleID(s)', 'dbSNP',
                                                                                             'ID_1'])

clinvar_loss_1 = pd.read_table('Clinvar_copy_number_loss.txt', sep='\t', comment='#', names=['name_1', 'genes',
                                                                                             'protein_change',
                                                                                             'conditions',
                                                                                             'clinical_significance',
                                                                                             'review_status',
                                                                                             'ID',
                                                                                             'chromosome',
                                                                                             'GRCh37Location',
                                                                                             'GRCh38Chromosome',
                                                                                             'GRCh38Location',
                                                                                             'VariationID',
                                                                                             'AlleleID(s)', 'dbSNP',
                                                                                             'ID_1'])

# adding columns
clinvar_gain_1['data_source'] = 'clinvar'
clinvar_loss_1['data_source'] = 'clinvar'
clinvar_gain_1['variant_sub_type'] = 'gain'
clinvar_loss_1['variant_sub_type'] = 'loss'
clinvar_gain_1['gene_related_diseases'] = ''
clinvar_loss_1['gene_related_diseases'] = ''
clinvar_gain_1['variants'] = ''
clinvar_loss_1['variants'] = ''
clinvar_gain_1['num_unique_samples_tested'] = ''
clinvar_loss_1['num_unique_samples_tested'] = ''
clinvar_gain_1['population_summary'] = ''
clinvar_loss_1['population_summary'] = ''
clinvar_gain_1['frequency'] = ''
clinvar_loss_1['frequency'] = ''
clinvar_gain_1['platforms'] = ''
clinvar_loss_1['platforms'] = ''
clinvar_gain_1['algorithms'] = ''
clinvar_loss_1['algorithms'] = ''
clinvar_gain_1['studies'] = ''
clinvar_loss_1['studies'] = ''
clinvar_gain_1['inner_rank'] = ''
clinvar_loss_1['inner_rank'] = ''
clinvar_gain_1['deletion_observations'] = ''
clinvar_loss_1['deletion_observations'] = ''
clinvar_gain_1['deletion_frequency'] = ''
clinvar_loss_1['deletion_frequency'] = ''
clinvar_gain_1['deletion_standard_error'] = ''
clinvar_loss_1['deletion_standard_error'] = ''
clinvar_gain_1['duplication_observations'] = ''
clinvar_loss_1['duplication_observations'] = ''
clinvar_gain_1['duplication_frequency'] = ''
clinvar_loss_1['duplication_frequency'] = ''
clinvar_gain_1['duplication_standard_error'] = ''
clinvar_loss_1['duplication_standard_error'] = ''
clinvar_gain_1['standard_error'] = ''
clinvar_loss_1['standard_error'] = ''
clinvar_gain_1['number_case_population'] = ''
clinvar_loss_1['number_case_population'] = ''
clinvar_gain_1['number_case_individuals'] = ''
clinvar_loss_1['number_case_individuals'] = ''

# selecting the rows for only GRCh37 build
clinvar_gain_new = clinvar_gain_1[clinvar_gain_1['name_1'].str.match('GRCh37')]
clinvar_loss_new = clinvar_loss_1[clinvar_loss_1['name_1'].str.match('GRCh37')]

# extracting information from column to form new column
clinvar_gain_new['name_2'] = clinvar_gain_new.name_1.str.split(' ', n=1, expand=True)[1]
clinvar_gain_new['locus'] = clinvar_gain_new.name_2.str.split('(', expand=True)[0]
clinvar_gain_new['name'] = clinvar_gain_new.name_2.str.split('(', expand=True)[1]

new_loss = clinvar_loss_new['name_1'].str.split(' ', n=1, expand=True)
clinvar_loss_new['name_2'] = new_loss[1]
clinvar_loss_new['locus'] = clinvar_loss_new.name_2.str.split('(', expand=True)[0]
clinvar_loss_new['name'] = clinvar_loss_new.name_2.str.split('(', expand=True)[1]

clinvar_gain_new['GRCh37Location'] = clinvar_gain_new['GRCh37Location'].str.replace(' ', '')
clinvar_loss_new['GRCh37Location'] = clinvar_loss_new['GRCh37Location'].str.replace(' ', '')

clinvar_gain_new['start'] = clinvar_gain_new.GRCh37Location.str.split('-', expand=True)[0]
clinvar_gain_new['stop'] = clinvar_gain_new.GRCh37Location.str.split('-', expand=True)[1]

clinvar_loss_new['start'] = clinvar_loss_new.GRCh37Location.str.split('-', expand=True)[0]
clinvar_loss_new['stop'] = clinvar_loss_new.GRCh37Location.str.split('-', expand=True)[1]

# making a copy so that you have the original as backup if you made a mistake plus deleting unnecessary fields
clinvar_new_gain_1 = clinvar_gain_new[['chromosome', 'start', 'stop', 'locus', 'variant_sub_type', 'ID', 'name',
                                       'clinical_significance', 'conditions', 'genes', 'gene_related_diseases',
                                       'variants', 'num_unique_samples_tested', 'population_summary', 'frequency',
                                       'platforms', 'algorithms', 'studies', 'inner_rank', 'review_status',
                                       'VariationID', 'AlleleID(s)', 'deletion_observations', 'deletion_frequency',
                                       'deletion_standard_error', 'duplication_observations', 'duplication_frequency',
                                       'duplication_standard_error', 'standard_error', 'number_case_population',
                                       'number_case_individuals', 'data_source', 'name_1', 'name_2', 'protein_change',
                                       'GRCh37Location', 'GRCh38Chromosome', 'GRCh38Location', 'dbSNP', 'ID_1']]\
    .copy().reset_index().drop(['index', 'name_1', 'name_2', 'protein_change', 'GRCh37Location', 'GRCh38Chromosome',
                                'GRCh38Location', 'dbSNP', 'ID_1'], axis=1)

clinvar_new_loss_1 = clinvar_loss_new[['chromosome', 'start', 'stop', 'locus', 'variant_sub_type', 'ID', 'name',
                                       'clinical_significance', 'conditions', 'genes', 'gene_related_diseases',
                                       'variants', 'num_unique_samples_tested', 'population_summary', 'frequency',
                                       'platforms', 'algorithms', 'studies', 'inner_rank', 'review_status',
                                       'VariationID', 'AlleleID(s)', 'deletion_observations', 'deletion_frequency',
                                       'deletion_standard_error', 'duplication_observations', 'duplication_frequency',
                                       'duplication_standard_error', 'standard_error', 'number_case_population',
                                       'number_case_individuals', 'data_source', 'name_1', 'name_2', 'protein_change',
                                       'GRCh37Location', 'GRCh38Chromosome', 'GRCh38Location', 'dbSNP', 'ID_1']]\
    .copy().reset_index().drop(['index', 'name_1', 'name_2', 'protein_change', 'GRCh37Location', 'GRCh38Chromosome',
                                'GRCh38Location', 'dbSNP', 'ID_1'], axis=1)

# merging from two tables
clinvar = pd.concat([clinvar_new_gain_1, clinvar_new_loss_1])

clinvar.to_excel('Clinvar_copy_number_new.xlsx', index=False, header=True)
