import pandas as pd
import nvd3
from IPython.display import Image
import matplotlib
from matplotlib import pyplot as plt
from IPython.core.display import display, HTML
from nvd3 import lineChart
#
df = pd.read_csv(r"/home/varun/q4-3.1-table.csv")
df = pd.DataFrame(df)
#
output_file = open('Literacy_rate.html', 'w')
chart = lineChart(width = 1000,name="lineChart", x_is_date=False, x_axis_format=None)
#
xdata = df['Year']
y1 = df['Rural Female']
y2 = df['Rural Male']
y3 = df['Urban Female']
y4 = df['Urban Male']
extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
chart.add_serie(y=y1, x=xdata, name='Rural Female', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y2, x=xdata, name='Rural Male', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
chart.add_serie(y=y3, x=xdata, name='Urban Female', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y4, x=xdata, name='Urban Male', extra=extra_serie)
#
chart.set_containerheader("<h2>Sex wise Literacy rate among Rural & Urban India<h2>")
chart.buildhtml()
display(Image(chart.htmlcontent))
output_file.write(chart.htmlcontent)
output_file.close()