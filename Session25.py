                                     # WEB SCRAPPING....

import requests
from bs4 import BeautifulSoup

url = "https://www.indiatoday.in/sports"
response = requests.get(url)
#print(response.text)

soup = BeautifulSoup(response.text , "html.parser")

tags = soup.find_all("h3")

#tags = soup.find_all_next("div", class_="B1S3_content__wrap__9mSB6")

for tag in tags:
    print("````````````````````````````````")
    print(tag.text)
    print("````````````````````````````````")
    print()