import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as ticker
def draw_straight_line_on_red_xaxis(plt):
  #import matplotlib.pyplot as plt
  #
  fig = plt.figure()
  fig.canvas.set_window_title('Matplotlib Experiments')
  ax = fig.add_subplot(2,2,1,axisbg=(0,0,0.2,0.7))
  ax2 = fig.add_subplot(222,axisbg=(0,0.5,0.6,0.7))
  #
  ax.plot(range(10))
  ax2.plot([5,4,4])
  ax.set_xlabel('X-axis')
  ax.set_ylabel('Y-axis')
  ax2.set_xlabel('name')
  ax2.set_ylabel('rate')
  #
  ax.spines['bottom'].set_color('red')
  ax.spines['left'].set_color('red')
  ax.xaxis.label.set_color('red')
  ax.tick_params(axis='x', colors='red')
  #
  plt.show()
draw_straight_line_on_red_xaxis(plt)