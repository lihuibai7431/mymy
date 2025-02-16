#文件相关的类定义
import json

from 数据定义 import jilu
class readfile:     #抽象类
    def duqu(self)->list[jilu]:    #读取文件的数据，读到的每一条数据都转换为jilu对象，将它们都封装到list内返回即可
        pass
class readfile1(readfile):
    def __init__(self,path):
        self.path=path
    def duqu(self)->list[jilu]:
        f=open(self.path,"r",encoding="utf-8")    #类的内部调用对象一定要self前缀
        a=f.readlines()
        recordlt:list[jilu]=[]
        for i in a:
            # print(i)
            i=i.strip()
            b=i.split(',')    #b其实已经是一个列表（元素都是字符串）了，但是它需要转换为jilu类型
            # print(b)    #整这么复杂其实就是为了得到一堆各项数据分开的列表,而且列表要赋值给jilu对象
            # print(b[0])
            record=jilu(b[0],b[1],int(b[2]),b[3])    #这里的b[2]是字符串，需要转换为数字。还有，jilu（。。。）是一个类对象，它不是一个列表，你print它的实例取决于你定义return是什么。
            # print(record)
            # print(type(record))    #注意，record就是class  jilu的一个实例，所以它的类型就是jilu（类相当于自己定义的一种字面量）
            recordlt.append(record)    #append出来得到的recordlt里面元素不是record的类返回值
            # print(recordlt)     #这里应该是打印格式出问题了
        # print(recordlt)
        f.close()
        return recordlt
class readjs(readfile):
    def __init__(self,path):
        self.path=path
    def duqu(self)->list[jilu]:
         f=open(self.path,"r",encoding="utf-8")
         recordlt:list[jilu]=[]
         a=f.readlines()
         for i in a:
             jsdic=json.loads(i)
             jilu(jsdic['date'],jsdic['order_id'],jsdic['money'],jsdic['province'])
             recordlt.append(jilu(jsdic['date'],jsdic['order_id'],jsdic['money'],jsdic['province']))
         f.close()
         return recordlt


if __name__=='__main__':
     # r=readfile1('D:\\BaiduNetdiskDownload\\python入门\第13章资料\\2011年1月销售数据.txt')
     # ao=r.duqu()    #这样就封装好了，如果没有用str方法打印就会直接输出jilu实例的内存地址
     # print(ao)
     # for i in ao:
     #     print(i)    #什么意思，你打印的a不是jilu实例，而是包括jilu实例的一个列表recordlt，自然输出内存地址。你要直接输出jilu实例。
     r1=readjs('D:\\BaiduNetdiskDownload\\python入门\第13章资料\\2011年2月销售数据JSON.txt')
     ao1=r1.duqu()    #注意，调用类方法必须写括号
     print(ao1)
     for i in ao1:
         print(i)
