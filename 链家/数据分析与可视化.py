import pandas as pd
import os
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from wordcloud import WordCloud

# 构建柱状图调用接口，传入x轴和y轴的信息，以及名称
def draw_bar(xlist, ylist, name):
    bar = (
        Bar(init_opts=opts.InitOpts(
            width='1800px',
            height='800px',
            js_host="./",
        ))
        .set_global_opts(title_opts=opts.TitleOpts(
                title=name
            )
        )
        .add_xaxis(xaxis_data=xlist)
        .add_yaxis(series_name=name, yaxis_data=ylist)
        .render(name + '.html')
    )

# 构建饼图调用接口，传入可视化内容的名称和数值，以及饼图名称
def draw_pie(xlist, ylist, name):
    data_pair = [list(z) for z in zip(xlist, ylist)]
    c = (
        Pie(init_opts=opts.InitOpts(
            width='1800px',
            height='800px',
            js_host="./",
        ))
        .set_global_opts(title_opts=opts.TitleOpts(
            title=name
            )
        )
        .add(
            series_name=name,
            data_pair=data_pair
        )
        .render(name + '.html')
    )

# 定义计算各区平均房价函数
def cal_avg_rent(filenames):
    # 平均房价柱状图
    xlist = []
    ylist = []
    for filename in filenames:
        xlist.append(str(str(filename).split('-')[-1]).split('.')[0])
        f = open(os.path.join('', filename), encoding='gb18030')
        data = pd.read_csv(f)
        total_price = 0
        for i in data['租金']:
            total_price += float(str(i).split(' ')[0]) # 添加每个信息的租金情况
        ylist.append(round(total_price / len(data), 2)) # 求平均值
    draw_bar(xlist, ylist, '各区平均房价')

# 定义统计样本数量的统计函数，调用的是柱状图函数
def cal_num(filenames):
    # 样本数量
    xlist = []
    ylist = []
    for filename in filenames:
        xlist.append(str(str(filename).split('-')[-1]).split('.')[0])
        f = open(os.path.join('', filename), encoding='gb18030')
        data = pd.read_csv(f)
        ylist.append(len(data))
    draw_bar(xlist, ylist, '样本数量')

# 定义计算北京租房价格情况函数，调用饼图
def rent_distribution(filenames):
    # 北京租房价格饼图
    # 分为7个档次进行计算
    xlist = ['1000元以下', '1000-2000元', '2000-3000元', '3000-4000元', '4000-5000元', '5000-6000元', '6000元以上']
    ydic = {'1000元以下': 0, '1000-2000元': 0, '2000-3000元': 0, '3000-4000元': 0, '4000-5000元': 0, '5000-6000元': 0,
            '6000元以上': 0}
    ylist = []
    for filename in filenames:
        f = open(os.path.join('', filename), encoding='gb18030')
        data = pd.read_csv(f)
        for i in data['租金']:
            price = float(str(i).split(' ')[0])
            if price <= 1000:
                ydic['1000元以下'] += 1
            elif price > 1000 and price <= 2000:
                ydic['1000-2000元'] += 1
            elif price > 2000 and price <= 3000:
                ydic['2000-3000元'] += 1
            elif price > 3000 and price <= 4000:
                ydic['3000-4000元'] += 1
            elif price > 4000 and price <= 5000:
                ydic['4000-5000元'] += 1
            elif price > 5000 and price <= 6000:
                ydic['5000-6000元'] += 1
            else:
                ydic['6000元以上'] += 1
    for i in ydic:
        ylist.append(ydic[i])
    draw_pie(xlist, ylist, '北京租房价格分布图')

# 计算北京房间类型的分布情况
def cal_room_type(filenames):
    # 房间类型
    xlist = []
    ydic = {}
    ylist = []
    for filename in filenames:
        f = open(os.path.join('', filename), encoding='gb18030')
        data = pd.read_csv(f)
        for i in data['房间组成']:
            i = i.replace(' ', '').replace('\n', '')
            if i in xlist:
                ydic[i] += 1
            else:
                xlist.append(i)
                ydic[i] = 1
    for i in ydic:
        ylist.append(ydic[i])
    draw_pie(xlist, ylist, '北京租房房间类型分布图')

# 计算房间朝向
def cal_orientation(filenames):
    # 房间朝向
    xlist = []
    ydic = {}
    ylist = []
    for filename in filenames:
        f = open(os.path.join('', filename), encoding='gb18030')
        data = pd.read_csv(f)
        for i in data['朝向']:
            elements = i.split(' ')
            for element in elements:
                if element != '':
                    if element in xlist:
                        ydic[element] += 1
                    else:
                        xlist.append(element)
                        ydic[element] = 1
    for i in ydic:
        ylist.append(ydic[i])
    draw_pie(xlist, ylist, '北京租房房间朝向分布图')

def draw_wordcloud(filenames):
    # 租房标签词云图
    labels_dic = {}
    for filename in filenames:
        f = open(os.path.join('', filename), encoding='gb18030')
        data = pd.read_csv(f)
        for i in data['标签']:
            elements = i.split('\n')
            for element in elements:
                if element != '':
                    if element in labels_dic:
                        labels_dic[element] += 1
                    else:
                        labels_dic[element] = 1
    wc = WordCloud(font_path='simkai.ttf', max_words=100, width=1920, height=1080, margin=5)
    wc.generate_from_frequencies(labels_dic)
    wc.to_file('北京租房标签词云图.png')

if __name__ == '__main__':
    filenames = os.listdir('./')  # 设定调用文件的相对路径
    f = []
    for i in filenames:
        if '.csv' in str(i):
            f.append(i)
    filenames = f
    cal_num(filenames)  # 调用函数

    cal_avg_rent(filenames)

    rent_distribution(filenames)

    cal_room_type(filenames)

    cal_orientation(filenames)

    draw_wordcloud(filenames)