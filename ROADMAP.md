# Roadmap

Planned visualisation scripts. Focus on infrastructure, operational, and data science charts that go beyond standard line/bar plots.

---

## In Progress

_Nothing currently active._

---

## Planned

### Infrastructure & Operations

- [ ] **disk_usage_treemap.py** — Render a treemap of disk usage by mount point and filesystem using Plotly. Input: output from `python-sysadmin-tools` audit scripts.
- [ ] **vm_capacity_dashboard.py** — Multi-panel Bokeh dashboard showing CPU, memory, and disk utilisation per VM. Reads from CSV audit exports. Filterable by environment tier.
- [ ] **network_topology_graph.py** — Visualise host-to-host connectivity as a NetworkX graph rendered with Matplotlib or Plotly. Node colour encodes tier; edge weight encodes traffic volume.
- [ ] **azure_cost_breakdown.py** — Stacked bar chart of Azure spend by resource group and month. Input: Azure cost export CSV. Highlights top-5 cost drivers.

### Time Series & Metrics

- [ ] **metric_timeseries.py** — Multi-series line chart with configurable rolling average overlay. Designed for CPU/memory/disk trend visualisation. Outputs PNG and interactive HTML.
- [ ] **anomaly_overlay.py** — Plot a metric time series with anomaly markers (from `python-machine-learning` outputs) overlaid. Configurable marker style and annotation.
- [ ] **change_calendar.py** — GitHub-style contribution heatmap showing change/incident frequency by day. Useful for identifying busy periods and change freeze effectiveness.

### Data Science

- [ ] **correlation_heatmap.py** — Seaborn heatmap of a feature correlation matrix with configurable masking of the upper triangle. Input: any numeric CSV.
- [ ] **roc_comparison.py** — Plot multiple ROC curves on one axes for model comparison. Reads from `python-machine-learning` evaluation outputs.
- [ ] **distribution_grid.py** — Grid of histograms + KDE curves for all numeric columns in a dataset. Useful for EDA on new data sources.

### Reporting Outputs

- [ ] **report_chart_exporter.py** — Batch export a directory of CSVs as standardised chart PNGs (one per file) using a configurable chart type. Useful for automated reporting pipelines.

---

## Ideas / Backlog

- Interactive Jupyter-based dashboard template for ad hoc infrastructure analysis
- Gantt-style chart for visualising maintenance windows and change schedules
- Sunburst chart for hierarchical infrastructure inventory (region → vnet → host)

---

## Notes

- Prefer Plotly for interactive outputs (HTML), Matplotlib/Seaborn for static exports (PNG/PDF).
- All scripts should accept a `--output` flag to control output path and format.
- Sample data for each chart should be included in `sample-data/`.
