import requests

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50&start=0")

# print(indeed_result)
print(indeed_result.text)