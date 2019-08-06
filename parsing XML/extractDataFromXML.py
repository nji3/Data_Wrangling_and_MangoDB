## Extract the infromation you want in general
import xml.etree.ElementTree as ET

# 1. get the elementTree root and show the children, so that you could have
# better idea about the structure of the data store in this .xml file
article_file = "exampleResearchArticle.xml"
tree = ET.parse(article_file)
root = tree.getroot()

print('\nChildren of root: ')
for child in root:
    print(child.tag) # Tag of each part of the data file

# 2. extract the specific content we want from the .xml file by
# specifying the content location and read them
# Find the bibl titles
title = root.find('./fm/bibl/title')
title_txt = ""
for t in title:
    title_txt += t.text
print("\nTitle:\n",title_txt)

# Extract the date in the history
print('\nThe date in the history:')
for d in root.findall('./fm/history/rec/date'):
    day = d.find('day')
    month = d.find('month')
    year = d.find('year')
    print(month.text+'-'+day.text+'-'+year.text)

#!/usr/bin/env python
# Your task here is to extract data from xml on authors of an article
# and add it to a list, one item for an author.
# See the provided data structure for the expected format.
# The tags for first name, surname and email should map directly
# to the dictionary keys
import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None
        }
        # YOUR CODE HERE
        data['fnm'] = author.find('fnm').text
        data['snm'] = author.find('snm').text
        data['email'] = author.find('email').text
        authors.append(data)
    return authors


def test():
    solution = [{'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'}, {'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'}, {'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'}, {'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'}, {'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'}, {'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'}, {'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'}, {'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]
    root = get_root(article_file)
    data = get_authors(root)
    assert data[0] == solution[0]
    assert data[1]["fnm"] == solution[1]["fnm"]


test()

#!/usr/bin/env python
# Your task here is to extract data from xml on authors of an article
# and add it to a list, one item for an author.
# See the provided data structure for the expected format.
# The tags for first name, surname and email should map directly
# to the dictionary keys, but you have to extract the attributes from the "insr" tag
# and add them to the list for the dictionary key "insr"
import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"

def get_authors2(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None,
                "insr": []
        }
        # YOUR CODE HERE
        data['fnm'] = author.find('fnm').text
        data['snm'] = author.find('snm').text
        data['email'] = author.find('email').text
        for insr in author.findall('insr'):
            data['insr'].append(insr.attrib['iid'])
        authors.append(data)
    return authors


def test2():
    solution = [{'insr': ['I1'], 'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'},
                {'insr': ['I2'], 'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'},
                {'insr': ['I3', 'I4'], 'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'},
                {'insr': ['I3'], 'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'},
                {'insr': ['I8'], 'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'},
                {'insr': ['I3', 'I5'], 'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'},
                {'insr': ['I6'], 'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'},
                {'insr': ['I7'], 'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]
    root = get_root(article_file)
    data = get_authors2(root)
    assert data[0] == solution[0]
    assert data[1]["insr"] == solution[1]["insr"]


test2()