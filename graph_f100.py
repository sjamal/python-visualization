# https://programminghistorian.org/en/lessons/visualizing-with-bokeh

import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from math import pi

# Experiment with Magma, Spectral5, Inferno5 or RdGy5
from bokeh.palettes import Magma256
from bokeh.palettes import Inferno5
from bokeh.transform import factor_cmap
from bokeh.models import NumeralTickFormatter
output_file('donations_by_company.html')

df = pd.read_csv('Downloads/f100dons.csv')  # Update path to actual CSV location

grouped = df.groupby('Company')[['Pledged','Profits']].sum()

grouped = grouped / 1000000000

source = ColumnDataSource(grouped)
f100 = source.data['Company'].tolist()

p = figure(x_range=f100)

#p.line(x='Company', y='Profits', line_width=2, source=source, color=Magma256[200], legend_label='2019 Profits')
#p.line(x='Company', y='Pledged', line_width=2, source=source, color=Magma256[100], legend_label='2020 Contributions')

p.vbar(x='Company', top='Profits', source=source, width=1, color=Magma256[240], legend_label='2019 Profits')
p.vbar(x='Company', top='Pledged', source=source, width=1, color=Magma256[75], legend_label='2020 Contributions')

p.title.text = 'Pledges to BLM initiatives by Fortune 100 Companies (June 2020)'
p.title.align = 'center'
#p.background_fill_color = "beige"
#p.background_fill_alpha = 0.5
p.legend.title = 'Source: Fortune magazine'
p.legend.title_text_font_size = "12px"
#p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"
p.legend.label_text_font_size = "12px"
p.legend.location = 'top_right'
p.legend.label_standoff = 5
#p.legend.glyph_width = 50
#p.legend.spacing = 10
#p.legend.padding = 50
#p.legend.margin = 50
#p.xaxis.axis_label = 'Fortune 100 Company Name'
p.xgrid.visible = False
p.xaxis.major_label_orientation = pi/3
p.xaxis.major_label_standoff = 5
#p.ygrid.visible = True
p.ygrid.band_fill_alpha = 0.1
p.ygrid.band_fill_color = "navy"
p.yaxis.axis_label = 'Contributions in Billions compared to 2019 Profits'
#p.yaxis[0].formatter = NumeralTickFormatter(format="$0,00")
#p.xgrid.grid_line_color = None

show(p)
