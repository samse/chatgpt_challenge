import json
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
selenium 설치
pip3 install selenium
brew install chromedriver

브라우저 드라이버 설치
 크롬 : https://sites.google.com/a/chromium.org/chromedriver/downloads 
 파이어폭스 : https://github.com/mozilla/geckodriver/releases
 사파리 : https://webkit.org/blog/6900/webdriver-support-in-safari-10/
 
 맥은 크롬드라이버를 brew로 설치
 brew install chromedriver
"""

# 키워드로 indeed 사이트 일감목록 조회하기
def extract_indeed_jobs(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    query_offset = 50
    print_guide(base_url, keyword)

    allJobs = [];
    options = Options()
    start = 0

    # sandbox 보안기능을 disable함. 보안때문에 스크래핑이 안되는 경우를 막기 위함인듯 함. for replit
    options.add_argument("--no-sandbox") 
    # 공유메모리 공간의 사용을 disable함. 메모리 사용량의 폭주를 막기 위함. for replit
    options.add_argument("--disable-dev-shm-usage") 
    
    browser = webdriver.Chrome(options=options)

    browser.get(f"{base_url}{keyword}&limit={query_offset}&start={start}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    page_count = get_pages(soup)
    print(f"total pages: {page_count}")

    for i in range(page_count):
        if (i!=0):
            start = start + query_offset
            url = f"{base_url}{keyword}&limit={query_offset}&start={start}"
            print(f"url: {url}")
            browser.get(url)
            soup = BeautifulSoup(browser.page_source, "html.parser") 
        get_jobs(soup, allJobs)

    print(f"all Jobs count is {len(allJobs)}")
    # print_all_jobs(allJobs)
    # for j in allJobs:
    #     print(json.dumps(j, indent=2))
    return allJobs

def print_all_jobs(allJobs):
    for i in range(len(allJobs)):
        job = allJobs[i]
        print(f"({i+1}) {job['title']}\n")
    # for job in allJobs:
    #     print(f"{job['title']}\n")


# 조회된 결과로 페이지 수 가져오기
def get_pages(soup):
    pages = 0
    nav = soup.find('nav', attrs={"aria-label": "pagination"})
    if nav == None:
        return 1
    else:
        anchors = nav.find_all('a')
        for anchor in anchors:
            if (anchor["data-testid"] != "pagination-page-next"):
                pages = pages+1
    # navs = soup.find_all('nav')
    # for nav in navs:
    #     area_label = nav["aria-label"]
    #     if ( area_label != None and area_label == "pagination"):
    #         anchors = nav.find_all('a')
    #         for anchor in anchors:
    #             if (anchor["data-testid"] != "pagination-page-next"):
    #                 pages = pages+1
    return 1 if pages==0 else pages

# 조회된 결과로 일감가져와서 전체 목록에 추가하기
def get_jobs(soup, allJobs):
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

# 타이틀 출력
def print_guide(base_url, keyword):
    print('=====================================')
    print('    Indeed JOB SCRAPPER')
    print(f"{base_url}{keyword}")
    print('=====================================')


# jobs = extract_indeed_jobs('python')
# print(json.dumps(jobs, indent=2))

