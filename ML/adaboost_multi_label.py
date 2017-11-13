'''
2017.11.13
adaboost multiple label classify
'''
from adaboost import *
import numpy as np
import random


def loadData():  # 加载数据集iris
    from sklearn import datasets
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target
    return np.mat(X), np.array(Y)


def train(X, Y, labelNum):
    num = 0  # 二分类器的索引
    model = {}  #保存多个二分类器，每个二分类器由若干个弱分类器组成
    for i in range(labelNum - 1):  # 3 category
        for j in range(i + 1, labelNum):
            num = num + 1
            #找到i和j类别的数据，重新归类
            index1 = np.nonzero(Y == i)[0]
            index2 = np.nonzero(Y == j)[0]
            label_temp = np.zeros((len(index1) + len(index2), 1))
            #i类标签设置为1,j类标签设置为-1
            label_temp[:len(index1)] = 1
            label_temp[len(index1):len(index1) + len(index2)] = -1
	    #形成由i和j组成的训练数据集
            train_temp = np.vstack((
                X[index1, :], X[index2, :]))
	    #得到索引为num的二分器(针对i和j类别)
            model[num] = adaBoostTrainDS(train_temp, label_temp.T[0])
    return model


def predict(X, classifierArr):
    m, n = shape(X)
    aggClassEst = mat(zeros((m, 1)))  # 弱分类器的累加情况
    for i in range(len(classifierArr)):
        classEst = stumpClassify(
            X, classifierArr[i]['dim'], classifierArr[i]['thresh'], classifierArr[i]['ineq'])
        aggClassEst += classEst * classifierArr[i]['alpha']
    return sign(aggClassEst)  # 分类结果


def main():
    X, Y = loadData()
    N = len(X)  # 150
    numberTrain = 100
    #随机划分，形成训练数据集和测试数据集
    train_index = random.sample(range(0, N), numberTrain)
    test_index = []
    for i in range(150):
        if i in train_index:
            continue
        test_index.append(i)
    train_data = X[train_index, :]
    train_target = Y[train_index]
    test_data = X[test_index, :]
    test_target = Y[test_index]
    labelNum = len(set(train_target))
    # train
    model = train(train_data, train_target, labelNum)
    # test
    predict_result = np.zeros((len(test_data),)) #保存测试分类结果
    for m in range(len(test_data)):
        data_test = test_data[m, :]
        num = 0
        addnum = np.zeros((5,))
        for i in range(labelNum - 1):
            for j in range(i + 1, labelNum):
                num = num + 1
                temp_predict = predict(data_test, model[num])
                if temp_predict == 1:
                    addnum[i] = addnum[i] + 1
                elif temp_predict == -1:
                    addnum[j] = addnum[j] + 1
        numMax = max(addnum)
        index_max = list(addnum).index(numMax)
        predict_result[m] = index_max
    tmp = (predict_result != test_target)
    errorNums = (np.multiply(tmp, np.ones(len(test_data),))).sum()
    test_errorRate = errorNums / len(test_data)
    print("correct rate is: {}".format(str(1 - test_errorRate)))


if __name__ == '__main__':
    main()
