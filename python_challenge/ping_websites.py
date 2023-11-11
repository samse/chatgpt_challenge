import requests
import json

websites = [
  "google.com",
  "facebook.com",
  "https://airbnb.com",
  "https://www.ntoworks.com"
]
results = {}
for website in websites:
  if not website.startswith("https"):
      website = f"https://{website}"
  response = requests.get(website)
  if response.status_code == 200:
    results[website] = "OK"
  else:
    results[website] = "FAILED"

print(json.dumps(results, indent=2))
