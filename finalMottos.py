  # Load the list back from the pickle file.

import pickle
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

schools = pickle.load(open("SchoolMottos.txt", "rb"))

print(schools)

mottos = []
# for links in schools:
#     url = "https://en.wikipedia.org" + links[0]
#     uClient = urlopen(url)
#     content = uClient.read()
#     uClient.close()
#
#     soup = bs(content, 'html.parser')
    # look for motto here and append to mottos



# todo then looks for the mottos and then appends them to a list which is then pickled back into another file

# below is some tests to see if i can find it
url = "https://en.wikipedia.org" + schools[0][1]
uClient = urlopen(url)
content = uClient.read()
uClient.close()

soup = bs(content, 'html.parser')

find_t_body = soup.find("tbody")

