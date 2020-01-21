import pandas as pd
import matplotlib.pyplot as plt


def openCSV():
    data = pd.read_csv("data.csv")
    prices = data.price
    kms = data.km
    
    return prices, kms

def displayFunction(kms, theta0, theta1):
    a = []
    for i in range(len(kms)):
        a.append(kms[i] * theta1 + theta0)
    return a

def costFunction(theta0, theta1, prices, kms):
    m = len(prices)
    cost = 0
    for i in range(m):
        cost += (1/m) * ((theta0 + theta1 * kms[i]) - (prices[i]))
    return(cost)

def normalizeFonction(datas):
    normalizedDatas = []
    for i in range(len(datas)):
        normalizedDatas.append((datas[i]) / (max(datas)))
    return normalizedDatas

def costFunction_2(theta0, theta1, prices, kms):
    m = len(prices)
    cost = 0
    for i in range(m):
        cost += (1/m) * (((theta0 + theta1 * kms[i]) - (prices[i])) * kms[i])
    return(cost)

def gradientDescent(prices, kms, plt):
    theta0 = 0
    theta1 = 0
    pricesNormalized = normalizeFonction(prices)
    kmsNormalized = normalizeFonction(kms)
    learningRate = 15
    m = len(prices)
    while(True):
        temp0 = theta0
        temp1 = theta1
        theta0 = temp0 - learningRate * ((1 / m) * costFunction(temp0, temp1, pricesNormalized, kmsNormalized))
        theta1 = temp1 - learningRate * ((1 / m) * costFunction_2(temp0, temp1, pricesNormalized, kmsNormalized))
        if(temp0 == theta0 and theta1 == temp1):
            break
    return theta0, theta1

def writeCSV(theta0, theta1):
    df = pd.DataFrame({"theta0": [theta0], "theta1": [theta1]})
    df.to_csv('theta.csv')


if __name__ == '__main__':
    prices, kms = openCSV()
    axes = plt.axes()
    axes.grid() # dessiner une grille pour une meilleur lisibilité du graphe
    plt.scatter(kms, prices) # X et Y sont les variables qu'on a extraite dans le paragraphe précédent
    plt.xlabel("Kilometrage")
    plt.ylabel("Prix")
    theta0, theta1 = gradientDescent(prices, kms, plt)
    theta0 = theta0 * max(prices)
    theta1 = theta1 * (max(prices)) / max(kms)
    plt.plot(kms, displayFunction(kms, theta0, theta1))
    plt.show()
    writeCSV(theta0, theta1)