import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

Url = 'https://www.fifa.com/fifaplus/en/tournaments/mens/worldcup/qatar2022'

options = webdriver.EdgeOptions()
# 访问时不加载图片，加快访问速度
options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
browser = webdriver.Edge(options=options)
browser.implicitly_wait(10)
# 储存结果的容器
res = []
normal_res = []
penalty_res = []


def get_url():
    f = open('Url.txt', 'r', encoding='UTF-8')
    return f.readline()


# 获取所有赛程结果并保存
def get_result(url):
    # 访问官网获取比赛信息的网站
    browser.get(url)
    url = browser.find_element(By.XPATH, './/*[@id="mobileMainLinksID"]/div[1]/a').get_attribute('href')
    # 访问网站并爬取比赛信息
    browser.get(url)
    time.sleep(1)
    items = browser.find_elements(By.XPATH, './/*[@id="section-7eFcWpPHXL2i45S72sNWng"]/div/section/div/div[2]/div/div')
    time.sleep(1)
    for item in items:
        get_game(item)


# 获取每个赛程的信息
def get_game(item):
    global normal_res
    global penalty_res
    global res
    games = item.find_elements(By.XPATH, './div/div[2]/div')
    for game in games:
        re = item.find_element(By.XPATH, './div/div[1]').text.split('\n')
        data = game.text.split('\n')
        if data[-1][-9::] != 'penalties':
            re += data[0:4] + [None, None] + data[4:] + [None]
            normal_res.append(re)
        else:
            re += data
            penalty_res.append(re)
        res.append(re)


# 执行
get_result(get_url())
browser.quit()
# 保存至csv中方便分析

print(normal_res)
print(penalty_res)
print(res)

pd.DataFrame(normal_res).to_csv('normal_result.csv')
pd.DataFrame(penalty_res).to_csv('penalty_result.csv')
pd.DataFrame(res).to_csv('result.csv')
