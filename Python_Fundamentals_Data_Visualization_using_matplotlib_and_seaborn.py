# Code 1
# import the packages
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

# create random data
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(100.0, 1.0, 1000)

# use matplotlib to plot graph
plt.scatter(x, y)
plt.xlabel("Random Data 1")
plt.ylabel("Random Data 2")
plt.title("Scatter Plot Example")
plt.show()

# use seaborn to plot graph
# uncomment below code and comment the matplotlib to see the plot:

# plotSns = sns.scatterplot(x =x, y=y).set_title("Scatter Plot Example")
# plt.xlabel("Random Data 1")
# plt.ylabel("Random Data 2")

# Code 2
# import the packages
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# create randome data array
randData = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])

# use matplotlib to plot graph
plt.hist(randData, bins = [0,25,50,75,100])
plt.title("Histogram of Result")
plt.xticks([0,25,50,75,100])
plt.xlabel('Marks')
plt.ylabel('No. of Students')
plt.show()

# use seaborn to plot graph
# uncomment below code and comment the matplotlib to see the plot:
# sns.histplot(data = randData).set_title("Histogram of Result")
# plt.xlabel("Marks")
# plt.ylabel("No. of Students")

# Code 3
# import the packages
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# create randome data array
np.random.seed(10) 
data = np.random.normal(100, 10, 200) 
  
# use matplotlib to plot graph
plt.boxplot(data)
plt.title("Boxplot Example")
plt.xlabel('Random Data 1')
plt.ylabel('Random Data 2')
plt.show()  

# use seaborn to plot graph
# uncomment below code and comment the matplotlib to see the plot:
  
# sns.set_theme(style="whitegrid")
# plotSns = sns.boxplot(data = data).set_title("Boxplot Example")
# plt.xlabel("Random Data 1")
# plt.ylabel("Random Data 2")

# Code 4
# import the packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# create random data
data = np.random.random((10,10)) 

# use matplotlib to plot graph
plt.imshow(data,cmap = 'autumn',interpolation = 'nearest')   
plt.title("2-D Heat Map") 
plt.show() 

# use seaborn to plot graph
# uncomment below code and comment the matplotlib to see the plot:
    
# ax = sns.heatmap(data).set_title("2-D Heat Map")

# Code 5
# import the packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime

# create random data
data = np.random.rand(50)
time = pd.date_range(datetime.today(), periods = 50).tolist()

# use matplotlib to plot graph
plt.plot(time,data) 
plt.title("Time-series Example")
plt.xlabel('Time')
plt.ylabel('Random Data 1')
plt.show()

# use seaborn to plot graph
# uncomment below code and comment the matplotlib to see the plot:
    
# sns.lineplot(x = time,y = data).set_title("Time-series Example")
# plt.xlabel('Time')
# plt.ylabel('Random Data 1')