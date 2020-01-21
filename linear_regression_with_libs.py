import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    datas = pd.read_csv('data.csv')
    X = np.array(datas.km)
    Y = np.array(datas.price)
    coef = np.polyfit(X,Y,1)
    poly1d_fn = np.poly1d(coef)
    axes = plt.axes()
    axes.grid()
    plt.plot(X,Y, 'yo', X, poly1d_fn(X))
    plt.xlabel("Kilometrage")
    plt.ylabel("Prix")