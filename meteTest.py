__author__='zhaicao'

def fn(self, name='world'):
    print('Hello,%s' % name)

# 创建Hello类
Hello = type('Hello', (object,), dict(hello = fn))

h = Hello()

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 使用ListMetaclass来定制类
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)