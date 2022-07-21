import pandas as pd
import requests
import json
from bs4 import BeautifulSoup as bs

def get_data(text):
    json_data = json.loads(text)
    json_comments = json_data['data']
    for i in json_comments:
        comment = i['text'].split('<')[0]
        comment = pd.DataFrame([comment], columns=['comment'])
        comment.to_csv('评论.csv', index=False, mode='a+', header=False, encoding='gb18030')

if __name__ == '__main__':
    url = 'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4717489961308147&is_show_bulletin=2&is_mix=0&count=10&uid=2803301701'
    res = requests.get(url)
    get_data(res.text)