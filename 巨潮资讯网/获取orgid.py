import requests
import urllib.request
import random
import json

stocklist = ['000998', '600265', '002556', '002385', '000713', '002714', '002891', '600371', '600598', '000860', '600354', '600506', '601952', '600313', '603668', '603336', '300189', '600108', '002746', '002041', '002157', '601118', '002311', '300498', '002299', '002696', '002124', '600359', '002086', '002240', '600076', '300094', '300106', '002200', '600275', '000592', '300087', '002069', '002234', '300313', '600540', '600467', '600257', '002679', '300262', '300761', '600097', '002321', '000798', '000663', '600975', '002458', '002688', '002100', '000735', '600965', '603363', '300511']
stocks = ['000998,gssz0000998', '600265,gssh0600265', '002556,9900018282', '002385,9900011648', '000713,gssz0000713', '002714,9900022995', '002891,9900032780', '600371,gssh0600371', '600598,gssh0600598', '000860,gssz0000860', '600354,gssh0600354', '600506,gssh0600506', '601952,9900030581', '600313,gssh0600313', '603668,9900029592', '603336,9900023771', '300189,9900017647', '600108,gssh0600108', '002746,9900023137', '002041,gssz0002041', '002157,9900003434', '601118,9900005902', '002311,9900009032', '300498,9900009247', '002299,9900008409', '002696,9900023143', '002124,9900002441', '600359,gssh0600359', '002086,9900001344', '002240,9900004687', '600076,gssh0600076', '300094,9900012529', '300106,9900013409', '002200,9900003907', '600275,gssh0600275', '000592,gssz0000592', '300087,9900010589', '002069,9900000781', '002234,9900004604', '300313,9900021985', '600540,gssh0600540', '600467,gssh0600467', '600257,gssh0600257', '002679,9900022738', '300262,9900021192', '300761,9900032565', '600097,gssh0600097', '002321,9900009334', '000798,gssz0000798', '000663,gssz0000663', '600975,gssh0600975', '002458,9900013789', '002688,9900023128', '002100,9900001641', '000735,gssz0000735', '600965,gssh0600965', '603363,9900033003', '300511,9900024682']
dic = {'000998,gssz0000998': 'sz', '600265,gssh0600265': 'sh', '002556,9900018282': 'sz', '002385,9900011648': 'sz', '000713,gssz0000713': 'sz', '002714,9900022995': 'sz', '002891,9900032780': 'sz', '600371,gssh0600371': 'sh', '600598,gssh0600598': 'sh', '000860,gssz0000860': 'sz', '600354,gssh0600354': 'sh', '600506,gssh0600506': 'sh', '601952,9900030581': 'sz', '600313,gssh0600313': 'sh', '603668,9900029592': 'sz', '603336,9900023771': 'sz', '300189,9900017647': 'sz', '600108,gssh0600108': 'sh', '002746,9900023137': 'sz', '002041,gssz0002041': 'sz', '002157,9900003434': 'sz', '601118,9900005902': 'sz', '002311,9900009032': 'sz', '300498,9900009247': 'sz', '002299,9900008409': 'sz', '002696,9900023143': 'sz', '002124,9900002441': 'sz', '600359,gssh0600359': 'sh', '002086,9900001344': 'sz', '002240,9900004687': 'sz', '600076,gssh0600076': 'sh', '300094,9900012529': 'sz', '300106,9900013409': 'sz', '002200,9900003907': 'sz', '600275,gssh0600275': 'sh', '000592,gssz0000592': 'sz', '300087,9900010589': 'sz', '002069,9900000781': 'sz', '002234,9900004604': 'sz', '300313,9900021985': 'sz', '600540,gssh0600540': 'sh', '600467,gssh0600467': 'sh', '600257,gssh0600257': 'sh', '002679,9900022738': 'sz', '300262,9900021192': 'sz', '300761,9900032565': 'sz', '600097,gssh0600097': 'sh', '002321,9900009334': 'sz', '000798,gssz0000798': 'sz', '000663,gssz0000663': 'sz', '600975,gssh0600975': 'sh', '002458,9900013789': 'sz', '002688,9900023128': 'sz', '002100,9900001641': 'sz', '000735,gssz0000735': 'sz', '600965,gssh0600965': 'sh', '603363,9900033003': 'sz', '300511,9900024682': 'sz'}


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
           'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '40',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'www.cninfo.com.cn',
            'Origin': 'http://www.cninfo.com.cn',
            'Referer': 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=000998',
           'Referer': 'http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice',
           'X-Requested-With': 'XMLHttpRequest'
           }

def pdf():
    url = r"http://static.cninfo.com.cn/finalpage/2017-04-28/1203415549.PDF"
    path = r"./pdf目录/" + str(123) + ".pdf"
    data = urllib.request.urlopen(url).read()
    f = open(path, "wb")
    f.write(data)
    f.close()
    print("finish download " + url + "!")

def run():
    s = []
    for i in stocklist:
        query_path = 'http://www.cninfo.com.cn/new/information/topSearch/detailOfQuery'
        headers['User-Agent'] = random.choice(User_Agent)  # 定义User_Agent
        query = {
            'keyWord': i,
            'maxSecNum': '10',
            'maxListNum': '5'
        }
        namelist = requests.post(query_path, headers=headers, data=query)
        s.append(i + ',' + namelist.json()['keyBoardList'][0]['orgId'])
    print(s)

if __name__ == '__main__':
    # run()
    for stock in stocks:
        if (stock[9: 11] == 'sh' or stock[9: 11] == 'sz'):
            dic[stock] = stock[9: 11]
        else:
            dic[stock] = 'sz'
    print(dic)