import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

EKG = pd.read_csv("../MIT-BIH_Arrhythmia/100.csv", header=None)

plotData = EKG[2:500]

np.set_printoptions(threshold=np.nan)
print(plotData)

x = np.asarray(plotData[0])
y = np.asarray(pd.to_numeric(plotData[1]))

plt.plot(y)
plt.ylabel("mV")
plt.xlabel("Index n * 0.003")
plt.show()

'''
cA4 = coeffs[0]
cD4 = coeffs[1]['d']
cD3 = coeffs[2]['d']
cD2 = coeffs[3]['d']
cD1 = coeffs[4]['d']
#cA4, cD4, cD3, cD2, cD1 = coeffs
'''

'''
plotWave(cD1, "cD1", "Index 2n * 0.003")
plotWave(cD2, "cD2", "Index 3n * 0.003")
plotWave(cD3, "cD3", "Index 4n * 0.003")
plotWave(cD4, "cD4", "Index 5n * 0.003")
plotWave(cA4, "cA4", "Index 5n * 0.003")
'''