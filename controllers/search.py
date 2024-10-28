import requests
from bs4 import BeautifulSoup


def run_search(query: str):
    url = f"https://www.bing.com/search?q={query}"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('li', class_='b_algo')

    search_results = []
    for counter, result in enumerate(results):
        title = result.find('h2').text
        link = result.find('a')['href']
        search_results.append({
            "rank": counter + 1,
            "title": title,
            "link": link
        })
    
    return search_results