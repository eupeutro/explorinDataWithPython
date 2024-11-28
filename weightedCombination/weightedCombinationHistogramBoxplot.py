#IMPORTING NECESSARY LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats


#GENERATING RANDOM VARIABLES WITH UNIFORM DISTRIBUTION
xU10000 = np.random.uniform(low=-3, high=6, size=10000)

#GENERATING RANDOM VARIABLES WITH NORMAL DISTRIBUTION
xN10000 = np.random.normal(loc=3, scale=2, size=10000)

#GENERATING A WEIGHTED COMBINATION VARIABLE FROM PREVIOUS VARIABLES "xU" AND "xN"
xSum =2*xN10000+xU10000/3

#SETTING THE GRAPH SIZE
fig = plt.figure(figsize=(10, 10))

#HISTOGRAM OF xSum
xSumHist= plt.subplot(2, 2, 1)
xSumHist.set_title('xSum Histogram')
xSumHist.hist(xSum, edgecolor='black', color='orange', density=True,bins=30) #INCREASING BINS LEVELS IMPROVES THE GRAPH VISUALIZATION
sns.kdeplot(xSum, color='black')

#BOXPLOT OF xSum
xSumBoxPlot = plt.subplot(2, 2, 2)
xSumBoxPlot.set_title('xSum Boxplot')
sns.boxplot(xSum, color='orange')

#CALCULATING THE MEAN, MEDIAN, AND MODE
xSumMean = np.mean(xSum)
xSumMedian = np.median(xSum)
#USING ARRAYS TO SELECT ONLY THE NUMBER INSTEAD OF THE OBJECT
xSumMode = stats.mode(xSum)[0]

#ADDING THE MEAN, MEDIAN, AND MODE TO THE GRAPH
xSumHist.text(-14, -0.02, f'Mean of xSum: {xSumMean:.2f}',fontsize = 12)
xSumHist.text(-14, -0.03, f'Median of xSum: {xSumMedian:.2f}',fontsize = 12)
xSumHist.text(-14, -0.04, f'Mode of xSum: {xSumMode:.2f}',fontsize = 12)

#CALCULATING VARIANCE, SKEWNESS, AND KURTOSIS
xSumVariance = np.var(xSum)
xSumSkewness = stats.skew(xSum)
xSumKurtosis = stats.kurtosis(xSum)

#ADDING VARIANCE, SKEWNESS, AND KURTOSIS TO THE GRAPH
xSumHist.text(14, -0.02, f'Variance of xSum: {xSumVariance:.2f}',fontsize = 12)
xSumHist.text(14, -0.03, f'Skewness of xSum: {xSumSkewness:.2f}',fontsize = 12)
xSumHist.text(14, -0.04, f'Kurtosis of xSum: {xSumKurtosis:.2f}',fontsize = 12)

#ADDING CAPTIONS OF MEAN, MEDIAN AND MODE TO THE HISTOGRAM GRAPH
xSumHist.axvline(xSumMean, color='blue', linestyle='--', label='Mean')
xSumHist.axvline(xSumMedian, color='green', linestyle='--', label='Median')
xSumHist.axvline(xSumMode, color='purple', linestyle='--', label='Mode')
xSumHist.legend(loc='upper right')

plt.show()

