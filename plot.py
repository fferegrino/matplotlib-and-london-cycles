import matplotlib.pyplot as plt
import seaborn as sns


def create_plot(data, out, **kwargs):
    fig = plt.figure(**kwargs)
    ax = fig.gca()
    fig.add_axes(ax)

    plot_station_usage(data, fig, ax)
    
    fig.savefig(out)


def plot_station_usage(data, fig, ax):

    # Main drawing method
    sns.scatterplot(y="lat", x="lon", hue="occupancy", data=data, legend=False, ax=ax)
