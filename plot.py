import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd


def create_plot(data, out, **kwargs):
    fig = plt.figure(**kwargs)
    ax = fig.gca()
    fig.add_axes(ax)

    plot_station_usage(data, fig, ax)

    fig.savefig(out)


def plot_station_usage(data, fig, ax):

    # Draw map
    london_map = gpd.read_file("london-cycles-db/shapefiles/London_Borough_Excluding_MHW.shp").to_crs(epsg=4326)
    london_map.plot(ax=ax)

    # Main drawing method
    sns.scatterplot(y="lat", x="lon", hue="occupancy", data=data, legend=False, ax=ax)


def plot_station_usage_v1(data, fig, ax):

    # Main drawing method
    sns.scatterplot(y="lat", x="lon", hue="occupancy", data=data, legend=False, ax=ax)
