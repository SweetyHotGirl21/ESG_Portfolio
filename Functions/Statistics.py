import pandas as pd
import numpy as np

def corr_to_cov(corr, st):
    if len(corr) != len(st):
        print("The dimensions don't match")
    variance = np.power(st,2)
    dimension = len(corr)
    covari = np.zeros((dimension,dimension))
    for i in range(dimension):
        covari[i][i] = variance[i]
    for j in range(len(st)):
        for i in range(0,len(st)):
            covari[j][i] = st[j] * st[i] * corr[j][i]
    return np.around(covari, decimals= 4) 