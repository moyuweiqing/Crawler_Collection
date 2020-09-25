import requests, re
import schedule
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
           'cookie': '_zap=ece0df40-bfac-4c9d-9e11-c5cb3f5c83cb; d_c0="ANBg96Qy1A6PTmNnvL4o-v-I0ZXcCKSOYiI=|1547538523"; __gads=ID=65ffaed1ff8ad8e7:T=1547538528:S=ALNI_MbAFbTAViC5nLBlykYv4j-Q-8e76g; _xsrf=CzYLikZzgwd6M2xfzWNPBrXlilFS41Qw; __utma=51854390.912379540.1576769594.1576769594.1576769594.1; __utmv=51854390.100--|2=registration_date=20190907=1^3=entry_date=20190228=1; __guid=74140564.3239082011773169700.1581513138812.8223; q_c1=7cac302e550e4372a1c513a3ba84cc9e|1581513274000|1551325637000; _ga=GA1.2.912379540.1576769594; _gid=GA1.2.278624250.1600649146; count=1; capsion_ticket="2|1:0|10:1600912149|14:capsion_ticket|44:N2U5ODllZTYwMzc2NDI3Yjk1YWNjZDQzNmEzOGU2YTY=|13498c0a814fd83afab482f239cce08f14e31875c8b085facd539b9a0a4f3ce0"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1600909254,1600910439,1600911714,1600912479; SESSIONID=5KkOddS83P42PkPS8Od7RoUz0dsPjaV12wsteLTkzKu; JOID=VFEdBU5MRFF4nh1gaEyIDnpiKeN3dg40NPl2Ml58G2REzXU_Oie3NyeSE29lhKU1IoYDVpoiIVjnnmb-6xCL7D0=; osd=Vl0RAExOSF19nB9sZEmKDHZuLOF1egIxNvt6Plt-GWhIyHc9NiuyNSWeH2pnhqk5J4QBWpYnI1rrkmP86RyH6T8=; KLBRSID=76ae5fb4fba0f519d97e594f1cef9fab|1600912561|1600909257; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1600912557'}

judge = True

def get_data():
    global judge

    info_table = pd.DataFrame(columns=['时间', '序号', '标题', '热度'])

    html_all = requests.get('https://www.zhihu.com/billboard', headers = headers)
    html_text = bs(html_all.text, 'lxml')

    comments = html_text.find_all('div', class_ = 'HotList-itemBody')
    for i in range(0, 10):
        alist = []
        alist.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        alist.append(i)

        name = re.findall('class="HotList-itemTitle">(.*?)</div>', str(comments[i]))
        hot = re.findall('class="HotList-itemMetrics">(.*?)万热度', str(comments[i]))

        alist.append(name[0])
        alist.append(int(hot[0]))

        info_table.loc[i] = alist

    if judge:
        info_table.to_csv('datas1.csv', mode='a+', index=False, encoding='gb18030')
        judge = False
    else:
        info_table.to_csv('datas1.csv', mode='a+', index=False, header=False, encoding='gb18030')

    print(datetime.datetime.now().strftime('%H:%M:%S'), 'finish')

if __name__ == '__main__':
    schedule.every(1).minutes.do(get_data)

    while True:
        schedule.run_pending()