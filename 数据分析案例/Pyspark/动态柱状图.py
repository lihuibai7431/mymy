from pyecharts.globals import ThemeType
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
f=open("D:\\BaiduNetdiskDownload\\python入门\资料\可视化案例数据\动态柱状图数据\\1960-2019全球GDP数据.csv",'r',encoding='gb2312')
a=f.readlines()
f.close()
a=a[1:]
# print(a)
zid={}
for i in a:
    # print(i)
    # print(type(i))
    I=i.split(',')
    year=I[0]
    country=I[1]
    GDP=float(I[2])
    try:
        zid[year].append([country,GDP])
    except:
        zid[year]=[]
        zid[year].append([country,GDP])
# print(zid)
tm=Timeline({'theme':ThemeType.LIGHT})
YEAR=sorted(zid.keys())
for year in YEAR:
    # print(year)
    zid[year].sort(key=lambda x:x[1],reverse=True)
    zid[year]=zid[year][:8]
    xdt=[]
    ydt=[]
    for i in zid[year]:
       xdt.append(i[0])
       ydt.append(i[1]/100000000)
    xdt.reverse()
    ydt.reverse()
    bar=Bar()
    bar.add_xaxis(xdt)
    bar.add_yaxis("GDP(亿)",ydt,label_opts=LabelOpts(position='right'))
    bar.reversal_axis()
    bar.set_global_opts(title_opts=TitleOpts(title=f'{year}年全球前八国家GDP数据'))
    tm.add(bar,str(year))
tm.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
tm.render('1960-2019全球GDP数据.html')