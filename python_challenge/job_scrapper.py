from requests import get
import json
from bs4 import BeautifulSoup

print('=====================================')
print('          JOB SCRAPPER')
print('=====================================')

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = 'backend'

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("request failed")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    sections = soup.find_all("section", class_="jobs")
    allJobs = []
    for section in sections:
        jobs = section.find_all('li')
        jobs.pop(-1) # 리스트의 마지막 항목 삭제, 실제 View-all 버튼 삭제함
        for job in jobs:
            _anchorHref = ''
            anchors = job.find_all('a')
            if len(anchors) > 1:
                anchor = anchors[1]
                _anchorHref = anchor['href']
                
                companies = anchor.find_all('span', class_='company')
                company, position, region_company = companies
                title = anchor.find('span', class_='title')
                job_data = {
                    "title": title.string, 
                    "position": position.string,
                    "link": _anchorHref,
                    "region": region_company.string
                }
                allJobs.append(job_data)
    print(json.dumps(allJobs, indent=2))
                
                
            
