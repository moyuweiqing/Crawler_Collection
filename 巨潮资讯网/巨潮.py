import requests
import json
import pandas as pd

stocklist = ['000998', '600265', '002556', '002385', '000713', '002714', '002891', '600371', '600598', '000860', '600354', '600506', '601952', '600313', '603668', '603336', '300189', '600108', '002746', '002041', '002157', '601118', '002311', '300498', '002299', '002696', '002124', '600359', '002086', '002240', '600076', '300094', '300106', '002200', '600275', '000592', '300087', '002069', '002234', '300313', '600540', '600467', '600257', '002679', '300262', '300761', '600097', '002321', '000798', '000663', '600975', '002458', '002688', '002100', '000735', '600965', '603363', '300511']

yysr = pd.DataFrame(columns=['name', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
lrze = pd.DataFrame(columns=['name', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
sds = pd.DataFrame(columns=['name', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
jlr = pd.DataFrame(columns=['name', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])

def get_data(dic, l, df, number):
    years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
    for i in years:
        if i in dic:
            l.append(dic[i])
        else:
            l.append(' ')
    df.loc[number] = l

def detail(url, headers, data, stock, number):
    global yysr, lrze, sds, jlr

    req = requests.post(url, headers=headers, data=data)  # 通过requests来获取网页内容
    js = json.loads(req.content)
    for i in js:
        if i['index'] == '营业收入':
            temp = [stock]
            get_data(i, temp, yysr, number)
        elif i['index'] == '利润总额':
            temp = [stock]
            get_data(i, temp, lrze, number)
        elif i['index'] == '所得税':
            temp = [stock]
            get_data(i, temp, sds, number)
        elif i['index'] == '净利润':
            temp = [stock]
            get_data(i, temp, jlr, number)


def run():
    global yysr, lrze, sds, jlr

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
        req = requests.post(url, headers = headers, data = data1)  # 通过requests来获取网页内容
        js = json.loads(req.content)
        param = js[0]['F002N']

        para = 'scode='+stock+';rtype=4;sign=' + str(param)
        print(para)
        # 利润表
        data2 = {
            'mergerMark': 'sysapi1075', 'paramStr': para
        }
        detail(url, headers, data2, stock, i)
    yysr.to_csv('营业收入.csv', encoding='gbk')
    lrze.to_csv('利润总额.csv', encoding='gbk')
    sds.to_csv('所得税.csv', encoding='gbk')
    jlr.to_csv('净利润.csv', encoding='gbk')

if __name__ == '__main__':
    run()