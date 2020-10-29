from requests_html import HTMLSession
from bs4 import BeautifulSoup


session = HTMLSession()

url = "https://www.airnow.gov/?city=Daly%20City&state=CA&country=USA"


r = session.get(url)

r.html.render(sleep=1, keep_page=True, scrolldown=1)

aqis = r.html.find('.pollutant-info-heading')

for aqi in aqis:
    print(aqi.text, end="\n \n \n")
