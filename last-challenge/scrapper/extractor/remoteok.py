from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
중요중요!!!!
requests로 작업하려고 하였으나 503오류가 계속 발생하여 부득이 selenium
으로 작업하였습니다.
replit에서는 chromedriver 문제로 인해 정상 동작하지 않지만 로컬에서는
동작을 확인하였습니다.
"""
def extract_remoteok_jobs_w_requests(keyword):
    print('=====================================')
    print('    RemoteOK JOB SCRAPPER')
    print('=====================================')

    allJobs = [];

    base_url = "https://remoteok.com/remote-"
    url = f"{base_url}{keyword}-jobs"

    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print(f"request failed {response.status_code}")
    else:
        soup = BeautifulSoup(browser.page_source, "html.parser")

        jobTrs = soup.find_all("tr", class_="job")
        for jobTr in jobTrs:
            companyTd = jobTr.find('td', class_="company")
            anchor = companyTd.find('a', class_="preventLink")
            link = anchor['href']
            h2 = anchor.find('h2')
            title = h2.string
            companySpan = companyTd.find('span', class_="companyLink")
            h3 = companySpan.find('h3')
            company = h3.string

            job = {
                "company": company,
                "title": title,
                "link": link
            }
            allJobs.append(job)
    return allJobs

def extract_remoteok_jobs(keyword):
    print('=====================================')
    print('    RemoteOK JOB SCRAPPER')
    print('=====================================')

    allJobs = [];

    base_url = "https://remoteok.com/remote-"
    url = f"{base_url}{keyword}-jobs"

    options = Options()

    options.add_argument("--set-legacy")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox") 
    options.add_argument("--disable-dev-shm-usage") 
    browser = webdriver.Chrome(options=options)

    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "html.parser")

    jobTrs = soup.find_all("tr", class_="job")
    for jobTr in jobTrs:
        companyTd = jobTr.find('td', class_="company")
        anchor = companyTd.find('a', class_="preventLink")
        link = anchor['href']
        h2 = anchor.find('h2')
        title = h2.string
        companySpan = companyTd.find('span', class_="companyLink")
        h3 = companySpan.find('h3')
        company = h3.string

        job = {
            "position": company,
            "title": title,
            "link": link
        }
        allJobs.append(job)
    # return allJobs
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


# jobs = extract_remoteok_jobs("ruby")
