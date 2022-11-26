from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import pytz

london_tz = pytz.timezone("Europe/London")


def read_stations(beginning, end):

    _beginning = datetime(beginning.year, beginning.month, beginning.day) - timedelta(days=1)
    _end = datetime(end.year, end.month, end.day) + timedelta(days=1)

    dates = [(_beginning + timedelta(days=days)).strftime("%Y-%m-%d") for days in range((_end - _beginning).days + 1)]

    # Read data from the CSV files
    station_info = []
    for date in dates:
        csv_file = Path("london-cycles-db/data/", f"{date}.csv")
        if not csv_file.exists():
            continue
        station_info.append(pd.read_csv(csv_file, parse_dates=["query_time"]))
    all_data = pd.concat(station_info)

    # Bin data to 15 minutes
    all_data["query_time"] = pd.to_datetime(
        all_data["query_time"].dt.tz_localize("utc").dt.tz_convert(london_tz).dt.floor("15min", ambiguous=True)
    )

    # TODO: Fix division by zero, then we can delete this line
    all_data = all_data[all_data["docks"] != 0]

    all_data["occupancy"] = (all_data["docks"] - all_data["empty_docks"]) / all_data["docks"]
    all_data["occupancy"] = all_data["occupancy"].astype(float)

    # Interpolate to fill gaps
    def interpolate_bikepoint(dataframe):
        resampled = dataframe.copy()
        resampled = resampled.set_index("query_time")
        resampled = resampled.resample("15min")[["lat", "lon", "occupancy"]].median()
        resampled = resampled.interpolate()
        return resampled.reset_index()

    if beginning and end:
        data_to_plot = all_data[(all_data["query_time"] >= beginning) & (all_data["query_time"] <= end)]
    else:
        data_to_plot = all_data

    resampled_frames = []

    for bikepoint in data_to_plot["place_id"].unique():
        resampled = interpolate_bikepoint(data_to_plot[data_to_plot["place_id"] == bikepoint])
        resampled["place_id"] = bikepoint
        resampled_frames.append(resampled)

    data_to_plot = pd.concat(resampled_frames)

    return data_to_plot
