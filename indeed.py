import requests
from bs4 import BeautifulSoup

LIMIT=3
LAST_PAGE = 1
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"

def extract_indeed_pages():  
  indeed_result = requests.get(URL)
  indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

  pagination = indeed_soup.find("div", {"class": "pagination"})
  links = pagination.find_all("a")

  pages = []

  for link in links[:-1]:
      pages.append(int(link.find("span").string))
  last_page = pages[-1]-5+LAST_PAGE

  return last_page
  
  # range(s,n)   : 숫자n부터 시작하는 n개 수모임
  # range(0,5)   : 0부터시작하는 5개
  # 0 1 2 3 4
def extract_indded_jobs(last_page):
  jobs=[]
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
    for result in results:
      title = result.find("h2",{"class":"title"}).find("a")["title"]
      company = result.find("span",{"class":"company"})
      company = company.string

      print(title, company)

  return jobs
  
