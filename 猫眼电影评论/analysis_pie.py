import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Pie

moviename = '八佰'

def draw_pie(ylist):
    xlist = ['男性', '女性', '未告知']


    c = (
        Pie(init_opts=opts.InitOpts(
            width='1800px',
            height='800px',
            js_host="./",
        ))
            .add(
            "",
            [list(z) for z in zip(xlist, ylist)],
            center=["50%", "50%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="电影" + moviename + '观影观众性别分布图'),
            legend_opts=opts.LegendOpts(pos_left="15%"),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .render(moviename + "观影观众性别分布图.html")
    )

def process(df):
    male = 0
    female = 0
    unknown = 0

    for i in range(0, len(df)):
        if df['用户性别'].iloc[i] == 1:
            male += 1
        elif df['用户性别'].iloc[i] == 2:
            female += 1
        else:
            unknown += 1

    alist = []
    alist.append(male)
    alist.append(female)
    alist.append(unknown)

    draw_pie(ylist=alist)

if __name__ == '__main__':
    df = pd.read_csv('电影评论/' + moviename + '.csv', encoding = 'gb18030')
    process(df)