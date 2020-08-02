import requests
import os
from lxml import etree
import pandas as pd

info_table = pd.DataFrame(columns=['电影名称', '主演名单', '上映日期', '评分'])
count = 0

def write(l):
    global info_table
    global count

    info_table.loc[count] = l
    count += 1

def parsedd(text):
    name = text.xpath("dd/div/div/div[1]/p[1]/a/text()")
    actor = text.xpath("dd/div/div/div[1]/p[2]/text()")
    time = text.xpath("dd/div/div/div[1]/p[3]/text()")
    point_int = text.xpath("dd/div/div/div[2]/p/i[1]/text()")
    point_fra = text.xpath("dd/div/div/div[2]/p/i[2]/text()")
    for i in range(0, 10):
        l = []
        l.append(name[i])
        l.append(str(actor[i]).replace('\n', '').replace(' ', '').replace('主演：', ''))
        l.append(str(time[i]).replace('上映时间：', ''))
        l.append(str(point_int[i])+str(point_fra[i]))
        write(l)


def page(url, headers):
    page = requests.get(url, headers=headers)
    selector = etree.HTML(page.text)
    html_text = selector.xpath("//dl[@class='board-wrapper']")
    for each in html_text:
        parsedd(each)
        break

def run():
    global info_table

    url_head = 'https://maoyan.com/board/4?offset='
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
               'Host': 'maoyan.com',
               'Referer': 'https://maoyan.com/board'}
    for i in range(0, 10):
        url = url_head + str(i * 10)
        page(url, headers)
    path = str(os.getcwd() + '\猫眼爬虫结果\\top100.csv')
    info_table.to_csv(path, encoding='gbk')

if __name__ == '__main__':
    run()