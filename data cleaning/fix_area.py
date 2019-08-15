"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the
"areaLand" field, you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it
has to return a float representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you
like, but changes to process_file will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'


def fix_area(area):
    # YOUR CODE HERE
    if area != '' and area != 'NULL':
        try:
            area = float(area)
        except ValueError:
            split = area.split('|')
            if len(set(split[0])) > len(set(split[1])):
                area = float(split[0].split('{')[1])
            else:
                area = float(split[1].split('}')[0])
    else:
        area = None
    return area



def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #skipping the extra metadata
        # processing file
        for i,line in enumerate(reader):
            if i > 2:
                # calling your function to fix the area value
                if "areaLand" in line:
                    line["areaLand"] = fix_area(line["areaLand"])
                data.append(line)
    return data


def test():
    data = process_file(CITIES)
    print("Printing three example results:")
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])
    assert data[3]["areaLand"] == None        
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0    


if __name__ == "__main__":
    test()