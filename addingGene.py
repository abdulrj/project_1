import csv
import os
import numpy as np

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


# can also use forward slash on Windows as Python can accept this, which makes this to work on all platforms
with open('Nikita_gnomad_canonical_transcripts_new.csv', 'r') as open_csv, open('main_database.csv', 'r+', newline='') \
        as open_csv_2:
    read_csv = csv.reader(open_csv, delimiter='|')
    header_1 = next(read_csv, None)
    read_csv_2 = csv.reader(open_csv_2, delimiter='|')
    header_2 = next(read_csv_2, None)
    write_2 = csv.writer(open_csv_2, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # chromosome still the same, follows what the user queried
    for r in read_csv_2:
        uqc = str(r[0])
        uqs = r[1]
        uqe = r[2]
        genes = []
        # putting the reader back to the start of the file since after finishing the first iteration of the inner loop
        # the file reader offset will be placed at the end of the file, this happen as the iterators (inner for loop)
        # are exhausted after the first iteration
        open_csv.seek(0)
        for row in read_csv:
            gene_name = row[2]
            if uqc == str(row[3]):
                # can change / add to the code here and also the new defined function used here in the defining
                # above to determine whether the overlap is partial or full as right now both is define with the
                # same term so you can't differentiate between the to, it is useful to know when the CNV is deletion
                # just to check if it overlaps
                if range_overlapping(intervals_range(int(uqs), int(uqe)),
                                     intervals_range(int(row[4]), int(row[5]))) is True:
                    # calculating the overlap
                    overlap_len = overlap(int(uqs), int(uqe), int(row[4]), int(row[5]))
                    # can also add new formula to calculate the percentage of the gene that is overlap with query
                    # if it is partially overlap
                    # calculate the percentage of the input interval that overlap with the gene  where it is good to
                    # know the effect of duplication
                    r.append(row)
                    write_2.writerow(r)
    # putting the reader back to the start of the file since r+ will only write and update after finishing reading the
    # file, if not the output from writing will only be one line
    open_csv_2.seek(0)
