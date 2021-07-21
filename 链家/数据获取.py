# 导入相关库
import requests
import pandas as pd
import re
import os
from bs4 import BeautifulSoup as bs
import time

# 定义数据标准化函数
def getIntoPage(url, info_table, row_num):
    page_source = requests.get(url).text
    html_text = bs(page_source, 'lxml')
    home_names = html_text.find_all('a', class_ = 'twoline')
    price_list = html_text.find_all('span', class_ = 'content__list--item-price')
    msg_list = html_text.find_all('p', class_ = 'content__list--item--des')
    labels = html_text.find_all('p', class_ = 'content__list--item--bottom oneline')
    for i in range(0, len(home_names)):
        alist = []
        alist.append(home_names[i].text)
        alist.append(price_list[i].text)
        msg_sub_list = msg_list[i].text.split('/')
        for sub_msg in msg_sub_list:
            alist.append(sub_msg)

        while len(alist) < 7:
            alist.append('')
        alist.append(labels[i].text)
        info_table.loc[row_num] = alist
        row_num += 1
    return row_num

def parse(English, Chinese, page):
    try:
        # 定义变量，表格和行数
        info_table = pd.DataFrame(columns=['名称', '租金', '地址', '面积', '朝向', '房间组成', '楼层', '标签'])
        row_num = 0
        url_head = 'https://bj.lianjia.com/zufang/' + English + '/pg'
        # url_head = 'https://bj.lianjia.com/zufang/pg'
        for page in range(1, page ):
            url = url_head + str(page) + '/#contentList'
            row_num = getIntoPage(url, info_table, row_num)
            print('完成', str(page), '页')
            info_table.to_csv('链家数据-北京-' + Chinese + '.csv', encoding='gb18030')
    except:
        return

if __name__ == '__main__':
    parse('mentougou', '门头沟', 41)  # 传参，英文部分为url中的一部分，中文为保存的内容，以及最大页数
    parse('changping', '昌平', 100)
    parse('chaoyang', '朝阳', 88)
    parse('daxing', '大兴', 100)
    parse('dongcheng', '东城', 100)
    parse('fangshan', '房山', 100)
    parse('fengtai', '丰台', 100)
    parse('haidian', '海淀', 100)
    parse('shijingshan', '石景山', 68)
    parse('shunyi', '顺义', 100)
    parse('tongzhou', '通州', 100)
    parse('xicheng', '西城', 100)
    parse('pinggu', '平谷', 5)
    parse('yizhuangkaifaqu', '亦庄开发区', 38)