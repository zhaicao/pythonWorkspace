# coding: utf-8

# Copyright (c) 2018 BeiTown

import os
import pandas
import common.conApriori

from numpy import *
from sklearn.linear_model import LinearRegression


def linear_model_main(_distances, _press_times, target_distance):
    regr = LinearRegression()
    regr.fit(_distances, _press_times)
    predict_press_time = regr.predict(target_distance)
    result = {}
    # 截距 b
    result['intercept'] = regr.intercept_
    # 斜率值 k
    result['coefficient'] = regr.coef_
    # 预估的按压时间
    result['value'] = predict_press_time
    return result


def computing_k_b_v(target_distance):
    result = linear_model_main(distances, press_times, target_distance)
    b = result['intercept']
    k = result['coefficient']
    v = result['value']
    return k[0], b[0], v[0]


def add_data(distance, press_time):
    distances.append([distance])
    press_times.append([press_time])
    save_data('./jump_range.csv', distances, press_times)


def save_data(file_name, distances, press_times):
    pf = pandas.DataFrame({'Distance': distances, 'Press_time': press_times})
    # print(pf)
    pf.to_csv(file_name, index=False, sep=',')


def get_data(file_name):
    data = pandas.read_csv(file_name)
    distance_array = []
    press_time_array = []
    for distance, press_time in zip(data['Distance'], data['Press_time']):
        distance_array.append([float(distance.strip().strip('[]'))])
        press_time_array.append([float(press_time.strip().strip('[]'))])
    return distance_array, press_time_array


def init():
    global distances, press_times
    distances = []
    press_times = []

    if os.path.exists('./jump_range.csv'):
        distances, press_times = get_data('./jump_range.csv')
    else:
        save_data('./jump_range.csv', [], [])
        return 0

def loadData():
    mat(loadData("../data/testSet.txt"))


def get_result_len():
    return len(distances)

#构建多个对应的项集
def aprioriGen(Lk,k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1 = list(Lk[i])[:k-2]
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i]|Lk[j])
    return retList


#使用关联规则生成函数
def generateRules(L,supportData,minConf = 0.7):
    bigRuleList = []
    for i in range(1,len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet,H1,supportData,bigRuleList,minConf)
            else:
                calcConf(freqSet,H1,supportData,bigRuleList,minConf)
    return bigRuleList

#集合右边一个元素
def calcConf(freqSet,H,supportData,brl,minConf = 0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet - conseq]
        if conf >= minConf:
            print(freqSet - conseq,'-->',conseq,'conf:',conf)
            brl.append((freqSet-conseq,conseq,conf))
            prunedH.append(conseq)
    return prunedH

#生成更多的关联规则
def rulesFromConseq(freqSet,H,supportData,br1,minConf = 0.7):
    m = len(H[0])
    if (len(freqSet)>(m + 1)):
        Hmp1 = aprioriGen(H,m+1)
        Hmp1 = calcConf(freqSet,Hmp1,supportData,br1,minConf)
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet,Hmp1,supportData,br1,minConf)


