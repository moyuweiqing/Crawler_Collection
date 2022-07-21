import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar

moviename = '八佰'

def draw_line(xlist, ylist):
    c = (
        Bar(init_opts=opts.InitOpts(
            width='1800px',
            height='800px',
            js_host="./",
        ))
            .add_xaxis(xlist)
            .add_yaxis("用户数", ylist)
            .set_global_opts(
            title_opts=opts.TitleOpts("电影" + moviename + '观影观众评分分布图'),
            brush_opts=opts.BrushOpts(),
        )
            .render(moviename + '观影观众评分分布图.html')
    )

def process(df):
    point_dic = {}

    for i in range(0, len(df)):
        if df['用户评分'].iloc[i] in point_dic:
            point_dic[df['用户评分'].iloc[i]] += 1
        else:
            point_dic[df['用户评分'].iloc[i]] = 1

    data = d_order=sorted(point_dic.items(),key=lambda x:x[0],reverse=False)

    xlist = []
    ylist = []

    for i in range(0, len(data)):
        xlist.append(data[i][0])
        ylist.append(data[i][1])

    draw_line(xlist, ylist)

if __name__ == '__main__':
    df = pd.read_csv('电影评论/' + moviename + '.csv', encoding = 'gb18030')
    process(df)