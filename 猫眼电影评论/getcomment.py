import pandas as pd
import json
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Cookie': 'td_cookie=18446744070798277348; _lxsdk_cuid=16bf8b5b7922e-0e65d805a43579-43450721-1fa400-16bf8b5b7937c; t_lxid=17181097322c8-08cee160ed4e47-43450721-1fa400-17181097322c8-tid; _lxsdk=21F5CDC0390C11EBB1AF0F1DB9BFAA150E43C6306AAA4E03B718ED819929DD40; _lx_utm=utm_source%3Dso.com%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1607415151,1607494792,1607495145,1607495198; __mta=142434189.1563245787449.1607495198562.1607496161071.18; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1607496401; _lxsdk_s=1764627f287-e2b-be5-036%7C%7C59',
    'Host': 'm.maoyan.com'
}

info_table = pd.DataFrame(columns=['城市名称', '用户性别', '评论', '用户id', '用户昵称', '用户评分', '用户等级'])
row = 0

def savedata(info):
    global info_table, row

    alist = []
    try:
        city = info['cityName']
        alist.append(city)
    except:
        alist.append('')

    try:
        gender = info['gender']
        alist.append(gender)
    except:
        alist.append('')

    try:
        content = info['content']
        alist.append(content)
    except:
        alist.append('')

    try:
        id = info['id']
        alist.append(id)
    except:
        alist.append('')

    try:
        nick = info['nick']
        alist.append(nick)
    except:
        alist.append('')

    try:
        score = info['score']
        alist.append(score)
    except:
        alist.append('')

    try:
        level = info['userLevel']
        alist.append(level)
    except:
        alist.append('')

    info_table.loc[row] = alist
    row += 1

def getcomment(res):
    data = json.loads(res.text)
    cmts = data['cmts']
    for i in cmts:
        savedata(i)

if __name__ == '__main__':
    url_head = 'https://m.maoyan.com/mmdb/comments/movie/'
    movie_id = pd.read_excel('电影id.xlsx')
    for i in range(0, len(movie_id)):
        id = movie_id['电影id'].iloc[i]
        url_head2 = url_head + str(id) + '.json?v=yes&offset='
        for j in range(0, 1000, 15):
            url = url_head2 + str(j)
            try:
                res = requests.get(url=url, headers=headers)
                getcomment(res)
                print('完成', j, '条')
                info_table.to_csv(movie_id['电影名称'].iloc[i] + '.csv', encoding='gb18030')
                # time.sleep(2)
            except:
                print('获取失败')
                break
        info_table = pd.DataFrame(columns=['城市名称', '用户性别', '评论', '用户id', '用户昵称', '用户评分', '用户等级'])
        row = 0
        time.sleep(2)
        print('      已完成：', id)