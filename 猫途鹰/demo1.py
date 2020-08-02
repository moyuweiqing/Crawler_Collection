from selenium import webdriver
import pandas as pd
import re
import os
import time
import pandas as pd

url = 'https://www.tripadvisor.cn/Attraction_Review-g298555-d2050559-Reviews-Chimelong_Birds_Park-Guangzhou_Guangdong.html#REVIEWS'
page = 1
doc_name = '长隆飞鸟乐园'
traver_type = 1

info_table = pd.DataFrame(columns=['旅行者类型', '昵称', '地区', '时间', '标题', '评论'])
page_change = True

def get_loc(loc):
    local = driver.find_elements_by_class_name(loc)
    return local.text

def get_data(index):
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

    for i in range(0, 8):
        alist = ['独自旅游']
        alist.append(namelist[i])
        alist.append(loclist[i])
        alist.append(datelist[i])
        alist.append(str(titlelist[i]).replace('[', '').replace(']', '').replace('\'', ''))
        alist.append(str(commentlist[i]).replace('[', '').replace(']', '').replace('\'', ''))
        # print(index + i)
        info_table.loc[index + i] = alist

def next_page():
    global page_change
    if page_change:
        driver.find_element_by_xpath('//*[@id="taplc_location_reviews_list_resp_ar_responsive_0"]/div/div[15]/div/div/a[2]').click()
        page_change = False
    else:
        driver.find_element_by_xpath('//*[@id="taplc_location_reviews_list_resp_ar_responsive_0"]/div/div[14]/div/div/a[2]').click()


def choose_type():
    pre = '//*[@id="taplc_detail_filters_ar_responsive_0"]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div['
    full = pre + str(traver_type) + ']/label'
    # driver.find_element_by_xpath('//*[@id="taplc_detail_filters_ar_responsive_0"]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/label').click()
    driver.find_element_by_xpath(full).click()


if __name__ == '__main__':
    driver = webdriver.Chrome(r'D:\360极速浏览器下载\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    # time.sleep(2)
    choose_type()
    time.sleep(0.5)
    # get_data(0)
    # time.sleep(0.5)
    for i in range(0, page):
        get_data(i * 10)
        time.sleep(0.5)
        # next_page()
        print('已完成'+str(i + 1)+'页')
        time.sleep(0.5)
    if not os.path.exists('./results'):
        os.mkdir('./results')
    info_table.to_csv('./results/' + doc_name + '-' + str(traver_type) + '.csv', encoding='gbk')