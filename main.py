import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50&start=0")

indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

pagination = indeed_soup.find("div",{"class":"pagination"})
links = pagination.find_all("a")

spans = []

for link in links[:-1]:
  spans.append(int(link.find("span").string))
last_page = spans[-1]
print(spans)
print(last_page)


