from selenium import webdriver
from selenium.webdriver.common.by import By
import time

results = []


def get_TH(url):
    browser = webdriver.Edge()
    browser.get(url)
    time.sleep(0.5)
    print(browser.find_element(By.XPATH, r'//*[@id="table_main"]').text)
    browser.quit()


def get_column(res, n):
    list = []
    for x in res:
        list.append(x[n])
    return list


url = 'https://data.stats.gov.cn/easyquery.htm?cn=E0102'

get_TH(url)
# labels = get_column(results, 0)
# fourth = get_column(results, 1)
# third = get_column(results, 2)
# second = get_column(results, 3)
# first = get_column(results, 4)
# print(labels)