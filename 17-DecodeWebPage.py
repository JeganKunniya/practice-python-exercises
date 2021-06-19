# Exercise 17 - Decode a web page https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
from bs4 import BeautifulSoup


def print_all_titles_from_nyt():
    """
    Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the
    New York Times homepage.

    Crawl the page and find the element that holds the article title.
    """
    nyt_url = 'https://www.nytimes.com/'
    response = requests.get(nyt_url)
    soup = BeautifulSoup(response.text, 'lxml')
    page_elements = soup.find_all('h3')
    for element in page_elements:
        if len(element.attrs) > 0 and len(element.attrs['class']) > 0 and 'e1lsht870' in element.attrs['class']:
            print(element.text)


if __name__ == '__main__':
    print_all_titles_from_nyt()
