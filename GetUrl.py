import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
# 访问时不加载图片，加快访问速度
options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
browser = webdriver.Edge(options=options)
browser.implicitly_wait(10)

browser.get('https://cn.bing.com/')
browser.find_element(By.XPATH, './/*[@id="sb_form_q"]').send_keys('FIFA World Cup 2022')
browser.find_element(By.XPATH, './/*[@id="sb_form_q"]').send_keys(Keys.ENTER)
time.sleep(3)
Urls = browser.find_elements(By.XPATH, './/a[@class="tilk"]//cite')
f = open('Url.txt', 'w', encoding='UTF-8')
for url in Urls:
    f.write(url.text)
    f.write('\n')
f.close()
