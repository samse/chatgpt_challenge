from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    print('=====================================')
    print('    WeworkRemotely JOB SCRAPPER')
    print('=====================================')

    base_url = "https://weworkremotely.com/remote-jobs/search?term="

    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("request failed")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        sections = soup.find_all("section", class_="jobs")
        allJobs = []
        for section in sections:
            jobs = section.find_all('li')
            if len(jobs) > 0:
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
                    print(f"{job_data}")
                    allJobs.append(job_data)
        result = "["
        for c in allJobs:
            result = result + "{"
            result = result + f" \"title\": \"{c['title']}\","
            result = result + f" \"position\": \"{c['position']}\","
            result = result + f" \"link\": \"{c['link']}\""
            result = result + "}, \n"
        result = result + "]"
        print(result)
        return result
                    
                    
            