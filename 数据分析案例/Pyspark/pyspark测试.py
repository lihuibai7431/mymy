from pyspark import SparkConf, SparkContext    #优先导入本地包，你叫pyspark？
import os
import json
os.environ['HADOOP_HOME']="D:\派森相关\hadoop-3.4.0"
os.environ['PYSPARK_PYTHON']="D:\派森相关\派森11\\python.exe"    #设置spark运行时需要的python解释器
conf=SparkConf().setMaster("local[*]").setAppName('test_spark')     #链式调用，依次执行
conf.set('spark.default.parallelism','1')   #设置spark并行度，默认是cpu核数，核数=分区数=结果文件数这里设置Sparkconf对象属性全局并行度为1
#上一步需要安装hadoop
sc=SparkContext(conf=conf)
'''
rdd1=sc.parallelize('diaonm')
rdd2=sc.parallelize({'key':'jfjf'})    #通过parallelize方法将Python对象加载到Spark内，成为RDD对象，就可以用spark很多数据处理方法
print(rdd1.collect())     #数据输入的本质就是获取rdd对象，pyspark数据计算的载体只能是rdd对象
print(rdd2.collect())    #查看rdd内容需要collect()方法
rdd3=sc.textFile('D:/bill.txt')     #textFile()方法可以将文件加载到Spark内，成为RDD对象，rdd对象总体是一个列表，里面元素是字符串，一行对应一个字符串
print(rdd3.collect())
sc.stop()
'''
# rdd=sc.parallelize([1,2,3,4,5,6,7,8,9,10])     #创建rdd对象
# # def hanshu(x):
# #     return x**3
# rdd1=rdd.map(lambda x:x**3).map(lambda x:x*2)     #map()方法可以对rdd对象中的每个元素进行操作，返回一个新的rdd对象,其逻辑是(t)->U,有传入参数有返回值。返回值是rdd对象就可以链式调用。
# print(rdd1.collect())     #lambda表达式，匿名函数，可以简化代码。  输出rdd对象内容的内容是一个列表。

# rddd=sc.parallelize({'fj jj jl','aa bb cc'})
# rddd1=rddd.flatMap(lambda x:x.split(" "))     #脑残了这么简单的语法错误找半天，就是忘了用新变量接收表达式
# print(rddd1.collect())    #flatMap()方法可以在map方法的基础上解除输出的内部嵌套。
# sc.stop()
# rdd=sc.parallelize([(1,4),(1,6),(2,7),(2,9),(2,2),(3,7)])    #reduceByKey()方法可以对二元元组rdd对象中的元素进行分组，然后对分组后的元素根据处理函数进行两两计算，返回一个新的rdd对象
# rdd1=rdd.reduceByKey(lambda x,y:x*y)
# print(rdd1.collect())
# sc.stop()

# rdd=sc.textFile("D:\\BaiduNetdiskDownload\\python入门\第15章资料\资料\\hello.txt")
# rdd1=rdd.flatMap(lambda x:x.split(" "))
# print(rdd1.collect())
# print(type(rdd1.collect()))     #rdd1.collect()返回的是一个列表.
# list1=[]
# for i in rdd1.collect():
#     a=(i,1)
#     list1.append(a)
# rdd2=rdd1.map(lambda x:(x,1))
# rdd3=rdd2.reduceByKey(lambda x,y:x+y)
# # rdd2=sc.parallelize(list1).reduceByKey(lambda x,y:x+y)
# print(rdd3.collect())
# rdd4=rdd3.sortBy(lambda x:x[1],ascending=False,numPartitions=1)   #sortBy()方法可以对rdd对象中的元素进行排序，一个处理函数决定排序依据，一个升降序，一个全局排序分区
# print(rdd4.collect())
# sc.stop()

# rdd=sc.textFile("D:\\BaiduNetdiskDownload\\python入门\第15章资料\资料\\hello.txt")
# sc.stop()
# rdd=sc.parallelize('jfjjfjfjjf')
# rdd2=rdd.distinct()   #老是忘记赋值。distinct就是去重，最外层的重复元素。
# print(rdd2.collect())   #字符串一个个拆开字符存入rdd列表，字典只有key存入。
# sc.stop()
'''
rdd=sc.parallelize('fjjfjfj')     
print(rdd.collect())     #发现，rdd输入字符串会在列表里拆开输出，para的作用只是构建rdd，拆开作用是print collect的
'''
# 练习案例

