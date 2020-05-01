import os
import pandas as pd

os.chdir(r'C:\Users\Acer\Desktop\P1\Datasets')


def at_in(x):
    # Extract important information from the attributes field
    idd_ = list(filter(lambda xx: 'ID' in xx, x.split(';')))[0].split('=')[1]
    v_s = list(filter(lambda xx: 'variant_sub_type' in xx, x.split(';')))[0].split('=')[1]
    o_s = list(filter(lambda xx: 'outer_start' in xx, x.split(';')))[0].split('=')[1]
    i_s = list(filter(lambda xx: 'inner_start' in xx, x.split(';')))[0].split('=')[1]
    i_e = list(filter(lambda xx: 'inner_end' in xx, x.split(';')))[0].split('=')[1]
    o_e = list(filter(lambda xx: 'outer_end' in xx, x.split(';')))[0].split('=')[1]
    variants_ = list(filter(lambda xx: 'variants' in xx, x.split(';')))[0].split('=')[1]
    studies_ = list(filter(lambda xx: 'Studies' in xx, x.split(';')))[0].split('=')[1]
    platforms_ = list(filter(lambda xx: 'Platforms' in xx, x.split(';')))[0].split('=')[1]
    algorithms_ = list(filter(lambda xx: 'algorithms' in xx, x.split(';')))[0].split('=')[1]
    samples_ = list(filter(lambda xx: 'samples' in xx, x.split(';')))[0].split('=')[1]
    frequency_ = list(filter(lambda xx: 'Frequency' in xx, x.split(';')))[0].split('=')[1]
    p_s = list(filter(lambda xx: 'PopulationSummary' in xx, x.split(';')))[0].split('=')[1]
    i_r = list(filter(lambda xx: 'inner_rank' in xx, x.split(';')))[0].split('=')[1]
    n_u_s_t = list(filter(lambda xx: 'num_unique_samples_tested' in xx, x.split(';')))[0].split('=')[1]
    return (idd_, v_s, o_s, i_s, i_e, o_e, variants_, studies_, platforms_,
            algorithms_, samples_, frequency_, p_s, i_r, n_u_s_t)


dgv_gold_1 = pd.read_table('DGV_GS_March2016_50percent_GainLossSep_Final_hg19.gff3.txt', sep='\t', comment='#',
                           names=['chromosome', 'structural_variant', 'region', 'similar_outer_start_inner_1',
                                  'similar_outer_start_inner_2', 'null_1', 'null_2', 'null_3', 'attribute'])

# print(dgv_gold_1.head())
# dgv_gold_1.info()
# print(dgv_gold_1['attribute'])

# separating the attributes to multiple columns
dgv_gold_1['ID'], dgv_gold_1['variant_sub_type'], dgv_gold_1['start'], dgv_gold_1['inner_start'], \
    dgv_gold_1['inner_end'], dgv_gold_1['stop'], dgv_gold_1['variants'], dgv_gold_1['studies'], \
    dgv_gold_1['platforms'], dgv_gold_1['algorithms'], dgv_gold_1['samples'], dgv_gold_1['frequency'], \
    dgv_gold_1['population_summary'], dgv_gold_1['inner_rank'], dgv_gold_1['num_unique_samples_tested'] \
    = zip(*dgv_gold_1.attribute.apply(lambda x: at_in(x)))

# remove certain characters from a string in column
dgv_gold_1['chromosome'] = dgv_gold_1['chromosome'].str[3:]

# adding columns
dgv_gold_1['data_source'] = 'DGV'
dgv_gold_1['locus'] = ''
dgv_gold_1['genes'] = ''
dgv_gold_1['name'] = ''
dgv_gold_1['clinical_significance'] = ''
dgv_gold_1['conditions'] = ''
dgv_gold_1['gene_related_diseases'] = ''
dgv_gold_1['review_status'] = ''
dgv_gold_1['VariationID'] = ''
dgv_gold_1['AlleleID(s)'] = ''
dgv_gold_1['deletion_observations'] = ''
dgv_gold_1['deletion_frequency'] = ''
dgv_gold_1['deletion_standard_error'] = ''
dgv_gold_1['duplication_observations'] = ''
dgv_gold_1['duplication_frequency'] = ''
dgv_gold_1['duplication_standard_error'] = ''
dgv_gold_1['standard_error'] = ''
dgv_gold_1['number_case_population'] = ''
dgv_gold_1['number_case_individuals'] = ''

# changing the percentage in the frequency column
dgv_gold_1['frequency'] = dgv_gold_1['frequency'].str.replace('%', '')
dgv_gold_1['frequency'] = dgv_gold_1.frequency.astype(float)
dgv_gold_1['frequency'] = dgv_gold_1['frequency']/100

# making a copy so that you have the original as backup if you made a mistake plus deleting unnecessary fields
dgv_gold_2 = dgv_gold_1[['chromosome', 'start', 'stop', 'locus', 'variant_sub_type', 'ID', 'name',
                         'clinical_significance', 'conditions', 'genes', 'gene_related_diseases', 'variants', 'samples',
                         'num_unique_samples_tested', 'population_summary', 'frequency', 'platforms', 'algorithms',
                         'studies', 'inner_rank', 'review_status', 'VariationID', 'AlleleID(s)',
                         'deletion_observations', 'deletion_frequency', 'deletion_standard_error',
                         'duplication_observations', 'duplication_frequency', 'duplication_standard_error',
                         'standard_error', 'number_case_population', 'number_case_individuals', 'data_source',
                         'structural_variant', 'region', 'similar_outer_start_inner_1', 'similar_outer_start_inner_2',
                         'null_1', 'null_2', 'null_3', 'attribute', 'inner_start', 'inner_end']].copy().reset_index()\
    .drop(['index', 'structural_variant', 'region', 'similar_outer_start_inner_1', 'similar_outer_start_inner_2',
           'null_1', 'null_2', 'null_3', 'attribute', 'inner_start', 'inner_end', 'samples'], axis=1)

dgv_gold_2.to_excel('DGV_GS_March2016_50percent_GainLossSep_Final_hg19_new.gff3.xlsx', index=False, header=True)
