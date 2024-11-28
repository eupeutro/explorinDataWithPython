#IMPORTING NECESSARY LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

#GENERATING RANDOM VARIABLES WITH NORMAL DISTRIBUTION
xN10000 = np.random.normal(loc=3, scale=2, size=10000)

#SETTING THE GRAPH SIZE
fig = plt.figure(figsize=(10, 10))

#HISTOGRAM OF NORMAL DISTRIBUTION
xN10000Hist = plt.subplot(2, 2, 1)
xN10000Hist.set_title('xN 10.000 Histogram')
xN10000Hist.hist(xN10000, edgecolor='black', color='yellow', density=True,bins = 30) #INCREASING BINS LEVELS IMPROVES THE GRAPH VISUALIZATION
sns.kdeplot(xN10000, color='black')

#BOXPLOT OF NORMAL DISTRIBUTION
xN10000BoxPlot = plt.subplot(2, 2, 2)
xN10000BoxPlot.set_title('xN10.000 Boxplot')
sns.boxplot(xN10000, color='yellow')

#CALCULATING THE MEAN, MEDIAN, AND MODE
xN10000Mean = np.mean(xN10000)
xN10000Median = np.median(xN10000)
#USING ARRAYS TO SELECT ONLY THE NUMBER INSTEAD OF THE OBJECT
xN10000Mode = stats.mode(xN10000)[0]

#ADDING THE MEAN, MEDIAN, AND MODE TO THE GRAPH
xN10000Hist.text(-8, -0.03, f'Mean of xN10000: {xN10000Mean:.2f}')
xN10000Hist.text(-8, -0.04, f'Median of xN10000: {xN10000Median:.2f}')
xN10000Hist.text(-8, -0.05, f'Mode of xN10000: {xN10000Mode:.2f}')

#CALCULATING VARIANCE, SKEWNESS, AND KURTOSIS
xN10000Variance = np.var(xN10000)
xN10000Skewness = stats.skew(xN10000)
xN10000Kurtosis = stats.kurtosis(xN10000)

#ADDING VARIANCE, SKEWNESS, AND KURTOSIS TO THE GRAPH
xN10000Hist.text(8, -0.03, f'Variance of xN10000: {xN10000Variance:.2f}')
xN10000Hist.text(8, -0.04, f'Skewness of xN10000: {xN10000Skewness:.2f}')
xN10000Hist.text(8, -0.05, f'Kurtosis of xN10000: {xN10000Kurtosis:.2f}')

#ADDING CAPTIONS OF MEAN, MEDIAN AND MODE TO THE HISTOGRAM GRAPH
xN10000Hist.axvline(xN10000Mean, color='blue', linestyle='--', label='Mean')
xN10000Hist.axvline(xN10000Median, color='orange', linestyle='--', label='Median')
xN10000Hist.axvline(xN10000Mode, color='purple', linestyle='--', label='Mode')
xN10000Hist.legend(loc='upper right')

plt.show()
