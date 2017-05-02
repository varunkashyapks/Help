import pandas as pd
import nvd3
from nvd3 import multiBarChart
from IPython.display import Image
from IPython.core.display import display, HTML

df= pd.read_csv("/home/varun/q2-2.4-table.csv")
# saving a file into HTML file
output_file = open('secondone.html', 'w')
chart = multiBarChart(width=1000, height=400, x_axis_format=None,color = 'green')
xdata = df['Period']
One = df['Rural Female']
Two = df['Rural Male']

chart.add_serie(name="Rural Female", y=One, x=xdata)
chart.add_serie(name="Rural Male", y=Two, x=xdata)

chart.buildhtml()
display(HTML(chart.htmlcontent))
output_file.write(chart.htmlcontent)

# close HTML file
output_file.close()