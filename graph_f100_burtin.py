from collections import OrderedDict
from io import StringIO
from math import log, sqrt

import numpy as np
import pandas as pd

from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.plotting import figure, output_file, show

fortune = u"""
company,              plb,   prb,    earnings
     Alphabet,             0.038, 34.343, positive
       Amazon.com,           0.01,  11.588, positive
               JPMorgan Chase,       0.003, 36.431, positive
          Cisco Systems,        0.005, 11.621, positive
            Nationwide,           0.001, 0.8297, positive
     Facebook,             0.01,  18.485, positive
            Procter & Gamble,     0.005, 3.897,  positive
       Walt Disney,          0.005, 11.054, positive
               AT&T,                 0.001, 13.903, positive
     TJX,                  0.01,  3.2722, positive
          Anthem,               0.05,  4.807,  positive
     Apple,                0.1,   55.256, positive
            HP,                   0.001, 3.152,  positive
          Bank of America,      1,     27.43,  positive
             Intel,                0.001, 21.048, positive
     Comcast,              0.1,   13.057, positive
               Northrop Grumman,     0.002, 2.248,  positive
Coca-Cola       ,            0.003, 8.92,   positive
Johnson & Johnson      ,    0.01,  15.119, positive
Progressive          ,          0.001, 3.9703, positive
Deere         ,                0.001, 3.253,  positive
UnitedHealth Group      ,   0.01,  13.839, positive
MetLife     ,              0.005, 5.899,  positive
American Express       ,     0.001, 6.759,  positive
State Farm Insurance      , 0.001, 5.5927, positive
Microsoft       ,            0.002, 39.24,  positive
Walmart     ,              0.1,   14.881, positive
Dow     ,                  0.005, -1.359, negative
UPS     ,                  0.004, 4.44,   positive
Boeing     ,               0.025, -0.636, negative
Home Depot       ,           0.001, 11.242, positive
General Motors     ,       0.01,  6.732,  positive
Humana     ,               0.012, 2.707,  positive
PepsiCo     ,              0.4,   7.314,  positive
"""

f100_color = OrderedDict([
    ("Contributions",   "#0d3362"),
    ("Profits", "#c64737"),
])

earn_color = OrderedDict([
    ("negative", "#e69584"),
    ("positive", "#aeaeb8"),
])

df = pd.read_csv(StringIO(fortune),
                 skiprows=1,
                 skipinitialspace=True,
                 engine='python')

width = 800
height = 800
inner_radius = 90
outer_radius = 300 - 10

minr = sqrt(log(.001 * 1E4))
print(minr)
maxr = sqrt(log(1000 * 1E4))
print(maxr)
a = (outer_radius - inner_radius) / (minr - maxr)
print(a)
b = inner_radius - a * maxr
print(b)

def rad(mic):
    return a * np.sqrt(np.log(mic * 1E4)) + b

big_angle = 2.0 * np.pi / (len(df) + 1)
print(big_angle)
small_angle = big_angle / 7
print(small_angle)

p = figure(plot_width=width, plot_height=height, title="",
    x_axis_type=None, y_axis_type=None,
    x_range=(-420, 420), y_range=(-420, 420),
    min_border=0, outline_line_color="black",
    background_fill_color="#f0e1d2")

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# annular wedges
angles = np.pi/2 - big_angle/2 - df.index.to_series()*big_angle
print(angles)
colors = [earn_color[earnings] for earnings in df.earnings]
p.annular_wedge(
    0, 0, inner_radius, outer_radius, -big_angle+angles, angles, color=colors,
)

# small wedges
p.annular_wedge(0, 0, inner_radius, rad(df.prb),
                -big_angle+angles+3*small_angle, -big_angle+angles+4*small_angle,
                color=f100_color['Contributions'])
p.annular_wedge(0, 0, inner_radius, rad(df.plb),
                -big_angle+angles+5*small_angle, -big_angle+angles+6*small_angle,
                color=f100_color['Profits'])

# circular axes and labels
labels = np.power(10.0, np.arange(-3, 4))
radii = a * np.sqrt(np.log(labels * 1E4)) + b
p.circle(0, 0, radius=radii, fill_color=None, line_color="white")
#p.text(0, radii[:-1], [str(r) for r in labels[:-1]],
#       text_font_size="11px", text_align="center", text_baseline="middle")

# radial axes
p.annular_wedge(0, 0, inner_radius-10, outer_radius+10,
                -big_angle+angles, -big_angle+angles, color="black")

# company labels
xr = radii[0]*np.cos(np.array(-big_angle/2 + angles))
yr = radii[0]*np.sin(np.array(-big_angle/2 + angles))
label_angle=np.array(-big_angle/2+angles)
label_angle[label_angle < -np.pi/2] += np.pi # easier to read labels on the left side
p.text(xr, yr, df.company, angle=label_angle,
       text_font_size="12px", text_align="center", text_baseline="middle")

# Label / Legend at base of plot
p.circle([-40, -40], [-370, -390], color=list(earn_color.values()), radius=5)
p.text([-30, -30], [-370, -390], text=["Earnings: " + gr for gr in earn_color.keys()],
       text_font_size="10px", text_align="left", text_baseline="middle")

# Label / Legend at center of plot
p.rect([-40, -40, -40], [18, 0, -18], width=30, height=13,
       color=list(f100_color.values()))
p.text([-15, -15, -15], [18, 0, -18], text=list(f100_color),
       text_font_size="11px", text_align="left", text_baseline="middle")

# Title header of plot
p.title.text = 'Radial bar graph representation of Fortune 100 contributions to social justice causes'
p.title.align = 'center'

output_file("fortune_burtin.html", title="Radial polar bar graph representation of BLM pledge amounts by Fortune 100 companies (June 2020)")

show(p)