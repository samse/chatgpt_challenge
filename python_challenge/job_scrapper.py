from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
import json

# jobs = extract_wwr_jobs('python')
jobs = extract_indeed_jobs('python')
print(json.dumps(jobs, indent=2))


