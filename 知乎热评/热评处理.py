import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline, Grid
from pyecharts.globals import ThemeType, CurrentConfig

CurrentConfig.ONLINE_HOST = r'D:/pyecharts-assets-master/assets/'
df = pd.read_csv('datas1.csv', encoding='gb18030')
# print(df.info())
t = Timeline(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))  # 定制主题
for i in range(112):
    bar = (
        Bar()
        .add_xaxis(list(df['标题'][i*10: i*10+10][::-1]))         # x轴数据
        .add_yaxis('热度', list(df['热度'][i*10: i*10+10][::-1]))   # y轴数据
        .reversal_axis()     # 翻转
        .set_global_opts(    # 全局配置项
            title_opts=opts.TitleOpts(  # 标题配置项
                title=f"{list(df['时间'])[i*10]}",
                pos_right="5%", pos_bottom="15%",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_family='KaiTi', font_size=24, color='#FF1493'
                )
            ),
            xaxis_opts=opts.AxisOpts(   # x轴配置项
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            yaxis_opts=opts.AxisOpts(   # y轴配置项
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axislabel_opts=opts.LabelOpts(color='#DC143C')
            )
        )
        .set_series_opts(    # 系列配置项
            label_opts=opts.LabelOpts(  # 标签配置
                position="right", color='#9400D3')
        )
    )
    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_left="24%"))
    )
    t.add(grid, "")
    t.add_schema(
        play_interval=100,          # 轮播速度
        is_timeline_show=False,     # 是否显示 timeline 组件
        is_auto_play=True,          # 是否自动播放
    )

t.render('时间轮播图.html')