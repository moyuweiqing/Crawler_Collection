from selenium import webdriver
import os
import time
import re
import pandas as pd
from bs4 import BeautifulSoup as bs

url = 'https://www.tripadvisor.cn/Attraction_Review-g298555-d2050559-Reviews-Chimelong_Birds_Park-Guangzhou_Guangdong.html#REVIEWS'
name = '长隆飞鸟乐园'

info_table = pd.DataFrame(columns=['旅行者类型', '昵称', '地区', '时间', '标题', '评论'])
page_number = 1
traver_type = 1
total_page = 0

# 展开
def release():
    elements = driver.find_elements_by_css_selector("[class='taLnk ulBlueLinks']")
    for element in elements:
        try:
            element.click()
            time.sleep(2)
            print('成功展开')
        except:
            print('展开失败')

def get_data(type_number):
    global total_page
    # print('typenumber:'+str(type_number))
    ttype = {1: '家庭', 2: '夫妻', 3: '独自旅游', 4: '商务', 5: '好友'}
    namelist = []
    loclist = []
    datelist = []
    titlelist = []
    commentlist = []

    # 名字和地区
    name = driver.find_elements_by_class_name('member_info')
    for i in range(0, len(name)):
        before = name[i].text
        after = before.split('\n')
        if len(after) == 1:
            after.append(' ')
        namelist.append(after[0])
        loclist.append(after[1])
    time.sleep(0.5)

    # 日期
    date = driver.find_elements_by_class_name('ratingDate')
    for i in range(0, len(date)):
        d = date[i].get_attribute('title')
        if(len(d) != 0):
            datelist.append(d)
    time.sleep(0.5)

    # 大标题
    title = driver.find_elements_by_class_name('noQuotes')
    for i in range(0, len(title)):
        titlelist.append(re.findall('[\u4e00-\u9fa5]+', title[i].text))

    # 评论
    comment = driver.find_elements_by_class_name('partial_entry')
    for i in range(2, len(comment)):
        commentlist.append(str(re.findall('[\u4e00-\u9fa5]+', comment[i].text)).replace('[', '').replace(']', '').replace('\'', ''))

    # 客服
    reback = driver.find_elements_by_class_name('mgrRspnInline')
    for i in range(0, len(reback)):
        r = reback[i].find_elements_by_class_name('partial_entry')
        rr = str(re.findall('[\u4e00-\u9fa5]+', r[0].text)).replace('[', '').replace(']', '').replace('\'', '')
        if rr in commentlist:
            commentlist.remove(rr)

    # print(ttype[type_number])
    for i in range(0, len(commentlist)):
        alist = [ttype[type_number]]
        alist.append(namelist[i])
        alist.append(loclist[i])
        alist.append(datelist[i])
        alist.append(str(titlelist[i]).replace('[', '').replace(']', '').replace('\'', ''))
        alist.append(str(commentlist[i]).replace('[', '').replace(']', '').replace('\'', ''))
        # print(index + i)
        info_table.loc[total_page] = alist
        total_page += 1

def choose_type():
    global traver_type
    h = 0.2
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % h
    driver.execute_script(js)
    time.sleep(0.3)

    pre = '//*[@id="taplc_detail_filters_ar_responsive_0"]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div['
    full = pre + str(traver_type) + ']/label'
    if traver_type == 1:
        driver.find_element_by_xpath(full).click()
        traver_type += 1
    else:
        driver.find_element_by_xpath(full).click()
        full = pre + str(traver_type - 1) + ']/label'
        time.sleep(1)
        driver.find_element_by_xpath(full).click()
        traver_type += 1

def next_page():
    global page_number
    if page_number == 1:
        try:
            driver.find_element_by_xpath('//*[@id="taplc_location_reviews_list_resp_ar_responsive_0"]/div/div[15]/div/div/a[2]').click()
            print('翻页成功')
            page_number += 1
            return True, page_number
        except:
            return False, page_number
    else:
        try:
            driver.find_element_by_xpath('//*[@id="taplc_location_reviews_list_resp_ar_responsive_0"]/div/div[14]/div/div/a[2]').click()
            print('翻页成功')
            page_number += 1
            return True, page_number
        except:
            return False, page_number

if __name__ == '__main__':
    driver = webdriver.Chrome(r'D:\360极速浏览器下载\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    for i in range(0, 5):
        choose_type()
        time.sleep(3)
        judge = True
        page = 1
        while judge:
            release() # 展开
            time.sleep(0.5)
            get_data(traver_type - 1)
            print('第'+str(page)+'页')
            j, page = next_page()
            judge = j
            time.sleep(8)
        print('最后一页')
        page_number = 1
        time.sleep(2)
    # if not os.path.exists('./results'):
    #     os.mkdir('./results')
    info_table.to_csv(name + '.csv', encoding='gbk')