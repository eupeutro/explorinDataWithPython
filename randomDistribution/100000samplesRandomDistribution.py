#IMPORTING NECESSARY LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

#GENERATING RANDOM VARIABLES WITH NORMAL DISTRIBUTION
xN100000 = np.random.normal(loc=3, scale=2, size=100000)

#SETTING THE GRAPH SIZE
fig = plt.figure(figsize=(10, 10))

#HISTOGRAM OF NORMAL DISTRIBUTION
xN100000Hist = plt.subplot(2, 2, 1)
xN100000Hist.set_title('xN 100.000 Histogram')
xN100000Hist.hist(xN100000, edgecolor='black', color='yellow', density=True,bins=50) #INCREASING BINS LEVELS IMPROVES THE GRAPH VISUALIZATION
sns.kdeplot(xN100000, color='black')

#BOXPLOT OF NORMAL DISTRIBUTION
xN100000BoxPlot = plt.subplot(2, 2, 2)
xN100000BoxPlot.set_title('xN100.000 Boxplot')
sns.boxplot(xN100000, color='yellow')

#CALCULATING THE MEAN, MEDIAN, AND MODE
xN100000Mean = np.mean(xN100000)
xN100000Median = np.median(xN100000)
#USING ARRAYS TO SELECT ONLY THE NUMBER INSTEAD OF THE OBJECT
xN100000Mode = stats.mode(xN100000)[0]

#ADDING THE MEAN, MEDIAN, AND MODE TO THE GRAPH
xN100000Hist.text(-8, -0.03, f'Mean of xN100000: {xN100000Mean:.2f}')
xN100000Hist.text(-8, -0.04, f'Median of xN100000: {xN100000Median:.2f}')
xN100000Hist.text(-8, -0.05, f'Mode of xN100000: {xN100000Mode:.2f}')

#CALCULATING VARIANCE, SKEWNESS, AND KURTOSIS
xN100000Variance = np.var(xN100000)
xN100000Skewness = stats.skew(xN100000)
xN100000Kurtosis = stats.kurtosis(xN100000)

#ADDING VARIANCE, SKEWNESS, AND KURTOSIS TO THE GRAPH
xN100000Hist.text(8, -0.03, f'Variance of xN100000: {xN100000Variance:.2f}')
xN100000Hist.text(8, -0.04, f'Skewness of xN100000: {xN100000Skewness:.2f}')
xN100000Hist.text(8, -0.05, f'Kurtosis of xN100000: {xN100000Kurtosis:.2f}')

#ADDING CAPTIONS OF MEAN, MEDIAN AND MODE TO THE HISTOGRAM GRAPH
xN100000Hist.axvline(xN100000Mean, color='blue', linestyle='--', label='Mean')
xN100000Hist.axvline(xN100000Median, color='orange', linestyle='--', label='Median')
xN100000Hist.axvline(xN100000Mode, color='purple', linestyle='--', label='Mode')
xN100000Hist.legend(loc='upper right')

plt.show()
