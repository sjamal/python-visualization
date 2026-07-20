# Python Visualization

Python scripts for generating interactive and static data visualizations. Includes Fortune 100 comparative analysis charts built with Bokeh and Matplotlib, demonstrating polar, radial, and bar chart techniques.

## Purpose

Visualization scripts focus on:
- Interactive visualizations with Bokeh
- Static plots with Matplotlib
- Data storytelling through graphics
- Publication-ready figures
- Exploratory visualization

## Scripts

### graph_f100.py
Bokeh bar chart visualization of Fortune 100 company contributions and profits.

**Features:**
- Multiple bar series
- Legend and styling
- Interactive hover tooltips
- Color palettes

**Usage:**
```bash
python scripts/visualization/graph_f100.py
```

### graph_f100_burtin.py
Radial/Burtin visualization of Fortune 100 contributions vs profits.

**Features:**
- Circular radial layout
- Multiple data dimensions
- Company labels and positioning
- Color coding by earnings

**Usage:**
```bash
python scripts/visualization/graph_f100_burtin.py
```

### f100_polarbar.py
Polar bar chart (radar plot) of Fortune 100 data.

**Features:**
- Polar coordinates
- Multiple series
- Legend
- Matplotlib-based

**Usage:**
```bash
python scripts/visualization/f100_polarbar.py
```

## Common Visualization Patterns

### Matplotlib
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Series 1')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.legend()
plt.title('Plot Title')
plt.savefig('output.png', dpi=300)
plt.show()
```

### Bokeh
```python
from bokeh.plotting import figure, output_file, show

p = figure(title="Title", x_axis_label='X', y_axis_label='Y')
p.vbar(x=categories, top=values, width=0.8)

output_file('plot.html')
show(p)
```

## Recommended Packages

- **matplotlib**: Static visualization
- **bokeh**: Interactive web visualization
- **seaborn**: Statistical visualization
- **plotly**: Interactive plots

## File Naming

Use descriptive names:
- `plot_*.py` for individual plots
- `viz_*.py` for visualization workflows
- `visualize_*.py` for data visualization

## Related Projects

- [python-sysadmin-tools](https://github.com/sjamal/python-sysadmin-tools) — Infrastructure auditing and VM sizing utilities
- [python-data-processing](https://github.com/sjamal/python-data-processing) — ETL and data transformation pipelines
- [python-machine-learning](https://github.com/sjamal/python-machine-learning) — Model training and evaluation scripts
- [python-utilities](https://github.com/sjamal/python-utilities) — Shared helper functions and utilities
- [python-visualization](https://github.com/sjamal/python-visualization) — Data visualization scripts
- [python-youtube-tools](https://github.com/sjamal/python-youtube-tools) — YouTube API data collection and analysis
- [r-data-analysis](https://github.com/sjamal/r-data-analysis) — R statistical analysis and visualization