
__author__='zhaicao '

def care(*number):
    sum = 0
    for n in number:
        sum = sum + n* n
    return sum

def person(name, age, **kw):
    print('name:', name , 'age:', age, 'other:', kw)


def people(name, age, *, city, job):
    print(name, age, city, job)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


if __name__ == '__main__':
    kw = {'city': 'beijing', 'grade': 'A级'}
    # person('zc',30, **kw)
    # person('zc', 30, city = kw['city'])
    #people('zc', 30, city = 'beijing', job = 'work')
    #L = [x * x for x in range(10)]
    #print(L)
    #g = (x * x for x in range(10))
    #for i in g:
    #   print(i)
