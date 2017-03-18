import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
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

'''
Uselessly prints specific detail levels and their corresponding unit conversion back to original
for i in range(1 + 2,levels + 1):
    index = i
    smallK = (levels - i) + 2
    bigK = (levels - i) + 1
    plotWave(coeffs[index]['d'], "cD" + str(bigK), "Index " + str(smallK) + "n * 0.003")
'''

# Don't need anymore since pywavelets is fixed and I can set levels to zeros
# thereby allowing reconstruction to give the full original coordinate system
# ... it was a fun problem to solve though
# Convert x value of level N to original coordinate

def generateLengths(pointsNum, levels):
    lengths = [pointsNum]
    
    for i in range (0,levels):
        if pointsNum % 2 == 0:
            pointsNum = (pointsNum + 6)/2
            lengths.append(pointsNum)
        else:
            pointsNum = (pointsNum + 7)/2
            lengths.append(pointsNum)
    
    return lengths

def getNLevelX(xVal, domain, pointsNum, levels):
    
    lengths = generateLengths(pointsNum, levels)
    index = lengths.index(domain)
    newVal = xVal
    
    while index != 0:
        if lengths[index - 1] % 2 == 0:
            newVal = (newVal * 2) - 6
        else:
            newVal = (newVal * 2) - 7
        index -= 1
    
    return newVal

# Automated way to get graphs for different wavelet types and store the images in folders
def getGraphs(waveletType):
    waveletType = waveletType
    w = pywt.Wavelet(waveletType)
    cA = y
    plotWave(cA, "Original", "Index n * 0.003", waveletType + "/")
    
    for i in range(1,5):
        cA, cD = pywt.dwt(cA, wavelet=w, mode='constant')
        plotWave(cA, "cA" + str(i), "Index " + str(i + 1) + "n * 0.003", waveletType + "/")
        plotWave(cD, "cD" + str(i), "Index " + str(i + 1) + "n * 0.003", waveletType + "/")
       
# Add arrays by element quickly
def addArrays(arrayList):
    return [sum(x) for x in zip(*arrayList)]