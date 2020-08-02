# 爬取猫眼电影指定日期区间的前十票房

import requests
import datetime
import json
import pandas as pd
import os

start = datetime.date(2020, 1, 1)
end = datetime.date(2020, 1, 5)
info_table = pd.DataFrame(columns = ['电影名称', '当日票房', '票房占比', '排片场次', '排片占比', '场均人次', '上座率'])

def detail(date, dic):
    global info_table

    l = []
    l.append(dic['movieName'])
    l.append(dic['boxInfo'])
    l.append(dic['boxRate'])
    l.append(dic['avgSeatView'])
    l.append(dic['showInfo'])
    l.append(dic['avgShowView'])
    l.append(dic['avgSeatView'])
    info_table.loc[date] = l

def run():
    global start
    global end
    global info_table
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

    while start <= end:
        url = 'http://piaofang.maoyan.com/second-box?beginDate='+start.strftime('%Y%m%d')
        response = requests.get(url, headers = headers)
        response_json = json.loads(response.text)
        for i in range(0, 10):
            detail(i + 1, response_json['data']['list'][i])
        path = str(os.getcwd()+'\猫眼爬虫结果'+'\\'+start.strftime('%Y%m%d')+'.csv')
        info_table.to_csv(path, encoding='gbk')
        start += datetime.timedelta(days=1)

if __name__ == '__main__':
    run()