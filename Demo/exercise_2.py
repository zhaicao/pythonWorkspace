__author__ = 'zhaicao'

class Test():
    pass


if __name__ == '__main__':
    T = Test()
    if hasattr(T, 'name'):
        #T.__setattr__('name','TestName') 等于 setattr(T, 'name', 'TestName')
        setattr(T, 'name', 'TestName')
    #print(T.__getattribute__('name')) 等于 print(getattr(T, 'name'))
    print(getattr(T, 'name'))