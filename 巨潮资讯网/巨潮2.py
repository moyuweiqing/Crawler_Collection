import requests
import json
import pandas as pd

stocklist = ['000998', '600265', '002556', '002385', '000713', '002714', '002891', '600371', '600598', '000860', '600354', '600506', '601952', '600313', '603668', '603336', '300189', '600108', '002746', '002041', '002157', '601118', '002311', '300498', '002299', '002696', '002124', '600359', '002086', '002240', '600076', '300094', '300106', '002200', '600275', '000592', '300087', '002069', '002234', '300313', '600540', '600467', '600257', '002679', '300262', '300761', '600097', '002321', '000798', '000663', '600975', '002458', '002688', '002100', '000735', '600965', '603363', '300511']

zzc = pd.DataFrame(columns=['name', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
zfz = pd.DataFrame(columns=['name', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])

def get_data(dic, l, df, number):
    years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
    for i in years:
        if i in dic:
            l.append(dic[i])
        else:
            l.append(' ')
    df.loc[number] = l

def detail(url, headers, data, stock, number):
    global zzc, zfz

    req = requests.post(url, headers=headers, data=data)  # 通过requests来获取网页内容
    js = json.loads(req.content)
    for i in js:
        if i['index'] == '总资产':
            temp = [stock]
            get_data(i, temp, zzc, number)
        elif i['index'] == '总负债':
            temp = [stock]
            get_data(i, temp, zfz, number)

def run():
    global zzc, zfz

    for i in range(0, len(stocklist)):
        stock = stocklist[i]
        para = 'scode='+stock
        data1 = {
            'mergerMark':'sysapi1067','paramStr': para
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 QQBrowser/3.9.3943.400",
            'X-Requested-With': 'XMLHttpRequest'
        }
        url = 'http://www.cninfo.com.cn/data/project/commonInterface'

        param = js[0]['F002N']
        req = requests.post(url, headers = headers, data = data1)  # 通过requests来获取网页内容
        js = json.loads(req.content)

        para = 'scode='+stock+';rtype=4;sign=' + str(param)
        print(para)
        # 利润表
        data2 = {
            'mergerMark': 'sysapi1077', 'paramStr': para
        }
        detail(url, headers, data2, stock, i)
    zzc.to_csv('总资产.csv', encoding='gbk')
    zfz.to_csv('总负债.csv', encoding='gbk')

if __name__ == '__main__':
    run()