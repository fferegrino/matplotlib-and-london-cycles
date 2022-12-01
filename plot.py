import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

LONGITUDE_PADDING = 0.02
LATITUDE_PADDING = 0.005


def create_plot(data, out, **kwargs):
    fig = plt.figure(**kwargs)
    ax = fig.gca()
    fig.add_axes(ax)

    plot_station_usage(data, fig, ax)

    fig.savefig(out)


def plot_station_usage(data, fig, ax):

    # Calculate map limits
    lats = data["lat"].min() - 0.005, data["lat"].max() + 0.005
    lons = data["lon"].min() - 0.02, data["lon"].max() + 0.02

    # Color the river
    ax.fill_between([lons[0], lons[1]], lats[0], lats[1], color="#81B9E3")

    # Draw map
    london_map = gpd.read_file("shapefiles/London_Borough_Excluding_MHW.shp").to_crs(epsg=4326)
    london_map.plot(ax=ax, color="#F4F6F7", edgecolor="black", linewidth=0.5)

    # Main drawing method
    sns.scatterplot(
        y="lat",
        x="lon",
        hue="occupancy",
        data=data,
        legend=False,
        palette="OrRd",
        s=25,
        edgecolor="k",
        linewidth=0.1,
        ax=ax,
    )

    # Set limits (+padding) and remove axis
    ax.set_ylim(lats[0], lats[1])
    ax.set_xlim(lons[0], lons[1])
    ax.set_axis_off()


def plot_station_usage_v5(data, fig, ax):

    # Draw map
    london_map = gpd.read_file("shapefiles/London_Borough_Excluding_MHW.shp").to_crs(epsg=4326)
    london_map.plot(ax=ax, color="#F4F6F7", edgecolor="black", linewidth=0.5)

    # Main drawing method
    sns.scatterplot(
        y="lat",
        x="lon",
        hue="occupancy",
        data=data,
        legend=False,
        palette="OrRd",
        s=25,
        edgecolor="k",
        linewidth=0.1,
        ax=ax,
    )

    # Set limits (+padding) and remove axis
    lats = data["lat"].min() - 0.005, data["lat"].max() + 0.005
    lons = data["lon"].min() - 0.02, data["lon"].max() + 0.02
    ax.set_ylim(lats[0], lats[1])
    ax.set_xlim(lons[0], lons[1])
    ax.set_axis_off()


def plot_station_usage_v4(data, fig, ax):

    # Draw map
    london_map = gpd.read_file("shapefiles/London_Borough_Excluding_MHW.shp").to_crs(epsg=4326)
    london_map.plot(ax=ax, color="#F4F6F7", edgecolor="black", linewidth=0.5)

    # Main drawing method
    sns.scatterplot(y="lat", x="lon", hue="occupancy", data=data, legend=False, ax=ax)

    # Set limits (+padding) and remove axis
    lats = data["lat"].min() - 0.005, data["lat"].max() + 0.005
    lons = data["lon"].min() - 0.02, data["lon"].max() + 0.02
    ax.set_ylim(lats[0], lats[1])
    ax.set_xlim(lons[0], lons[1])
    ax.set_axis_off()


def plot_station_usage_v3(data, fig, ax):

    # Draw map
    london_map = gpd.read_file("shapefiles/London_Borough_Excluding_MHW.shp").to_crs(epsg=4326)
    london_map.plot(ax=ax)

    # Main drawing method
    sns.scatterplot(y="lat", x="lon", hue="occupancy", data=data, legend=False, ax=ax)

    # Set limits (+padding) and remove axis
    lats = data["lat"].min() - 0.005, data["lat"].max() + 0.005
    lons = data["lon"].min() - 0.02, data["lon"].max() + 0.02
    ax.set_ylim(lats[0], lats[1])
    ax.set_xlim(lons[0], lons[1])
    ax.set_axis_off()


def plot_station_usage_v2(data, fig, ax):

    # Draw map
    london_map = gpd.read_file("shapefiles/London_Borough_Excluding_MHW.shp").to_crs(epsg=4326)
    london_map.plot(ax=ax)

    # Main drawing method
    sns.scatterplot(y="lat", x="lon", hue="occupancy", data=data, legend=False, ax=ax)


def plot_station_usage_v1(data, fig, ax):

    # Main drawing method
    sns.scatterplot(y="lat", x="lon", hue="occupancy", data=data, legend=False, ax=ax)
