#encoding=utf-8

__author__='ricky'

# def trim(s):
#     if len(s) == 0 : return s
#     for start in range(0, len(s) - 1):
#         if s[start] != ' ': break
#     for end in range(len(s) - 1, 0, -1):
#         if s[end] != ' ': break
#     return s[start : end + 1]
#
#
# # 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

s = {'a':'a1', 'b' : 'b1'}
print([k + ':' + v for k,v in s.items()])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]

print(L2)