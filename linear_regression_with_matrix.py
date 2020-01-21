#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def openCSV():
    data = pd.read_csv("data.csv")
    prices = data.price
    kms = data.km
    
    return prices, kms

def displayFunction(kms, thetas):
    return kms @ thetas

def normalizeFonction(datas):
    return datas / (max(datas))


def costFunction(thetas, prices, kms):
    m = len(prices)
    cost = (1 / (2 * m)) * sum((kms @ thetas - prices) ** 2)
    return cost

def gradientDescent(prices, kms, plt):
    cost = []
    thetas = np.array([0, 0])
    learningRate = 1.5
    m = len(prices)
    while(True):
        temp = thetas
        thetas = thetas - learningRate * ((1 / m) * (kms.T @ ((kms @ thetas) - prices)))
        cost.append(costFunction(thetas, prices, kms))
        if(np.array_equal(thetas, temp)):
            break
    return thetas, cost

def writeCSV(theta0, theta1):
    df = pd.DataFrame({"theta0": [theta0], "theta1": [theta1]})
    df.to_csv('theta.csv')

def printPrediction(kms, prices, thetas, cost):
    
    #Gradiant Descent
    axes = plt.axes()
    axes.grid()
    plt.scatter(kms, prices)
    plt.xlabel("Kilometrage")
    plt.ylabel("Prix")
    thetas[0] = thetas[0] * max(prices)
    thetas[1] = thetas[1] * (max(prices)) / max(kms)
    kmsMatrix = np.c_[np.ones(kms.shape[0]), kms]
    plt.plot(kms, kmsMatrix @ thetas)
    plt.show()
    
    #Cost Function
    x = np.arange(len(cost))
    plt.plot(x, cost)
    plt.show()

if __name__ == '__main__':
    prices, kms = openCSV()
    pricesNormalized = normalizeFonction(prices)
    kmsNormalized = normalizeFonction(kms)
    kmsNormalized = np.c_[np.ones(kmsNormalized.shape[0]), kmsNormalized]
    thetas, cost = gradientDescent(pricesNormalized, kmsNormalized, plt)
    printPrediction(kms, prices, thetas, cost)

    # writeCSV(theta0, theta1)