import requests
import random
import time
import urllib

download_path = 'http://static.cninfo.com.cn/'
saving_path = './'

stocks = ['000998,gssz0000998', '600265,gssh0600265', '002556,9900018282', '002385,9900011648', '000713,gssz0000713', '002714,9900022995', '002891,9900032780', '600371,gssh0600371', '600598,gssh0600598', '000860,gssz0000860', '600354,gssh0600354', '600506,gssh0600506', '601952,9900030581', '600313,gssh0600313', '603668,9900029592', '603336,9900023771', '300189,9900017647', '600108,gssh0600108', '002746,9900023137', '002041,gssz0002041', '002157,9900003434', '601118,9900005902', '002311,9900009032', '300498,9900009247', '002299,9900008409', '002696,9900023143', '002124,9900002441', '600359,gssh0600359', '002086,9900001344', '002240,9900004687', '600076,gssh0600076', '300094,9900012529', '300106,9900013409', '002200,9900003907', '600275,gssh0600275', '000592,gssz0000592', '300087,9900010589', '002069,9900000781', '002234,9900004604', '300313,9900021985', '600540,gssh0600540', '600467,gssh0600467', '600257,gssh0600257', '002679,9900022738', '300262,9900021192', '300761,9900032565', '600097,gssh0600097', '002321,9900009334', '000798,gssz0000798', '000663,gssz0000663', '600975,gssh0600975', '002458,9900013789', '002688,9900023128', '002100,9900001641', '000735,gssz0000735', '600965,gssh0600965', '603363,9900033003', '300511,9900024682']

User_Agent = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"
]  # User_Agent的集合

headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-TW;q=0.5",
           'Host': 'www.cninfo.com.cn',
           'Origin': 'http://www.cninfo.com.cn',
           'Referer': 'http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice',
           'X-Requested-With': 'XMLHttpRequest'
           }

def single_page(page, stock):
    query_path = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    headers['User-Agent'] = random.choice(User_Agent)  # 定义User_Agent
    a = ''
    if (stock[9: 11] == 'sh' or stock[9: 11] == 'sz'):
        a = stock[9: 11]
    else:
        a = 'sz'
    query = {'pageNum': page,  # 页码
             'pageSize': 30,
             'tabName': 'fulltext',
             'column': 'szse',  # 深交所
             'stock': stock,
             'searchkey': '',
             'secid': '',
             'plate': a,
             'category': 'category_ndbg_szsh;',  # 年度报告
             'trade': '',
             'seDate': '2009-01-01+~+2020-03-03'  # 时间区间
             }
    namelist = requests.post(query_path, headers=headers, data=query)
    print(page, '*********')
    return namelist.json()['announcements']  # json中的年度报告信息

def saving(single_page):  # 下载年报
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-TW;q=0.5",
               'Host': 'www.cninfo.com.cn',
               'Origin': 'http://www.cninfo.com.cn'
               }
    years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
    for i in single_page:
        for j in years:
            name1 = j + '年年度报告（更新后）'
            name2 = j + '年年度报告'
            if i['announcementTitle'] == name1 or i['announcementTitle'] == name2:
                download = download_path + i["adjunctUrl"]
                name = i["secCode"] + '_' + i['secName'] + '_' + i['announcementTitle'] + '.pdf'
                if '*' in name:
                    name = name.replace('*', '')
                file_path = saving_path + '//' + name
                time.sleep(random.random() * 2)
                headers['User-Agent'] = random.choice(User_Agent)
                data = urllib.request.urlopen(download).read()
                f = open(file_path, "wb")
                f.write(data)
                f.close()
                print(name)
            else:
                continue


def spy_save(page, stock):
    try:
        page_data = single_page(page, stock)
    except:
        print(page, 'page error, retrying')
        try:
            page_data = single_page(page, stock)
        except:
            print(page, 'page error')
    saving(page_data)

for i in stocks:
    spy_save(1, i)