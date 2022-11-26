import click
from datetime import datetime
from plot import create_plot
from read import read_stations
import pytz

london_tz = pytz.timezone("Europe/London")


@click.command()
@click.option("--sample", type=int, required=False, default=0)
def main(sample):
    beginning = datetime(2022, 11, 7, tzinfo=london_tz)
    end = datetime(2022, 11, 14, tzinfo=london_tz)
    data = read_stations(beginning, end)

    selected = data[data["query_time"] == data["query_time"].min()]
    if sample:
        selected = selected.sample(sample, random_state=42)
    print(selected)
    create_plot(selected, out="out/map.png")


if __name__ == "__main__":
    main()
