import pandas as pd
import nvd3
from nvd3 import multiBarChart
from IPython.display import Image
from IPython.core.display import display, HTML

df= pd.read_csv("/home/varun/q5-4.6-table.csv")
# saving a file into HTML file
output_file = open('allexam3rwre.html', 'w')
chart = multiBarChart(width=1000, height=400, x_axis_format=None,color = 'green')
xdata = df['Year']
One = df['Total']
Two = df['Women']
Three = df['Women1']

chart.add_serie(name="Public Sector", y=One, x=xdata)
chart.add_serie(name="Public Sector", y=Two, x=xdata)
chart.add_serie(name="Public Sector", y=Three, x=xdata)
chart.buildhtml()
display(HTML(chart.htmlcontent))
output_file.write(chart.htmlcontent)

# close HTML file
output_file.close()
#>>> ax = sns.barplot(x="day", y="total_bill", hue="sex", data=tips)