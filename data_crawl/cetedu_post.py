from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from openpyxl import Workbook

# import pandas as pd


if __name__ == '__main__':
    workbook = Workbook()
    workbook.create_sheet('main')

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)

    with open('food_article_url.txt', 'r') as urls:
        for url in urls:
            if url.startswith('http'):
                browser.get(url)

                # Wait for JavaScript to execute (you can adjust the wait time based on your needs)
                browser.implicitly_wait(10)

                html = BeautifulSoup(browser.page_source, 'html.parser')
                description = ' '
                try:
                    description = html.select_one('#ftwp-postcontent > div:nth-child(1) > p:nth-child(1) > em').text.strip()
                except AttributeError:
                    description = ''

                content = html.select_one('#ftwp-postcontent').find('div')
                if content.find_all('div'):
                    for e in content.find_all('div'):
                        e.extract()
                if content.find_all('style'):
                    for e in content.find_all('style'):
                        e.extract()
                if content.find_all('a'):
                    for e in content.find_all('a'):
                        e.extract()
                content_ = content.contents
                content = ' '
                for c_ in content_:
                    content += c_.__str__()
                row_data = [url.replace('\n', ''), description.replace('\n', ' '), content.replace('\n', ' ')]
                print(row_data)
                workbook['main'].append(row_data)

    workbook.save('food_article_url.xlsx')
