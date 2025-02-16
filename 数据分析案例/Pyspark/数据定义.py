#数据定义的类
class jilu:
    def __init__(self,data,id,money,province):
        self.data=data
        self.id=id
        self.money=money
        self.province=province
    def __str__(self):
        return f'{self.data},{self.id},{self.money},{self.province}'
