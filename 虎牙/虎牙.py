import requests
import pandas as pd
import os
from bs4 import BeautifulSoup as bs

info_table = pd.DataFrame(columns=['主播名称', '房间号', '人气值'])
count = 0

def write(alist):
    global count
    global info_table

    info_table.loc[count] = alist
    count += 1

def detail(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    alist = []

    response = requests.get(url, headers)
    res = response.content
    html_tree = bs(res, 'lxml')
    host_name = html_tree.find('h3', class_='host-name')
    alist.append(host_name['title'])
    room = html_tree.find('span', class_='host-rid')
    room_number = str(room.find('em')).replace('<em>', '').replace('</em>', '')
    alist.append(room_number)
    live_count = str(html_tree.find('em', id = 'live-count')).replace('<em id="live-count" title="人气值">', '').replace('</em>', '')
    alist.append(live_count)
    write(alist)

def run():
    global info_table

    url = 'https://www.huya.com/g/wzry'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    response = requests.get(url, headers)
    res = response.content  # 获取内容
    html = str(res, 'utf-8')  # 字符转换
    html_tree = bs(html, 'lxml')  # 用bs框架转换
    html_text = html_tree.find_all("a", class_="title new-clickstat j_live-card")  # 找到所有的
    for text in html_text:
        a_href = text['href']
        detail(a_href)
    path = str(os.getcwd() + '\虎牙爬虫结果\\results.csv')
    info_table.to_csv(path, encoding='gbk')

if __name__ == '__main__':
    run()