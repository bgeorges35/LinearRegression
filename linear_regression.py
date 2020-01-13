import pandas as pd

def openCSV():
    data = pd.read_csv("data.csv")
    prices = data.price
    kms = data.km
    
    return prices, kms

def costFunction(theta0, price):
    m = len(prices)
    prediction = 0
    for price in prices: 
        prediction += theta0 + theta1 * X - price
    print(prediction)

def linearRegression(prices, kms):
    theta0 = 0
    theta1 = 0
    X = 0
    LearningRate = 0.0000000000015
    costFunction(theta0, prices)
    

if __name__ == '__main__':
    prices, kms = openCSV()
    linearRegression(prices, kms)
    
    
    