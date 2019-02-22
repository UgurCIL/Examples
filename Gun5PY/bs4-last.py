import json
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

def scrap_website(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    main_content = soup.find('div', {'id': 'user-repositories-list'})

    list_of_repos = main_content.findAll('li')

    results = []

    for repo in list_of_repos:
        repository = {}

        repository["name"] = repo.a.string.strip()

        base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
        repository["link"] = "{0}{1}".format(base_url, repo.a.get('href'))

        if repo.p and repo.p.string:
            repository["description"] = repo.p.string.strip()

        else:
            repository["description"] = "No description available for this repository."

        programming_language = soup.find(attrs={"itemprop": "programmingLanguage"}).string.strip()
        repository["programming_language"] = programming_language
        results.append(repository)

    return results

print(json.dumps(scrap_website("https://github.com/gvanrossum?tab=repositories"), indent=4))

parsed_uri = urlparse("https://github.com/gvanrossum?tab=repositories")
result = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
print(result)
