# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

# This is a version with low efficiency
data = []
with open(DATAFILE,"r") as f:
    for i,line in enumerate(f):
        line_list = line.split(',')
        if i > 0:
            dic = {'Title':line_list[0],'UK Chart Position':line_list[3],'Label':line_list[2],\
                'Released':line_list[1],'US Chart Position':line_list[4],\
                    'RIAA Certification':line_list[6].split('\n')[0],'BPI Certification':line_list[5]}
            data.append(dic)
        if i > 10:
            break

# Let's improve it a little bit
### Important
# Python string method strip() will come in handy to get rid of the extra whitespace 
# (that includes newline character at the end of line)
data = []
with open(DATAFILE,"r") as f:
    head = f.readline().split(',')
    head[-1] = head[-1].split('\n')[0]
    for i,line in enumerate(f):
        line_list = line.split(',')
        dic = {}
        for j,col in enumerate(head):
            if col == 'RIAA Certification':
                dic[col] = line_list[j].split('\n')[0]
            else:
                dic[col] = line_list[j].strip()
        data.append(dic)
        if i > 10:
            break

# Add back to the function
def parse_file(datafile):
    data = []
    with open(DATAFILE,"r") as f:
        head = f.readline().split(',')
        head[-1] = head[-1].split('\n')[0]
        for i,line in enumerate(f):
            line_list = line.split(',')
            dic = {}
            for j,col in enumerate(head):
                if col == 'RIAA Certification':
                    dic[col] = line_list[j].split('\n')[0]
                else:
                    dic[col] = line_list[j].strip()
            data.append(dic)
            if i > 10:
                break
    return data

def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
    assert d[0] == firstline
    assert d[9] == tenthline

test()

