#IMPORTING NECESSARY LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

#GENERATING RANDOM VARIABLES WITH NORMAL DISTRIBUTION
xN = np.random.normal(loc=3, scale=2, size=1000)

#SETTING THE GRAPH SIZE
fig = plt.figure(figsize=(10, 10))

#HISTOGRAM OF NORMAL DISTRIBUTION
xNHist = plt.subplot(2, 2, 1)
xNHist.set_title('xN Histogram')
xNHist.hist(xN, edgecolor='black', color='yellow', density=True)
sns.kdeplot(xN, color='black')

#BOXPLOT OF NORMAL DISTRIBUTION
xNBoxPlot = plt.subplot(2, 2, 2)
xNBoxPlot.set_title('xN Boxplot')
sns.boxplot(xN, color='yellow')

#CALCULATING THE MEAN, MEDIAN, AND MODE
xNMean = np.mean(xN)
xNMedian = np.median(xN)
#USING ARRAYS TO SELECT ONLY THE NUMBER INSTEAD OF THE OBJECT
xNMode = stats.mode(xN)[0]

#ADDING THE MEAN, MEDIAN, AND MODE TO THE GRAPH
xNHist.text(-8, -0.03, f'Mean of xN: {xNMean:.2f}')
xNHist.text(-8, -0.04, f'Median of xN: {xNMedian:.2f}')
xNHist.text(-8, -0.05, f'Mode of xN: {xNMode:.2f}')

#CALCULATING VARIANCE, SKEWNESS, AND KURTOSIS
xNVariance = np.var(xN)
xNSkewness = stats.skew(xN)
xNKurtosis = stats.kurtosis(xN)

#ADDING VARIANCE, SKEWNESS, AND KURTOSIS TO THE GRAPH
xNHist.text(8, -0.03, f'Variance of xN: {xNVariance:.2f}')
xNHist.text(8, -0.04, f'Skewness of xN: {xNSkewness:.2f}')
xNHist.text(8, -0.05, f'Kurtosis of xN: {xNKurtosis:.2f}')

#ADDING CAPTIONS OF MEAN, MEDIAN AND MODE TO THE HISTOGRAM GRAPH
xNHist.axvline(xNMean, color='blue', linestyle='--', label='Mean')
xNHist.axvline(xNMedian, color='orange', linestyle='--', label='Median')
xNHist.axvline(xNMode, color='purple', linestyle='--', label='Mode')
xNHist.legend(loc='upper right')

plt.show()
