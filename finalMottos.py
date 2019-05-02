#      Load the list back from the pickle file.


import json
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen


with open('/Users/shreyanshanand/venv/Random/data_file.json', 'r') as f:
    schools = json.load(f)


mottos = []


for links in schools:
 # look for motto here and append to mottos
    url = "https://en.wikipedia.org" + links[0]
    uClient = urlopen(url)
    content = uClient.read()
    uClient.close()
    soup = bs(content, 'html.parser')
    try:
        mottos.append((links[1], "`", soup.find("th", string="Motto").parent.contents[1].text))
# finds the th in the table with the string of Motto, and then goes up the tree once
# to its parent, and then finds the second child (so basically the sibling for the
# th, and then takes its text.
    except:
        print(links[1])

print(mottos)

file_creation = open("final_mottoes.txt", "w+")
for motto in mottos:
    file_creation.write(str(motto)[2:-2])
    file_creation.write("\n")

# todo then looks for the mottos and then appends them to a list which is then pickled back into another file



