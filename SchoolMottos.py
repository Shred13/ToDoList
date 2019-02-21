# check to see the link is called school or institute in the ontario list of high schools
# if it is, see if the link works
# if it does, check to find motto and save that and use it

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re

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
    percentage = (percentage+ 1/len(SchoolFilter))*100
    print(percentage)
    checker = str(school[1])
    reSchool = re.search("([ ]*[a-z]*)*[S|s][c][h][o][o][l]([ ]*[a-z]*)*", checker)
    reInstitute = re.search("([ ]*[a-z]*)*[I|i][n][s][t][i][t][u][t][e]([ ]*[a-z]*)*", checker)
    reAcademy = re.search("([ ]*[a-z]*)*[A|a][c][a][d][e][m][y]([ ]*[a-z]*)*", checker)
    reCollege = re.search("([ ]*[a-z]*)*[C|c][o][l][l][e][g][e]([ ]*[a-z]*)*", checker)
    reEcole = re.search("([ ]*[a-z]*)*[É|é][c][o][l][e]([ ]*[a-z]*)*", checker)

    if reSchool or reInstitute or reAcademy or reCollege or reEcole:
        finalList.append(school)



# for school in SchoolFilter:
#     checker = str(school[1]).split()
#     found = False
#     percentage = percentage + 1 / len(SchoolFilter)
#     print(percentage, "% is done")
#     while (not found):
#         for check in checker:
#
#             if check is "School":
#                 finalList.append(school)
#                 found = True

print(finalList)

#TODO DO IT BY SCHOOL BOARD (GO TO WEBSITE AND SEE IF IT EXISTS)