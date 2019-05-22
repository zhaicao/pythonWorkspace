'''
Apriori算法
zc
'''
from numpy import *

def loadData():
    return[[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

def createC1(dataSet):
    c1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    return map(frozenset,c1)

def scanD(D,Ck,minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):#判断tid是否在can中
                if not ssCnt.has_key(can):
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList,supportData