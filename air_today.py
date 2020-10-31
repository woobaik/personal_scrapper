from requests_html import HTMLSession
from bs4 import BeautifulSoup


session = HTMLSession()

url = "https://www.airnow.gov/?city=Daly%20City&state=CA&country=USA"
r = session.get(url)

r.html.render(sleep=1, keep_page=True, scrolldown=1)

aqis = r.html.find('.pollutant-info-heading')

result = []
for aqi in aqis:
    result.append(aqi.text)
print("=======================================================")
for row in result:
    new_row = row.split('\n')
    print(f"Currently, {new_row[0]} is {new_row[1]}, which is {new_row[2]}.")
print("=======================================================")
