# check to see the link is called school or institute in the ontario list of high schools
# if it is, see if the link works
# if it does, check to find motto and save that and use it

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import json

schools = []
url = "https://en.wikipedia.org/wiki/List_of_high_schools_in_Ontario"

uClient = urlopen(url)

content = uClient.read()
uClient.close()

soup = bs(content, 'html.parser')

findSchools = soup.findAll("ul")

findSchoolLinks = []
# percentage = 0
for school in findSchools:
    try:
        findSchoolLinks.append(school.findAll('a'))
    #      percentage=percentage + 1/(len(findSchools))
    #       print (percentage, "% is done")
    except:
        print("")

# TODO CHECK IF THERE ARE CERTAIN TAGS FOR EACH SCHOOL LINK OR SUCH
# TODO MAYBE A CERTAIN KIND OF ATTR OR CSS CLASS?

SchoolURL = []
for school in findSchoolLinks:
    for school2 in school:
        SchoolURL.append((school2['href'], school2.string))

SchoolFilter = []
for school in SchoolURL:
    if school[0][-1] is not "1":
        SchoolFilter.append(school)

finalList = []

percentage = 0

for school in SchoolFilter:
    percentage = (percentage+ (1/len(SchoolFilter)*100))
    print(percentage)
    checker = str(school[1])
    reSchool = re.search("([ ]*[a-z]*)*[S][c][h][o][o][l]([ ]*[a-z]*)*", checker)
    reInstitute = re.search("([ ]*[a-z]*)*[I][n][s][t][i][t][u][t][e]([ ]*[a-z]*)*", checker)
    reAcademy = re.search("([ ]*[a-z]*)*[A][c][a][d][e][m][y]([ ]*[a-z]*)*", checker)
    reCollege = re.search("([ ]*[a-z]*)*[C][o][l][l][e][g][e]([ ]*[a-z]*)*", checker)
    reEcole = re.search("([ ]*[a-z]*)*[É][c][o][l][e]([ ]*[a-z]*)*", checker)

    if reSchool or reInstitute or reAcademy or reCollege or reEcole:
        finalList.append(school)
print(finalList)

with open("data_file.json", "w") as write_file:
    json.dump(finalList, write_file)

# with open("mottos.txt", "wb") as fp:   #Pickling
#     pickle.dump(finalList, fp)

print("hello")

