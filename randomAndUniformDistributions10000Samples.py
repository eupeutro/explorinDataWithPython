#IMPORTING NECESSARY LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

#GENERATING RANDOM VARIABLES WITH UNIFORM DISTRIBUTION
xU10000 = np.random.uniform(low=-3, high=6, size=10000)

#SETTING THE GRAPH SIZE
fig = plt.figure(figsize=(10, 10))

#HISTOGRAM OF UNIFORM DISTRIBUTION
xU10000Hist = plt.subplot(2, 2, 1)
xU10000Hist.set_title('xU*10000 Histogram')
xU10000Hist.hist(xU10000, edgecolor='black', density=True, color='green',bins=30) #INCREASING BINS LEVELS IMPROVES THE GRAPH VISUALIZATION
sns.kdeplot(xU10000, color='black')

#BOXPLOT OF UNIFORM DISTRIBUTION
xU10000BoxPlot = plt.subplot(2, 2, 2)
xU10000BoxPlot.set_title('xU*10000 Boxplot')
xU10000BoxPlot = sns.boxplot(xU10000, color='green')

#CALCULATING THE MEAN, MEDIAN, AND MODE
xU10000Mean = np.mean(xU10000)
xU10000Median = np.median(xU10000)
#USING ARRAYS TO SELECT ONLY THE NUMBER INSTEAD OF THE OBJECT
xU10000Mode = stats.mode(xU10000)[0]

#ADDING MEAN, MEDIAN, AND MODE TO THE GRAPH
xU10000Hist.text(-5, -0.03, f'Mean of xU*10000: {xU10000Mean:.2f}')
xU10000Hist.text(-5, -0.04, f'Median of xU*10000: {xU10000Median:.2f}')
xU10000Hist.text(-5, -0.05, f'Mode of xU*10000: {xU10000Mode:.2f}')

#ADDING CAPTIONS OF MEAN, MEDIAN E MODE TO THE GRAPH
xU10000Hist.axvline(xU10000Mean, color='blue', linestyle='--', label='Mean')
xU10000Hist.axvline(xU10000Median, color='orange', linestyle='--', label='Median')
xU10000Hist.axvline(xU10000Mode, color='purple', linestyle='--', label='Mode')
xU10000Hist.legend(loc='upper right')


#CALCULATING VARIANCE, SKEWNESS, AND KURTOSIS
xU10000Variance = np.var(xU10000)
xU10000Skewness = stats.skew(xU10000)
xU10000Kurtosis = stats.kurtosis(xU10000)

#ADDING VARIANCE, SKEWNESS, AND KURTOSIS TO THE GRAPH
xU10000Hist.text(8, -0.03, f'Variance of xU*10000: {xU10000Variance:.2f}')
xU10000Hist.text(8, -0.04, f'Skewness of xU*10000: {xU10000Skewness:.2f}')
xU10000Hist.text(8, -0.05, f'Kurtosis of xU*10000: {xU10000Kurtosis:.2f}')

#DISPLAYING THE GRAPH
plt.show()
