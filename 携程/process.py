import pandas as pd
import os
from wordcloud import WordCloud
import jieba
import jieba.analyse
from matplotlib import image
from pyecharts.charts import Pie
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts import options as opts

# s1 = text.replace('\n', '').replace(' ', '')#去除换行
info_table = pd.DataFrame(columns=['名字', '频数'])

# 获取关键词
def getKeyWords(text):
    fenci_text = jieba.cut(text)
    stopwords = {}.fromkeys([line.rstrip() for line in open('.\stopwords.txt', encoding="utf-8")])
    final = ""
    for word in fenci_text:
        if word not in stopwords:
            if (word != "。" and word != "，"):
                final = final + " " + word

    keywords = jieba.analyse.extract_tags(final, topK=20, withWeight=True, allowPOS=())
    print(keywords)

# 统计词频
def statistics(texts):
    words_dict = {}
    temp = jieba.cut(texts)
    stopwords = open('.\stopwords.txt', encoding="utf-8").read()
    # stopwords = {}.fromkeys([line.rstrip() for line in open('.\stopwords.txt', encoding="utf-8")])
    # print(stopwords)
    for t in temp:
        if t not in stopwords:
            if t in words_dict.keys():
                words_dict[t] += 1
            else:
                words_dict[t] = 1
    return words_dict

# 柱状图
def drawBar(title, x_data, y_data, savepath='./results'):
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("", y_data)
    bar.set_global_opts(title_opts=opts.TitleOpts(title=title))
    bar.render(os.path.join(savepath, '%s.html' % title))

# 饼图
def drawPie(title, data, savepath='./results'):
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    pie = Pie()
    attrs = [i for i, j in data.items()]
    values = [j for i, j in data.items()]
    pie.add("", [list(z) for z in zip(attrs, values)])
    pie.set_global_opts(title_opts=opts.TitleOpts(title="评分情况"), legend_opts=opts.LegendOpts(pos_left=160))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    pie.render(os.path.join(savepath, '%s.html' % title))

if __name__ == '__main__':
    data = pd.read_csv('./好评数据/广州长隆野生动物世界好评.csv', encoding='gbk')
    name = '差评+长隆野生动物世界+频数表'
    comment = ''
    for i in range(0, len(data)):
        comment += str(data['评论'].iloc[i])

    data = pd.read_csv('./好评数据/广州长隆国际马戏大剧院好评.csv', encoding='gbk')
    name = '差评+长隆野生动物世界+频数表'
    # comment = ''
    for i in range(0, len(data)):
        comment += str(data['评论'].iloc[i])

    data = pd.read_csv('./好评数据/广州长隆欢乐世界好评.csv', encoding='gbk')
    name = '差评+长隆野生动物世界+频数表'
    # comment = ''
    for i in range(0, len(data)):
        comment += str(data['评论'].iloc[i])

    data = pd.read_csv('./好评数据/广州长隆水上乐园好评.csv', encoding='gbk')
    name = '差评+长隆野生动物世界+频数表'
    # comment = ''
    for i in range(0, len(data)):
        comment += str(data['评论'].iloc[i])

    data = pd.read_csv('./好评数据/广州长隆野生动物世界好评.csv', encoding='gbk')
    name = '差评+长隆野生动物世界+频数表'
    # comment = ''
    for i in range(0, len(data)):
        comment += str(data['评论'].iloc[i])
    # text_family = ''
    # text_couple = ''
    # text_single = ''
    # text_business = ''
    # text_friend = ''
    #
    # # 画饼图
    # score_data = {'家庭': 0, '夫妻': 0, '独自旅游': 0, '商务': 0, '好友': 0}
    # for i in range(0, len(data)):
    #     if (data['旅游者类型'].iloc[i] == '家庭'):
    #         score_data['家庭'] += 1
    #         text_family += data['评论'].iloc[i]
    #     elif (data['旅游者类型'].iloc[i] == '夫妻'):
    #         score_data['夫妻'] += 1
    #         text_couple += data['评论'].iloc[i]
    #     elif (data['旅游者类型'].iloc[i] == '独自旅游'):
    #         score_data['独自旅游'] += 1
    #         text_single += data['评论'].iloc[i]
    #     elif (data['旅游者类型'].iloc[i] == '商务'):
    #         score_data['商务'] += 1
    #         text_business += data['评论'].iloc[i]
    #     else:
    #         score_data['好友'] += 1
    #         text_friend += data['评论'].iloc[i]
    # print(score_data)
    # drawPie('广州长隆飞鸟乐园评论游客类型分布图', score_data)
    # print(text_family)
    word = statistics(comment)
    a = sorted(word.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, int(len(a)*0.05)):
        print(a[i])
    # for i in range(0, int(len(a)*0.2)):
    #     alist = []
    #     alist.append(a[i][0])
    #     alist.append(a[i][1])
    #     info_table.loc[i] = alist
    # info_table.to_csv(name + '.csv', encoding='gbk')
    # getKeyWords(comment)