from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
brightStarsUrl = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(brightStarsUrl)
print(page)
soup = bs(page.text, 'html.parser')
starTable = soup.find('table')
tempList = []
tableRows = starTable.find_all('tr')
for tr in tableRows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)
starNames = []
distance = []
mass = []
radius = []
lum = []
for i in range(1, len(tempList)):
    starNames.append(tempList[i][1])
    distance.append(tempList[i][3])
    mass.append(tempList[i][5])
    radius.append(tempList[i][6])
    lum.append(tempList[i][7])
df2 = pd.DataFrame(list(zip(starNames, distance, mass, radius, lum)), columns = ['Star name', 'Distance', 'Mass', 'Radius', 'Luminosity'])
print(df2)
df2.to_csv('brightStars.csv')