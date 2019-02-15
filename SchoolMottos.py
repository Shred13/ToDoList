# check to see the link is called school or institute in the ontario list of high schools
# if it is, see if the link works
# if it does, check to find motto and save that and use it

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

schools = []

url = "https://en.wikipedia.org/wiki/List_of_high_schools_in_Ontario"

uClient = urlopen(url)

content = uClient.read()
uClient.close()

soup = bs(content, 'html.parser')

findSchools = soup.findAll("ul")

findSchoolLinks = []
percentage = 0
for school in findSchools:
    try:
        findSchoolLinks.append(soup.findAll(school.li.a))
        percentage=percentage + 1/(len(findSchools))
        print (percentage, "% is done")
    except:
        print ("")

filterSchool = []

for x in findSchoolLinks:
    filterSchool.append(soup.findAll(attrs={'class':None}))


print (filterSchool)
