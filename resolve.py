import pandas as pd

def openCSV():
    data = pd.read_csv("theta.csv")
    return (float(data.theta0), float(data.theta1))

def findPrice(theta0, theta1, km):
    price = km * theta1 + theta0
    print(price, "euros")

def main():
    theta0, theta1 = openCSV()
    km = input("Quel est le kilometrage de la voiture ? ")
    if (km.isnumeric() and int(km) >= 0):
        findPrice(theta0, theta1, int(km))
    else:
        print("ERROR")
        return 1
    return 0

if __name__ == '__main__':
    main()