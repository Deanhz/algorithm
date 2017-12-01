import numpy as np
import matplotlib.pyplot as plt
from point import *
from optics import *


def loadData(filename):
    fin = open(filename)
    data = []
    for line in fin:
        line_list = line.strip().split("\t")
        d1 = float(line_list[0])
        d2 = float(line_list[1])
        data.append([d1, d2])
    return np.array(data)


def getPoints(data):
    points = []
    for p in data:
        lat = p[0]
        lont = p[1]
        point = Point(lat, lont)
        points.append(point)
    return points


def plotClusters(clusters, rawData):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(rawData[:, 1], rawData[:, 0], s=0.2, c="black")
    for cluster in clusters:
        points = cluster.points
        data = []
        for point in points:
            lat = point.latitude
            lont = point.longitude
            data.append([lat, lont])
        data = np.array(data)
        ax.scatter(data[:, 1], data[:, 0], s=0.5)
    plt.show()


def plotReachability(orderList):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    index = list(range(len(orderList)))
    rList = []
    for p in orderList:
        if p.rd:
            rList.append(p.rd)
        else:
            rList.append(200)
    ax.plot(index, rList)
    plt.show()


if __name__ == "__main__":
    data = loadData("000_tmp2")
    points = getPoints(data)
    optics = Optics(points, 200, 60)
    optics.run()
    clusters = optics.cluster(80)
    for index, p in enumerate(optics.ordered):
        if p.rd and p.rd <= 60:
            print(
                "{} ----------------------------------------------------".format(str(index)))
        print(p.rd)
    # plotClusters(clusters, data)
    # plotReachability(optics.ordered)
