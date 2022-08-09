import requests
from lxml import etree
import datetime

start = datetime.date(2019, 11, 25)  # 起始日期
end = datetime.date(2019, 11, 30)  # 结束日期

while start <= end:
    url = 'http://tv.cctv.com/lm/xwlb/day/' + start.strftime('%Y%m%d') + '.shtml'
    r = requests.post(url, timeout=30)
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    html_data = html.xpath('/html/body/ul[*]/li[*]/a/div[2]/div[1]')
    for i in html_data:  #数据处理
        print(i.text)

    start += datetime.timedelta(days=1)