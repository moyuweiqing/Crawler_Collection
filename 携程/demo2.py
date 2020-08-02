from selenium import webdriver
from bs4 import BeautifulSoup as bs
# from selenium.webdriver.common.action_chains import ActionChains # 鼠标悬浮
import time
import re
import pandas as pd

url = 'https://you.ctrip.com/sight/2020086/51027.html'

info_table = pd.DataFrame(columns = ['昵称', '时间', '评论'])

row = 0
name = '广州长隆飞鸟乐园很差评'

def get_data():
    global info_table, row
    a = driver.page_source
    html_tree = bs(a, 'lxml')
    names = html_tree.find_all('span', class_ = 'ellipsis')
    dates = html_tree.find_all('span', class_ = 'time_line')
    comments = html_tree.find_all('span', class_ = 'heightbox')

    for i in range(0, len(names)):
        alist = []
        # alist.append(ttype[traveler_type])
        alist.append(names[i].get_text())
        alist.append(dates[i].get_text())
        alist.append(str(re.findall('[\u4e00-\u9fa5]+', str(comments[i]))).replace('[', '').replace(']', '').replace('\'', ''))
        info_table.loc[row] = alist
        row += 1

def next_page():
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % 0.8
    driver.execute_script(js)
    driver.find_element_by_class_name('nextpage').click()
    time.sleep(1)

if __name__ == '__main__':
    driver = webdriver.Chrome(r'D:\360极速浏览器下载\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    time.sleep(8)
    for i in range(0, 2):
        get_data()
        time.sleep(1)
        try:
            next_page()
            time.sleep(1)
        except:
            break
    info_table.to_csv(name + '.csv', encoding='gbk')