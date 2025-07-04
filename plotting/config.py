from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class AxisConfig:
    labels: list[str] = field(default_factory=list)
    ylabel: str = None
    ylim: tuple[float, float] = None
    plot_kwargs: list[dict] = field(default_factory=list)  # List of dicts for each series' styling
    horizontal_lines: Optional[List[float]] = None


@dataclass
class CommonPlotConfig:
    title: Optional[str] = None
    show_title: bool = True
    xlim: tuple[float, float] = None
    figsize: tuple[int, int] = (3.33, 1.7)
    show_legend: bool = True
    legend_kwargs: dict = field(default_factory=dict)
    legend_order: Optional[List[str]] = None
    tight_layout: bool = True
    grid: bool = True
    grid_minor: bool = True
    grid_kwargs: dict = field(default_factory=dict)
    minor_grid_kwargs: dict = field(default_factory=dict)
    minor_ticks: bool = True
    subplots_adjust: dict = None
    time_unit: str = 's'
    output_path: Optional[str] = None

@dataclass
class PlotConfig:
    common: CommonPlotConfig
    primary_axis: AxisConfig
    secondary_axis: AxisConfig = None