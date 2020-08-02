import requests
import json
import pandas as pd

stocks = ['SZ000998', 'SH600265', 'SZ002556','SZ002385', 'SZ000713', 'SZ002714', 'SZ002891', 'SH600371', 'SH600598', 'SZ000860', 'SH600354', 'SH600506', 'SH601952', 'SH600313', 'SH603668', 'SH603336', 'SZ300189', 'SH600108', 'SZ002746', 'SZ002041', 'SZ002157', 'SH601118', 'SZ002311', 'SZ300498', 'SZ002299', 'SZ002696', 'SZ002124', 'SH600359', 'SZ002086', 'SZ002240', 'SH600076', 'SZ300094', 'SZ300106', 'SZ002200', 'SH600275', 'SZ000592', 'SZ300087', 'SZ002069', 'SZ002234', 'SZ300313', 'SH600540', 'SH600467', 'SH600257', 'SZ002679', 'SZ300262', 'SZ300761', 'SH600097', 'SZ002321', 'SZ000798', 'SZ000663', 'SH600975', 'SZ002458', 'SZ002688', 'SZ002100', 'SZ000735', 'SH600965', 'SH603363', 'SZ300511', 'SZ002505', 'SZ002772', 'SZ300143', 'SH600189', 'SZ200992']

def run():
    row = 0
    info_table = pd.DataFrame(columns=['公司代码', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011'])
    for i in range(0, len(stocks)):
        temp = stocks[i]
        url_head = 'http://f10.eastmoney.com/NewFinanceAnalysis/MainTargetAjax?type=1&code='
        url = url_head + temp
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        response = requests.get(url, headers)
        # print(response.text)
        response_json = json.loads(response.text)
        try:
            alist = []
            alist.append(stocks[i])
            for year in range(0, 9):
                try:
                    alist.append(response_json[year]['zcfzl'])
                except:
                    alist.append('')
            info_table.loc[row] = alist
            row += 1
        except:
            continue

    info_table.to_csv('2011-2019资产负债率.csv', encoding='gbk')

if __name__ == '__main__':
    run()