# rdd=sc.textFile("D:\\BaiduNetdiskDownload\\python入门\第15章资料\资料\\orders.txt")
# print(rdd.collect())   #了解数据结构，总体结构是列表·字符串·带分隔符的几个字典（形式），列表是rdd输出的外层不用管，所以只有两层。
# rdd1=rdd.map(lambda x:x.split("|"))     #注意，lambda里的x就对应方法遍历的rdd的每个元素。这里用解嵌套是因为他妈的split会输出列表，print只会输出最外层列表
# print(rdd1.collect())    #每个JSON字符串都是rdd中的一个元素，不会像普通字符串一样分隔。
# dict1=rdd1.map(lambda x:json.loads(x))    #把x从json字符串转变为字典类型,注意这里map返回的依然是rdd对象。
# #!rdd2=rdd1.map(lambda x:(dict(x)["areaName"],dict(x)["money"]))
# rdd2=dict1.map(lambda x:(x["areaName"],int(x["money"])))    #晕了，map就是对rdd数据里的第二层元素一个一个按函数处理，这里rdd没有表层，就是读取文件层，默认字符串，改成了一个个字典，这里第一层就按函数处理

# rdd3=rdd2.reduceByKey(lambda x,y:x+y)    #money是字符串，要转化为整型，才能进行加法运算，这里仅仅只分组不排序
# # print(rdd3.collect())
# rdd4=rdd3.sortBy(lambda x:x[1],ascending=False,numPartitions=1)    #这里是按照第二层元素的第二个元素排序，降序，全局排序，分区数为1
# print(rdd4.collect())
# rdd5=dict1.map(lambda x:x['category']).distinct()
# print(rdd5.collect())
# rdd6=dict1.filter(lambda x:x['areaName']=='北京')     #filter就是过滤rdd数据，函数写过滤条件就行了，map函数是写操作
# rdd7=rdd6.map(lambda x:x['category']).distinct()
# print(rdd7.collect())

# rdd=sc.parallelize((1,5,8,6,7,7))
# print(rdd.reduce(lambda a,b:a*b))    #不同于计算的算子，输出算子直接可以print，collect只能输出列表，所以有别的类型]]
# print(rdd.take(4))    #take()方法可以取出rdd对象的前几个元素，返回一个列表
# print(rdd.count())    #count()方法可以统计rdd对象的元素个数
# sc.stop()
# rdd=sc.parallelize([1,24,5,6,7])
# # rdd=sc.parallelize([1,24,5,6,7],numSlices=1)   #单个rdd设置分区为1
# rdd.saveAsTextFile('D:\\outputs')

#练习案例
rdd=sc.textFile("D:\\BaiduNetdiskDownload\\python入门\第15章资料\资料\\search_log.txt")    #很奇怪，这里输出不全，可能文件数据太多了。
'''
# rdd1=rdd.map(lambda x:x[0])   #读取文件他妈肯定是字符串啊,每一行对应一个x
# rdd1=rdd.map(lambda x:x.split("\t")).map(lambda x:x[0]).map(lambda x:x[0:2]).\    #这是糟糕的写法
# map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(3)  #第一个不需要解嵌套，列表正好索引。不然全是字符串乱套了
rdd1=rdd.map(lambda x:(x.split("\t")[0][:2],1))\
    .reduceByKey(lambda x,y:x+y)\
    .sortBy(lambda x:x[1],ascending=False,numPartitions=1)\
    .take(3)
#搞不懂rdd.方法？就是rdd里面每个元素执行一遍，如果是文件这样没有封装，那就每行作为一个字符串元素处理。方法不会造成嵌套，split是特例。
print(rdd1)
'''
# rdd1=rdd.map(lambda x:(x.split('\t')[2],1)).\
#     reduceByKey(lambda x,y:x+y).\
#     sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
#     take(3)
# print(rdd1)
#
# rdd2=rdd.map(lambda x:x.split("\t")).filter(lambda x:x[2]=='黑马程序员')\
#     .map(lambda x:(x[0][:2],1))\
#     .reduceByKey(lambda x,y:x+y)\
#     .sortBy(lambda x:x[1],ascending=False,numPartitions=1)\
#     .take(1)
# print(rdd2)
#
# rdd3=rdd.map(lambda x:x.split("\t")).\
#     map(lambda x:{'time':x[0],'id':x[1],'keyword':x[2],'r1':x[3],'r2':x[4],'url':x[5]}).\
#     saveAsTextFile('D:\\outputs')

