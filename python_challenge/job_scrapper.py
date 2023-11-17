from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from extractors.indeed import print_all_jobs
import json

keyword = input("검색어를 입력하세요: ")
wwr = extract_wwr_jobs(keyword)
indeed = extract_indeed_jobs(keyword)

jobs = indeed + wwr

print_all_jobs(jobs)

# print(json.dumps(jobs, indent=2))


