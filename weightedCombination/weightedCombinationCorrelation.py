#IMPORTING NECESSARY LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
import pandas as pd

#GENERATING RANDOM VARIABLES WITH UNIFORM DISTRIBUTION
xU = np.random.uniform(low=-3, high=6, size=1000)

#GENERATING RANDOM VARIABLES WITH NORMAL DISTRIBUTION
xN = np.random.normal(loc=3, scale=2, size=1000)

#GENERATING A WEIGHTED COMBINATION VARIABLE FROM PREVIOUS VARIABLES "xU" AND "xN"
xSum =2*xN+xU/3

#SETTING THE GRAPH SIZE
fig = plt.figure(figsize=(10, 10))

#CREATING A DATAFRAME WITH xN and xSum
dataxNxSum = pd.DataFrame({'xN':xN, 'xSum':xSum})

#CREATING A DATAFRAME WITH xN and xU
dataxNxU = pd.DataFrame({'xN':xN, 'xU':xU})

#CALCULATING CORRELATION BETWEEN xN and xSum
correlationxNxSum = dataxNxSum.corr()

#CALCULATING CORRELATION BETWEEN xN and xU
correlationxNxU = dataxNxU.corr()

#HEATMAP OF CORRELATION BETWEEN xN and xSum
xNxSumHeatMap = plt.subplot(2,2,1)
sns.heatmap(correlationxNxSum,
            annot = True, #SHOW CORRELATION VALUES
            cmap='coolwarm',
            linewidths = 0.5,
            ax = xNxSumHeatMap,
            fmt = ".2f")
plt.title('Correlation of xN and xSum')

#HEATMAP OF CORRELATION BETWEEN xN and xU
xNxUHeatMap = plt.subplot(2,2,2)
sns.heatmap(correlationxNxU,
            annot = True, #SHOW CORRELATION VALUES
            cmap='coolwarm',
            linewidths = 0.5,
            ax = xNxUHeatMap, #USING AX ARG TO ASSIGN THE AXES OBJEC
            fmt = ".2f")
plt.title('Correlation of xN and xSum')





plt.show()