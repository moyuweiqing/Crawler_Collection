import requests
import json
import pandas as pd
import re

stocks = ['SZ000998', 'SH600265', 'SZ002556','SZ002385', 'SZ000713', 'SZ002714', 'SZ002891', 'SH600371', 'SH600598', 'SZ000860', 'SH600354', 'SH600506', 'SH601952', 'SH600313', 'SH603668', 'SH603336', 'SZ300189', 'SH600108', 'SZ002746', 'SZ002041', 'SZ002157', 'SH601118', 'SZ002311', 'SZ300498', 'SZ002299', 'SZ002696', 'SZ002124', 'SH600359', 'SZ002086', 'SZ002240', 'SH600076', 'SZ300094', 'SZ300106', 'SZ002200', 'SH600275', 'SZ000592', 'SZ300087', 'SZ002069', 'SZ002234', 'SZ300313', 'SH600540', 'SH600467', 'SH600257', 'SZ002679', 'SZ300262', 'SZ300761', 'SH600097', 'SZ002321', 'SZ000798', 'SZ000663', 'SH600975', 'SZ002458', 'SZ002688', 'SZ002100', 'SZ000735', 'SH600965', 'SH603363', 'SZ300511', 'SZ002505', 'SZ002772', 'SZ300143', 'SH600189', 'SZ200992']
# info_table = pd.DataFrame(columns = ['股票代码', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010'])
info_table = pd.DataFrame(columns = ['股票代码', '2009'])

def run():
    # years = ['2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010']
    years = ['2009']
    row = 0

    # url = 'http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/002714/ctrl/2019/displaytype/4.phtml'
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    # response = requests.get(url, headers)
    # # print(response.text)
    # zichan_span = re.findall('净资产报酬率(.*?)资产', response.text)
    # print(zichan_span[0])
    # zichan = re.findall('<td>(.*?)<', zichan_span[0])
    # print(zichan)
    # zichan = float(str(zichan[0]).replace(',', ''))
    # print(zichan)

    for stock in stocks:
        alist = []
        alist.append(stock[2:])
        for year in years:
            url = 'http://money.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet/stockid/' + str(stock[2:]) + '/ctrl/' + str(year) + '/displaytype/4.phtml'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
            response = requests.get(url, headers)
            try:
                zichan_span = re.findall('流动资产合计(.*?)非流动资产', response.text)
                zichan = re.findall(';\'>(.*?)<', zichan_span[0])
                zichan = float(str(zichan[0]).replace(',', ''))
                fuzhai_span = re.findall('流动负债合计(.*?)非流动负债', response.text)
                fuzhai = re.findall(';\'>(.*?)<', fuzhai_span[0])
                fuzhai = float(str(fuzhai[0]).replace(',', ''))
                alist.append(float(zichan-fuzhai))
            except:
                alist.append('')
        info_table.loc[row] = alist
        row += 1
        print('已完成', stock)

    info_table.to_csv('营运资本2009.csv', encoding='gbk')

if __name__ == '__main__':
    run()