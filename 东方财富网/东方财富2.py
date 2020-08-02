import requests
import json
import pandas as pd

stocks = ['SZ000998', 'SH600265', 'SZ002556','SZ002385', 'SZ000713', 'SZ002714', 'SZ002891', 'SH600371', 'SH600598', 'SZ000860', 'SH600354', 'SH600506', 'SH601952', 'SH600313', 'SH603668', 'SH603336', 'SZ300189', 'SH600108', 'SZ002746', 'SZ002041', 'SZ002157', 'SH601118', 'SZ002311', 'SZ300498', 'SZ002299', 'SZ002696', 'SZ002124', 'SH600359', 'SZ002086', 'SZ002240', 'SH600076', 'SZ300094', 'SZ300106', 'SZ002200', 'SH600275', 'SZ000592', 'SZ300087', 'SZ002069', 'SZ002234', 'SZ300313', 'SH600540', 'SH600467', 'SH600257', 'SZ002679', 'SZ300262', 'SZ300761', 'SH600097', 'SZ002321', 'SZ000798', 'SZ000663', 'SH600975', 'SZ002458', 'SZ002688', 'SZ002100', 'SZ000735', 'SH600965', 'SH603363', 'SZ300511', 'SZ002505', 'SZ002772', 'SZ300143', 'SH600189', 'SZ200992']

def run():
    for i in range(0, len(stocks)):
        temp = stocks[i]
        url_head = 'http://f10.eastmoney.com/CompanyManagement/CompanyManagementAjax?code='
        url = url_head + temp
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        response = requests.get(url, headers)
        # print(response.text)
        response_json = json.loads(response.text)
        print(response_json['RptManagerList'])
        info_table = pd.DataFrame(columns=['姓名', '性别', '出生日期（计算值）', '职位', '年龄', '学历', '简介'])
        row = 0
        for person in response_json['RptManagerList']:
            alist = []
            alist.append(response_json['RptManagerList'][row]['xm'])
            alist.append(response_json['RptManagerList'][row]['xb'])
            try:
                alist.append(2020 - int(response_json['RptManagerList'][row]['nl']))
            except:
                alist.append('')
            alist.append(response_json['RptManagerList'][row]['zw'])
            alist.append(response_json['RptManagerList'][row]['nl'])
            alist.append(response_json['RptManagerList'][row]['xl'])
            alist.append(response_json['RptManagerList'][row]['jj'])
            info_table.loc[row] = alist
            row += 1
        info_table.to_csv('./管理层信息/' + stocks[i] + '.csv', encoding='gbk')

def get_trade():
    for i in range(0, len(stocks)):
        temp = stocks[i]
        url_head = 'http://f10.eastmoney.com/CompanyManagement/CompanyManagementAjax?code='
        url = url_head + temp
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        response = requests.get(url, headers)
        # print(response.text)
        response_json = json.loads(response.text)
        print(response_json['RptManagerList'])
        info_table = pd.DataFrame(columns=['日期', '变动人', '变动数量（股）', '交易均价（元）', '结存股票（股）', '交易方式', '董监高管', '高管职位', '与高管关系'])
        row = 0
        for person in response_json['RptShareHeldChangeList']:
            alist = []
            alist.append(response_json['RptShareHeldChangeList'][row]['rq'])
            alist.append(response_json['RptShareHeldChangeList'][row]['bdr'])
            alist.append(response_json['RptShareHeldChangeList'][row]['bdsl'])
            alist.append(response_json['RptShareHeldChangeList'][row]['jjjj'])
            alist.append(response_json['RptShareHeldChangeList'][row]['jcgp'])
            alist.append(response_json['RptShareHeldChangeList'][row]['gfbdtj'])
            alist.append(response_json['RptShareHeldChangeList'][row]['djgg'])
            alist.append(response_json['RptShareHeldChangeList'][row]['ggzw'])
            alist.append(response_json['RptShareHeldChangeList'][row]['ygggx'])
            info_table.loc[row] = alist
            row += 1
        info_table.to_csv('./股票变动信息/' + stocks[i] + '.csv', encoding='gbk')

if __name__ == '__main__':
    get_trade()