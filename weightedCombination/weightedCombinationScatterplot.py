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
xSum =2*xN+xU/3

#SETTING THE GRAPH SIZE
fig = plt.figure(figsize=(10, 10))

#SCATTERPLOT xN x xSum
xNxSumScatter = plt.subplot(2, 2, 1)
#USING AX ARG TO ASSIGN THE AXES OBJECT
sns.scatterplot(x = xN, y=xSum, ax=xNxSumScatter)
xNxSumScatter.set_title('Scatterplot xN x xSum')

#SCATTERPLOT xN x xU
xNxUScatter = plt.subplot(2, 2, 2)
#USING AX ARG TO ASSIGN THE AXES OBJECT
sns.scatterplot(x = xN, y=xU, ax=xNxUScatter, color = 'green')
xNxUScatter.set_title('Scatterplot xN x xU')

#GRAPHS GENERATED ARE TOTALLY DISTINCTS


plt.show()

