import datetime
from typing import List, Any

from 文件定义 import readfile,readfile1,readjs
from 数据定义 import jilu
from pymysql import Connection
import json
txt1=readfile1("D:\\BaiduNetdiskDownload\\python入门\第13章资料\\2011年1月销售数据.txt")
json1=readjs("D:\\BaiduNetdiskDownload\\python入门\第13章资料\\2011年2月销售数据JSON.txt")
jandata:list[jilu]=txt1.duqu()
febdata:list[jilu]=json1.duqu()
alldata:list[jilu]=jandata+febdata
# print(alldata)
'''
datadict={}
for i in alldata:
    if i.data in datadict.keys():
        datadict[i.data]+=i.money
    else:
        datadict[i.data]=i.money
# print(datadict)
# print(type(datadict.keys()))
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType    #本应该写最上面
bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(datadict.keys()))
bar.add_yaxis('销售额',list(datadict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render('每日销售额柱状图.html')
'''
conn=Connection(host='localhost',port=3306,user='root',password='212121',autocommit=True)
cursor=conn.cursor()
conn.select_db('py_sql')
# for i in alldata:
#     sql=f"insert into orders(dday,id,money,province) values('{i.data}','{i.id}','{i.money}','{i.province}')"
#     # print(sql)
#     cursor.execute(sql)    #他妈的ai提示需要检查
# conn.close()    #忘记写了
cursor.execute('select * from orders')
a=cursor.fetchall()
list1=[]
for i in a:
    b:list=list(i)
    b[0]=str(b[0]).strip('datetime.date')     #狗屎弱警告不能用[]，能运行就行了，类型注解就没了
    keys=['date','id','money','province']
    js=json.dumps(dict(zip(keys,b)),ensure_ascii=False)     #注意一个是中文转码，一个是zip（keys，values），键值都是列表
    # print(js)
    list1.append(js)
with open('D:\\BaiduNetdiskDownload\\python入门\第13章资料\\示例js文件', 'w', encoding='utf-8') as file:
    json.dump(list1,file,indent=4,ensure_ascii=False)
conn.close()   #就这样吧，生成json文件不会，删反斜杠也不会。







