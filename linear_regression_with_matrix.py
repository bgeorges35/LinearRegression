import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def openCSV():
    data = pd.read_csv("data.csv")
    prices = data.price
    kms = data.km
    return prices, kms


def normalizeFonction(datas):
    return datas / (max(datas))


def gradientDescent(Y, X):
    thetas = np.array([0, 0])
    learningRate = 1.5
    m = len(Y)
    while (True):
        tmp = thetas
        thetas = thetas - learningRate * ((1 / m) * np.dot(X.T, np.dot(X, thetas) - Y))
        if (np.array_equal(thetas, tmp)):
            break
    return thetas


##BONUS
def printPrediction(kms, prices, thetas):
    kmsMatrix = np.c_[np.ones(kms.shape[0]), kms]
    fig, ax = plt.subplots()
    ax.set(xlabel="Kilometrage", ylabel="Prix", title="Prediction du cout d'une voiture")
    ax.grid()
    ax.scatter(kms, prices)
    ax.plot(kms, np.dot(kmsMatrix, thetas))
    plt.show()


if __name__ == '__main__':
    prices, kms = openCSV()
    Y = normalizeFonction(prices)
    X = normalizeFonction(kms)
    X = np.c_[np.ones(X.shape[0]), X]
    thetas = gradientDescent(Y, X)
    thetas[0] = thetas[0] * max(prices)
    thetas[1] = thetas[1] * (max(prices)) / max(kms)
    ##BONUS
    printPrediction(kms, prices, thetas)
    df = pd.DataFrame({"theta0": [thetas[0]], "theta1": [thetas[1]]})
    df.to_csv('theta.csv')
    print(thetas)