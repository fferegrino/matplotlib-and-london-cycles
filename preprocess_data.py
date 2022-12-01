from pathlib import Path
import pandas as pd
import pytz

london_tz = pytz.timezone("Europe/London")

data = Path("london-cycles-db/data/")

station_info = []
for csv_file in data.glob("*.csv"):
    if csv_file.stem.startswith("stations"):
        continue
    station_info.append(pd.read_csv(csv_file, parse_dates=["query_time"]))
    if len(station_info) == 5:
        break
all_data = pd.concat(station_info)

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


resampled_frames = []
for bikepoint in all_data["place_id"].unique():
    resampled = interpolate_bikepoint(all_data[all_data["place_id"] == bikepoint])
    resampled["place_id"] = bikepoint
    resampled_frames.append(resampled)

data_to_plot = pd.concat(resampled_frames)

data_to_plot["ym"] = data_to_plot["query_time"].dt.strftime("%Y-%m")

for ym in sorted(data_to_plot["ym"].unique()):
    selected = data_to_plot[data_to_plot["ym"] == ym]

    selected[["query_time", "place_id", "lat", "lon", "occupancy"]].sort_values(by="query_time").to_csv(
        f"data/{ym}.csv.gz", index=False, compression='gzip'
    )
