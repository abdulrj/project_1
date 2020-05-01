import csv
import os

os.chdir(r'C:\Users\Acer\Desktop\P1\Datasets')


# function to calculate overlapping base pairs between query coordinates and gene coordinates
def overlap(query_start, query_end, gene_start, gene_end):
    # what about half in and half out coverage of genes?
    o = min(query_end, gene_end) - max(query_start, gene_start)
    return o


# function to return the interval coordinates in ranges
def intervals_range(start, end):
    q = range(start, end)
    return q


# function to just to check if the intervals overlap
def range_overlapping(x, y):
    if x.start == x.stop or y.start == y.stop:
        return False
    # general definition where it includes both full and partial overlap
    # maybe add / change something in the this function to determine whether it is partial or full
    return (x.start < y.stop and x.stop > y.start) or (x.stop > y.start and y.stop > x.start)


def g_name(x):
    # extract gene name
    g_n = list(filter(lambda xx: 'gene_name' in xx, x.split(';')))[0].split('=')[1]
    return g_n


def g_id(x):
    # extract gene id
    g_i = list(filter(lambda xx: 'gene_id' in xx, x.split(';')))[0].split('=')[1]
    return g_i


def g_st(x):
    # extract gene status
    g_s = list(filter(lambda xx: 'gene_status' in xx, x.split(';')))[0].split('=')[1]
    return g_s


def g_ty(x):
    # extract gene type
    g_t = list(filter(lambda xx: 'gene_type' in xx, x.split(';')))[0].split('=')[1]
    return g_t


def g_le(x):
    # extract gene level
    g_l = list(filter(lambda xx: 'level' in xx, x.split(';')))[0].split('=')[1]
    return g_l


# def a new function similar to above for other information you want to extract

# right now it will just pull the diseases based on the genes column already present in DGV and not the pulled ones from
# Gencode, remember to change later when you have merge between the two and remove duplicates
# need to also make the the gene for the disease at the same start and end or at least overlap to avoid pulling of
# diseases from different places that are unrelated to the CNV
with open('OMIM_genemap2.csv', 'r') as open_csv_3, open('../test.csv', 'r+', newline='') as open_csv_4:
    read_csv_2 = csv.reader(open_csv_3, delimiter='|')
    read_csv_3 = csv.reader(open_csv_4, delimiter='|')
    write_3 = csv.writer(open_csv_4, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    match = 0
    uqc = str(1)
    uqs = 10000
    uqe = 13000
    new_uqc = 'chr' + uqc
    for r in read_csv_3:
        for row in read_csv_2:
            # ignoring the lines that starts with '#' but not possible with blank lines
            if row[0].startswith('#'):
                continue
            # search for a specific term here where all the data input for the file is read line by line in this section
            if row[6] in r[18] and new_uqc == row[0]:
                print(row)
                match += 1
        # to do if genes have no phenotypes / diseases
        if match > 0:
            pass
        else:
            print('No matched found')
