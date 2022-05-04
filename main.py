import requests
from bs4 import BeautifulSoup

URL = "https://weworkremotely.com/"

response = requests.get(URL)
website_html = response.text


soup = BeautifulSoup(website_html, "html.parser")

all_jobs = soup.find_all(name="span", class_="title")
print(all_jobs)

job_titles = [job.getText() for job in all_jobs]
jobs = job_titles[::-1]
print(jobs)

with open("jobs.txt", mode="w") as file:
    for job in jobs:
        file.write(f"{job}\n")