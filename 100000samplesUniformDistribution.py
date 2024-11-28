#IMPORTING NECESSARY LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

#GENERATING RANDOM VARIABLES WITH UNIFORM DISTRIBUTION
xU100000 = np.random.uniform(low=-3, high=6, size=100000)

#SETTING THE GRAPH SIZE
fig = plt.figure(figsize=(10, 10))

#HISTOGRAM OF UNIFORM DISTRIBUTION
xU100000Hist = plt.subplot(2, 2, 1)
xU100000Hist.set_title('xU*100.000 Histogram')
xU100000Hist.hist(xU100000, edgecolor='black', density=True, color='green',bins=50)
sns.kdeplot(xU100000, color='black')
#INCREASING BINS LEVELS IMPROVES THE GRAPH VISUALIZATION

#BOXPLOT OF UNIFORM DISTRIBUTION
xU100000BoxPlot = plt.subplot(2, 2, 2)
xU100000BoxPlot.set_title('xU*100.000 Boxplot')
xU100000BoxPlot = sns.boxplot(xU100000, color='green')

#CALCULATING THE MEAN, MEDIAN, AND MODE
xU100000Mean = np.mean(xU100000)
xU100000Median = np.median(xU100000)
#USING ARRAYS TO SELECT ONLY THE NUMBER INSTEAD OF THE OBJECT
xU100000Mode = stats.mode(xU100000)[0]

#ADDING MEAN, MEDIAN, AND MODE TO THE GRAPH
xU100000Hist.text(-8, -0.03, f'Mean of xU*100000: {xU100000Mean:.2f}')
xU100000Hist.text(-8, -0.04, f'Median of xU*100000: {xU100000Median:.2f}')
xU100000Hist.text(-8, -0.05, f'Mode of xU*100000: {xU100000Mode:.2f}')



#ADDING CAPTIONS OF MEAN, MEDIAN AND MODE TO THE HISTOGRAM GRAPH
xU100000Hist.axvline(xU100000Mean, color='blue', linestyle='--', label='Mean')
xU100000Hist.axvline(xU100000Median, color='orange', linestyle='--', label='Median')
xU100000Hist.axvline(xU100000Mode, color='purple', linestyle='--', label='Mode')
xU100000Hist.legend(loc='upper right')


#CALCULATING VARIANCE, SKEWNESS, AND KURTOSIS
xU100000Variance = np.var(xU100000)
xU100000Skewness = stats.skew(xU100000)
xU100000Kurtosis = stats.kurtosis(xU100000)

#ADDING VARIANCE, SKEWNESS, AND KURTOSIS TO THE GRAPH
xU100000Hist.text(8, -0.03, f'Variance of xU*100000: {xU100000Variance:.2f}')
xU100000Hist.text(8, -0.04, f'Skewness of xU*100000: {xU100000Skewness:.2f}')
xU100000Hist.text(8, -0.05, f'Kurtosis of xU*100000: {xU100000Kurtosis:.2f}')

#DISPLAYING THE GRAPH
plt.show()
