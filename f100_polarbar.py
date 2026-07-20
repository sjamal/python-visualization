import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show

df = pd.read_csv('Downloads/f100rads.csv')  # Update path to actual CSV location
grouped = df.groupby('Company')[['PLB','PRB']].sum()
source = ColumnDataSource(grouped)
f100 = source.data['Company'].tolist()
p = figure(x_range=f100)

company = source.data['Company'].tolist()
profits = source.data['PRB'].tolist()
donations = source.data['PLB'].tolist()

# Initialise the spider plot by setting figure size and polar projection
plt.figure(figsize=(30, 6))
plt.subplot(polar=True)

theta = np.linspace(0, 2 * np.pi, len(profits))

# Arrange the grid into number of sales equal parts in degrees
lines, labels = plt.thetagrids(range(0, 360, int(360/len(company))), (company))
 
# Plot profits sales graph
plt.plot(theta, profits)

# Plot donations graph
plt.plot(theta, donations)

# Add legend and title for the plot
plt.legend(labels=('2019 Profits', '2020 Donations'), loc=5)
plt.title("Pledges to BLM initiatives by Fortune 100 Companies (June 2020)")

# Dsiplay the plot on the screen
plt.show()