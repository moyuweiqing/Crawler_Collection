from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.action_chains import ActionChains # 鼠标悬浮
import time
import re
import pandas as pd

url = 'https://you.ctrip.com/sight/2020086/137991.html'

info_table = pd.DataFrame(columns=['旅游者类型', '昵称', '时间', '日期'])
row = 0
traveler_type = 1
ttype = {1: '家庭', 2: '夫妻', 3: '独自旅游', 4: '商务', 5: '好友'}
name = '广州长隆国际马戏大剧院'

# 滑动滑条，加载全部信息
def drop_down():
    for x in range(1, 11, 2):
        time.sleep(0.5)# 防止被预测到反爬
        h = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % h
        driver.execute_script(js)

def choose_type():
    # if traveler_type == 5:
    #     js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.5
    #     driver.execute_script(js)
    #     time.sleep(1)
    pre_xpath = '//*[@id="weiboCom1"]/div[1]/ul/li['
    type_xpath = pre_xpath + str(traveler_type) + ']'
    driver.find_element_by_xpath(type_xpath).click()

def get_data():
    global info_table, row
    a = driver.page_source
    html_tree = bs(a, 'lxml')
    names = html_tree.find_all('span', class_ = 'ellipsis')
    dates = html_tree.find_all('span', class_ = 'time_line')
    comments = html_tree.find_all('span', class_ = 'heightbox')

    for i in range(0, len(names)):
        alist = []
        alist.append(ttype[traveler_type])
        alist.append(names[i].get_text())
        alist.append(dates[i].get_text())
        alist.append(str(re.findall('[\u4e00-\u9fa5]+', str(comments[i]))).replace('[', '').replace(']', '').replace('\'', ''))
        info_table.loc[row] = alist
        row += 1

def choose_sort():
    # js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.5
    # driver.execute_script(js)
    # time.sleep(1)
    suspension = driver.find_element_by_css_selector("[class = 'gsn-select']")
    ActionChains(driver).move_to_element(suspension).perform()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="selectSort"]/ul/li[2]/a').click()

def next_page():
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.8
    driver.execute_script(js)
    driver.find_element_by_class_name('nextpage').click()
    time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="sightcommentbox"]/div[11]/div/a[7]').click()
    # js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.45
    # driver.execute_script(js)

if __name__ == '__main__':
    driver = webdriver.Chrome(r'D:\360极速浏览器下载\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    time.sleep(8)
    # choose_sort()
    for i in range(0, 5):
        choose_type()
        time.sleep(5)
        for j in range(0, 5):
            get_data()
            time.sleep(1)
            try:
                next_page()
                time.sleep(1)
            except:
                break
        traveler_type += 1

    info_table.to_csv(name + '.csv', encoding='gbk')