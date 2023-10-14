import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
response = requests.get(URL)

# print(response.text) -> Returns the entire HTML page as response.

# Parsing html response recieved
soup = BeautifulSoup(response.content, "html.parser")

# Finding elements by ID
results = soup.find(id="ResultsContainer")
print(type(results))

# Finding elements with class name
job_cards = results.find_all("div", class_="card-content")
for job_card in job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    # Extracting text from elements
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()


print("PYTHON JOBS ------------------------------------")

# Finding elements by specifiying a filtering criteria.
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

# Accessing the parent elements for a given element
python_jobs = [elem.parent.parent.parent for elem in python_jobs]

# Extracting attributes from HTML elements
for job in python_jobs:
    links = job.find_all("a")[1]["href"]
    print(links)