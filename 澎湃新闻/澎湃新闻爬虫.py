import pandas as pd
import requests
import re
from bs4 import BeautifulSoup as bs

class parser():
    def __init__(self):
        self.cnt = 1
    def parse(self, bs_lxml):
        comments = bs_lxml.find_all('div', class_ = 'ansright_cont')
        likes = bs_lxml.find_all('div', class_ = 'ansright_time')
        for c in comments:
            print(c.get_text().replace(' ', '').replace('\n', ''))
        for l in likes:
            print(l.get_text().split('|')[0].replace(' ', '').replace('\n', ''))

        # 找出下一页的id
        id_class = 'startId' + str(self.cnt)
        self.cnt += 1
        id = re.findall('startid="(.*?)"',str(bs_lxml.find_all('div', id = id_class)[0]))[0]
        print(id)
        return

if __name__ == '__main__':
    url = 'https://www.thepaper.cn/newDetail_commt.jsp?contid=15927538&_=1640047997919'
    url2_head = 'https://www.thepaper.cn/load_moreFloorComment.jsp?contid=15927538&hotIds=36245745,36245739,36245887,36245862,36245850&pageidx=2&startId='
    res = requests.get(url).text
    html_tree = bs(res, 'lxml')
    # print(html_tree)
    p = parser()
    id = 1
    while id != '0':
        url2 = url2_head + id
        res = requests.get()
        p.parse(html_tree)