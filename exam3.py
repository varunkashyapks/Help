import pandas as pd
import nvd3
from IPython.display import Image
import matplotlib
from matplotlib import pyplot as plt
from IPython.core.display import display, HTML
from nvd3 import lineChart
#
df = pd.read_csv(r"/home/varun/q3-2.6-table.csv")
df = pd.DataFrame(df)
#
output_file = open('mortality.html', 'w')
chart = lineChart(width = 1000,name="lineChart", x_is_date=False, x_axis_format=None)
#
xdata = df['Year']
y1 = df['Assam']
y2 = df['India']
y3 = df['Punjab']
y4 = df['Andhra Pradesh']
y5 = df['Kerala']
extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
chart.add_serie(y=y1, x=xdata, name='Assam', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y2, x=xdata, name='India', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
chart.add_serie(y=y3, x=xdata, name='Punjab', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y4, x=xdata, name='Andra pradesh', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y5, x=xdata, name='Kerala', extra=extra_serie)

chart.set_containerheader("<h2>Trend in Maternal Mortality Rate of India and States with best & worst achievers<h2>")
chart.buildhtml()
display(Image(chart.htmlcontent))
output_file.write(chart.htmlcontent)
output_file.close()