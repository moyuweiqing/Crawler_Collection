import pandas as pd

name = ['飞鸟乐园', '国际马戏大剧院', '欢乐世界', '水上乐园', '野生动物世界']

e1 = pd.DataFrame(columns=['评论'])
e2 = pd.DataFrame(columns=['评论'])
e3 = pd.DataFrame(columns=['评论'])
e4 = pd.DataFrame(columns=['评论'])
e5 = pd.DataFrame(columns=['评论'])

r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0

# words = '智慧、智能、APP、应用、公众号、微信、微博、wifi、速度、电子、讲解、先进、定位、买票、购票、订票、取票、电子票、出票、拿票、扫码、二维码、网上、网络、方便、快捷、快、便捷、广告、宣传'

word1 = '智慧、智能、APP、应用、公众号、微信、微博、wifi'
word2 = '电子、讲解、先进、定位'
word3 = '买票、购票、订票、取票、电子票、出票、拿票、扫码、二维码、网上、网络'
word3_1 = '方便、快捷、快、便捷'
word4 = '交通'
word5 = '广告、宣传'

w1 = word1.split('、')
w2 = word2.split('、')
w3 = word3.split('、')
w3_1 = word3_1.split('、')
w4 = word4.split('、')
w5 = word5.split('、')

comments = []
for n in name:
    fn = './好评数据/广州长隆' + n + '好评.csv'
    data = pd.read_csv(fn, encoding='gbk')
    for row in range(0, len(data)):
        for j in w1:
            if j in str(data['评论'].iloc[row]):
                e1.loc[r1] = str(data['评论'].iloc[row])
                r1 += 1
                break
        for j in w2:
            if j in str(data['评论'].iloc[row]):
                e2.loc[r2] = str(data['评论'].iloc[row])
                r2 += 1
                break
        for j in w3:
            for k in w3_1:
                if j in str(data['评论'].iloc[row]):
                    if k in str(data['评论'].iloc[row]):
                        e3.loc[r3] = str(data['评论'].iloc[row])
                        r3 += 1
                        break
        for j in w4:
            if j in str(data['评论'].iloc[row]):
                for k in w3_1:
                    if k in str(data['评论'].iloc[row]):
                        e4.loc[r4] = str(data['评论'].iloc[row])
                        r4 += 1
                        break
        for j in w5:
            if j in str(data['评论'].iloc[row]):
                e5.loc[r5] = str(data['评论'].iloc[row])
                r5 += 1
                break
        # for j in row:
        #     if j in str(data['评论'].iloc[i]):
        #         comments.append(str(data['评论'].iloc[i]))
        #         break

print(len(e1))
print(len(e2))
print(len(e3))
print(len(e4))
print(len(e5))


e1.to_csv('e1.csv',encoding='gbk')
e2.to_csv('e2.csv',encoding='gbk')
e3.to_csv('e3.csv',encoding='gbk')
e4.to_csv('e4.csv',encoding='gbk')
e5.to_csv('e5.csv',encoding='gbk')