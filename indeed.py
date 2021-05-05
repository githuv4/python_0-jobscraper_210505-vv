import requests
import os
from bs4 import BeautifulSoup

os.system("clear")

LIMIT = 50
LAST_PAGE = 20
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"


def extract_indeed_pages():
    indeed_result = requests.get(URL)
    indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

    pagination = indeed_soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.find("span").string))
    last_page = pages[-1] - 5 + LAST_PAGE

    return last_page


def extract_job(html):
    title_a = html.find("h2", {"class": "title"}).find("a")
    title = title_a["title"]
    company_span = html.find("span", {"class": "company"})
    if company_span == None:
      company=" "
    else:
      company = company_span.string
    
    # print(title,":",company)

    location = html.find("span", {"class": "location"})
    location = location.string
    job_href = title_a["href"]
    # job_id = html["data-jk"]
    # job_id = html["id"]
    # print(f"https://kr.indeed.com{job_href}")
    return {
        'title': title,
        'company': company,
        'location': location,
        # "link": f"https://kr.indeed.com/viewjob?jk={job_id}"
        "link": f"https://kr.indeed.com{job_href}"
    }

# https://kr.indeed.com/viewjob?jk={job_id}
# https://kr.indeed.com/viewjob?jk=5d586ea25719e960

# range(s,n)   : 숫자n부터 시작하는 n개 수모임
# range(0,5)   : 0부터시작하는 5개
# 0 1 2 3 4
def extract_indded_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs
