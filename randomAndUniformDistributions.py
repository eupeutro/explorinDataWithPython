#IMPORTING NECESSARY LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

#GENERATING RANDOM VARIABLES WITH UNIFORM DISTRIBUTION
xU = np.random.uniform(low=-3, high=6, size=1000)

#SETTING THE GRAPH SIZE
fig = plt.figure(figsize=(10, 10))

#HISTOGRAM OF UNIFORM DISTRIBUTION
xUHist = plt.subplot(2, 2, 1)
xUHist.set_title('xU Histogram')
xUHist.hist(xU, edgecolor='black', density=True, color='green')
sns.kdeplot(xU, color='black')

#BOXPLOT OF UNIFORM DISTRIBUTION
xUBoxPlot = plt.subplot(2, 2, 2)
xUBoxPlot.set_title('xU Boxplot')
xUBoxPlot = sns.boxplot(xU, color='green')

#CALCULATING THE MEAN, MEDIAN, AND MODE
xUMean = np.mean(xU)
xUMedian = np.median(xU)
#USING ARRAYS TO SELECT ONLY THE NUMBER INSTEAD OF THE OBJECT
xUMode = stats.mode(xU)[0]

#ADDING MEAN, MEDIAN, AND MODE TO THE HISTOGRAM
xUHist.text(-8, -0.015, f'Mean of xU: {xUMean:.2f}')
xUHist.text(-8, -0.025, f'Median of xU: {xUMedian:.2f}')
xUHist.text(-8, -0.035, f'Mode of xU: {xUMode:.2f}')

#ADDING CAPTIONS OF MEAN, MEDIAN E MODE TO THE GRAPH
xUHist.axvline(xUMean, color='blue', linestyle='--', label='Mean')
xUHist.axvline(xUMedian, color='orange', linestyle='--', label='Median')
xUHist.axvline(xUMode, color='purple', linestyle='--', label='Mode')
xUHist.legend(loc='upper right')

#CALCULATING VARIANCE, SKEWNESS, AND KURTOSIS
xUVariance = np.var(xU)
xUSkewness = stats.skew(xU)
xUKurtosis = stats.kurtosis(xU)

#ADDING VARIANCE, SKEWNESS, AND KURTOSIS TO THE GRAPH
xUHist.text(8, -0.015, f'Variance of xU: {xUVariance:.2f}')
xUHist.text(8, -0.025, f'Skewness of xU: {xUSkewness:.3f}')
xUHist.text(8, -0.035, f'Kurtosis of xU: {xUKurtosis:.2f}')

#DISPLAYING THE GRAPH
plt.show()
