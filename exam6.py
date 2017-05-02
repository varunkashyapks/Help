import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
from IPython.core.display import display, HTML
import seaborn as sns 

df = pd.read_csv("/home/varun/q6-5.10-table.csv")
var = sns.barplot(x='Name of the Court', y='Female',data =df,color = 'yellow')
var.axes.set_title('Regions vs Average NAR')
var.set(xlabel='Regions', ylabel='Average NAR')
plt.show()