import argparse
import csv
import os
import re

os.chdir(r'C:\Users\Acer\Desktop\P1\Datasets')

# create our Argument parser and set its description
parser = argparse.ArgumentParser()
parser.add_argument('-chr', '-chr', type=int, metavar='', help='chromosome to query')
parser.add_argument('-start', '-start', type=int, metavar='', help='start location to query')
parser.add_argument('-stop', '-stop', type=int, metavar='', help='stop location to query')
args = parser.parse_args()

uqc = args.chr
uqs = args.start
uqe = args.stop

# example of code to run in cmd: python query_cnv.py -chr 1 -start 1 -stop 10000


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


# def a new function similar to above for other information you want to extract

path = r'C:\Users\Acer\Desktop\P1'
fullpath = os.path.join(path, 'result.csv')
with open(fullpath, 'w', newline='') as open_output_csv, open('main_database.csv', 'r') as open_csv:
    read_csv = csv.reader(open_csv, delimiter='|')
    header = next(read_csv)
    sorted_csv = sorted(read_csv, key=lambda line: (line[0], line[1]), reverse=False)
    # data must be in list of strings or else the delimiter will be put between every character
    # using '|' as the delimiter in the csv to avoid confusion with fields that uses comma for multiple values
    write_1 = csv.writer(open_output_csv, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    write_1.writerow(header)
    match = 0
    for row in sorted_csv:
        if re.search(r'\b' + str(uqc) + r'\b', row[0]):
            # overlap define here is for both fully and partial overlap of the region queried by the user with the CNV
            if range_overlapping(intervals_range(int(uqs), int(uqe)),
                                 intervals_range(int(row[1]), int(row[2]))) is True:
                write_1.writerow(row)
                match += 1
    if match > 0:
        pass
    else:
        print('No matched found')
