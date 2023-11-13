import json
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_indeed_jobs(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    print('=====================================')
    print('    Indeed JOB SCRAPPER')
    print(f"{base_url}{keyword}")
    print('=====================================')

    allJobs = [];
    options = Options()
    options.add_argument("--no-sandbox") # for replit
    options.add_argument("--disable-dev-shm-usage") # for replit
    
    browser = webdriver.Chrome(options=options)
    browser.get(f"{base_url}{keyword}&limit=50")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find("ul", class_="css-zu9cdh")
    jobs = job_list.find_all('li', recursive=False)
    for job in jobs:
        zone = job.find('div', class_="mosaic-zone")
        if zone == None:
            titleAnchor = job.find('a', class_="jcs-JobTitle")
            link = titleAnchor['href']
            title = titleAnchor.find('span')
            locDiv = job.find('div', class_="company_location")
            company = locDiv.find('span')
            location = locDiv.find(attrs={"data-testid":"text-location"})
            posDiv = job.find('div', class_="salaryOnly")
            position = "없음"
            if posDiv != None:           
                pos = posDiv.find(attrs={"data-testid":"attribute_snippet_testid"})
                if pos != None and pos.string != None:
                    position = pos.string
            
            # print('position', position, " >> 없음" if position == None else position.string)

            allJobs.append({
                "title": title.string, 
                "company": company.string,
                "position": position,
                "link": f"https://kr.indeed.com/jobs{link}",
                "region": location.string
            })
    for j in allJobs:
        print(json.dumps(j, indent=2))

jobs = extract_indeed_jobs('python')
# print(json.dumps(jobs, indent=2))
