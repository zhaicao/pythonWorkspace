# k-means算法的实现
# -*-coding:utf-8 -*-
from numpy import *
from math import sqrt

import sys

sys.path.append("C:/Users/Administrator/Desktop/k-means的python实现")


def loadData(fileName):
    data = []
    fr = open(fileName)
    for line in fr.readlines():
        curline = line.strip().split('\t')
        frline = map(float, curline)
        data.append(frline)
    return data


'''
#test
a = mat(loadData("C:/Users/Administrator/Desktop/k-means/testSet.txt"))
print a
'''


# 计算欧氏距离
def distElud(vecA, vecB):
    return sqrt(sum(power((vecA - vecB), 2)))


# 初始化聚类中心
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    center = mat(zeros((k, n)))
    for j in range(n):
        rangeJ = float(max(dataSet[:, j]) - min(dataSet[:, j]))
        center[:, j] = min(dataSet[:, j]) + rangeJ * random.rand(k, 1)
    return center


'''
#test
a = mat(loadData("C:/Users/Administrator/Desktop/k-means/testSet.txt"))
n = 3
b = randCent(a,3)
print b
'''


def kMeans(dataSet, k, dist=distElud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))
    center = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = dist(dataSet[i, :], center[j, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:  # 判断是否收敛
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist ** 2
        print
        center
        for cent in range(k):  # 更新聚类中心
            dataCent = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            center[cent, :] = mean(dataCent, axis=0)  # axis是普通的将每一列相加，而axis=1表示的是将向量的每一行进行相加
    return center, clusterAssment


'''
#test
dataSet = mat(loadData("C:/Users/Administrator/Desktop/k-means/testSet.txt"))
k = 4
a = kMeans(dataSet,k)
print a
'''

## 采用MCR判定聚类效果
B = class(: ,4);
B = reshape(B, 1, row);
A = [ones(1, 100), 2 * ones(1, 100), 3 * ones(1, 100), 4 * ones(1, 100)];

sum = 0;
for i = 1:row
if (A(1, i) ~= B(1, i))
sum = sum + 1;
end
end
MCR = sum / row;
fprintf('MCR = %d\n', MCR);