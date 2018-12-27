__author__ = 'zhaicao'

from xmind2testlink.xmind_parser import *
from xmind2testlink.testlink_parser import *
from xmind2testlink.sharedparser import *
import copy



def list_all_dict(dict_a):
    if dict_a.get('makers') : #使用isinstance检测数据x],l)
        data = copy.deepcopy(dict_a)
        if data.get('topics'):
            data.pop('topics')
        print(data)
        for x in dict_a.get('topics'):
            list_all_dict(x) #自我调用实现无限遍历

# d = {1:"a",2:"b",3:{4:"c",5:"dprint(cases_dict)",6:{7:"e"}},8:"f"}
# list_all_dict(d)
if __name__ == '__main__':
    # root = xmind_to_dict('test_case_by_xmind_v2.xmind')
    # print(root[0]['topic'])
    suite = xmind_to_suite_v2('test_case_by_xmind_v2.xmind')
    # #print()
    # list_all_dict(root[0]['topic'])
    print(suite.to_dict())
