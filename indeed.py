import urllib.request
web = "https://www.indeed.ca/viewjob?jk=187606f78ce76232&tk=1d9fuv16h1fqs003&from=serp&vjs=3"
page = urllib.request.urlopen(web)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page,"html.parser")
print("")

print("TITLE:")
print(soup.title.string)

print("")
print("COMPANY NAME:")
cmpny=soup.find('div',class_='icl-u-lg-mr--sm icl-u-xs-mr--xs')
print(cmpny.string)

print("")
print("LOCATION:")
loc=soup.find('span',class_='jobsearch-JobMetadataHeader-iconLabel')
print(loc.string)

print("")
print("
CONTENT AND SKILLS(tech_tags):")
content=soup.find('div',class_='jobsearch-jobDescriptionText')
print(content.get_text())
