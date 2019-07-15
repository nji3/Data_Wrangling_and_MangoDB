import xlrd

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col) 
                for col in range(sheet.ncols)] 
                    for r in range(sheet.nrows)]

    print("\nList Comprehension")
    print("data[3][2]:",)
    print(data[3][2])

    print("\nCells in a nested loop:")    
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50:
                print(sheet.cell_value(row, col),)


    ### other useful methods:
    print("\nROWS, COLUMNS, and CELLS:")
    print("Number of rows in the sheet:",) 
    print(sheet.nrows)
    print("Type of data in cell (row 3, col 2):",) 
    print(sheet.cell_type(3, 2))
    print("Value in cell (row 3, col 2):",) 
    print(sheet.cell_value(3, 2))
    print("Get a slice of values in column 3, from rows 1-3:")
    print(sheet.col_values(3, start_rowx=1, end_rowx=4))

    print("\nDATES:")
    print("Type of data in cell (row 1, col 0):",) 
    print(sheet.cell_type(1, 0))
    exceltime = sheet.cell_value(1, 0)
    print("Time in Excel format:",)
    print(exceltime)
    print("Convert time to a Python datetime tuple, from the Excel float:",)
    print(xlrd.xldate_as_tuple(exceltime, 0))

    return data

data = parse_file(datafile)

#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


# Version When you do not know xlrd a lot
workbook = xlrd.open_workbook(datafile)
sheet = workbook.sheet_by_index(0)

col_names = [sheet.cell_value(0, c) for c in range(sheet.ncols)]
dic = {}
data = [[sheet.cell_value(r, c) for r in range(1,sheet.nrows)] for c in range(sheet.ncols)]
for i in range(len(col_names)):
    dic[col_names[i]] = data[i]

# When you know xlrd well, you could extract the col values by this way
coast = sheet.col_values(1,start_rowx=1,end_rowx=None)
coast_min_idx = dic['COAST'].index(min(dic['COAST'])) + 1
coast_max_idx = dic['COAST'].index(max(dic['COAST'])) + 1
maxtime = xlrd.xldate_as_tuple(sheet.cell_value(coast_max_idx,0), 0)
mintime = xlrd.xldate_as_tuple(sheet.cell_value(coast_min_idx,0), 0)

data = {
        'maxtime': maxtime ,
        'maxvalue': max(dic['COAST']),
        'mintime': mintime,
        'minvalue': min(dic['COAST']),
        'avgcoast': sum(dic['COAST'])/float(len(dic['COAST']))
}


def parse_file2(datafile):
    
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    coast = sheet.col_values(1,start_rowx=1,end_rowx=None)
    coast_min_idx = coast.index(min(coast)) + 1
    coast_max_idx = coast.index(max(coast)) + 1
    maxtime = xlrd.xldate_as_tuple(sheet.cell_value(coast_max_idx,0), 0)
    mintime = xlrd.xldate_as_tuple(sheet.cell_value(coast_min_idx,0), 0)

    data = {
        'maxtime': maxtime ,
        'maxvalue': max(coast),
        'mintime': mintime,
        'minvalue': min(coast),
        'avgcoast': sum(coast)/float(len(coast))
    }

    return data


def test():
    open_zip(datafile)
    data = parse_file2(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()