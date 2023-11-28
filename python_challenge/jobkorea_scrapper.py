from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

BASE_URL = "https://www.jobkorea.co.kr"

password = input("JobKorea ntoworks계정의 비번을 입력하세요")
keyword = input("검색어를 입력하세요: ")

"""
# WebDriver 인스턴스 생성
browser = webdriver.Chrome()  # 또는 Firefox, Safari 등

# 로그인 페이지로 이동
browser.get(f"{BASE_URL}/Login/Logout.asp")
"""

ff_options = FirefoxOptions()
ff_options.add_argument("--set-legacy")
ff_options.add_argument("--headless")
ff_options.add_argument("--disable-gpu")
ff_options.add_argument("--no-sandbox")  # Sandbox 비활성화
ff_options.add_argument("--disable-dev-shm-usage")  # /dev/shm 파티션 사용 비활성화

ff_service = FirefoxService(executable_path="/usr/local/bin/geckodriver")
browser = webdriver.Firefox(options=ff_options, service=ff_service)

browser.get(f"{BASE_URL}/Login/Logout.asp")


# 사용자 이름과 비밀번호 입력 필드 찾기
nameInput = browser.find_element(By.NAME, "M_ID")  # 'name' 속성에 따라 달라질 수 있음
pwdInput = browser.find_element(By.NAME, "M_PWD")  # 'name' 속성에 따라 달라질 수 있음
print("PASSWORD:", password)
nameInput.send_keys("ntoworks")
pwdInput.send_keys(password)

# 로그인 버튼 클릭
# login_button = driver.find_element(By.XPATH, "input[@type='submit']")
login_button = browser.find_element(By.CLASS_NAME, "btLoin")  # 'name' 속성에 따라 달라질 수 있음
login_button.click()

browser.get(f"{BASE_URL}/Corp/Person/Find")
txtKeyword = browser.find_element(By.ID, "txtKeyword")
txtKeyword.send_keys(keyword)

query_button = browser.find_element(By.CLASS_NAME, "btnKeywordSearch")
query_button.click()

soup = BeautifulSoup(browser.page_source, "html.parser")

tblSearchList = soup.find("table", class_="tblSearchList")
tbody = tblSearchList.find("tbody")
trList = tbody.find_all("tr")

candidates = []
for i in range(len(trList)):
    tr = trList[i]
    anchor = tr.find("a", class_="dvResumeLink")
    nameAge = tr.find("dd")
    careerLayer = tr.find("div", class_="careerLayer")
    career = careerLayer.find("dd").text.strip()
    nameAge = nameAge.text.strip()
    candidates.append({
        "name": anchor.text.strip(),
        "age": nameAge.replace(",", " "),
        "career": career.replace(",", " "),
        "link": f"{BASE_URL}{anchor['href']}"
    })

file = open(f"{keyword}.csv", "w", encoding="utf-8-sig")
file.write(f"{keyword}로 검색된 결과입니다.\n")
file.write("age, name, career, link\n")
for c in candidates:
    file.write(f"{c['name']}, {c['age']}, {c['career']}, {c['link']}\n")
file.close()

print(f"{keyword}.csv 에 저장되었습니다.")
