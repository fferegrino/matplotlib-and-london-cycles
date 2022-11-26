import click
from plot import create_plot
import pandas as pd


@click.command()
@click.argument("month")
@click.option("--sample", type=int, required=False, default=0)
def main(month, sample):
    data = pd.read_csv(f"data/{month}.csv.gz", parse_dates=["query_time"])
    selected = data[data["query_time"] == data["query_time"].min()]
    if sample:
        selected = selected.sample(sample, random_state=42)
    print(selected)
    create_plot(selected, out="out/map.png", figsize=(8, 6), dpi=200)


if __name__ == "__main__":
    main()
