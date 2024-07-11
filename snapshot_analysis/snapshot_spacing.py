import numpy as np
import pandas as pd
from astropy import units as units
from astropy.io import ascii
from matplotlib import pyplot as plt

DATA_FOLDER = "data/"
SNAPSHOT_FILE = "snapshot_times.txt"
SNAPSHOT_TIMES = "flathub_snaps.txt"

with open(DATA_FOLDER + SNAPSHOT_FILE) as f:
    s_output = f.readlines()
    s_output = s_output[5:]

data = ascii.read(s_output)
snap = pd.read_csv(DATA_FOLDER + SNAPSHOT_TIMES)

data["time[Gyr]"].name = "time"
data["time"].unit = units.Gyr

data["lookback-time[Gyr]"].name = "lookback-time"
data["lookback-time"].unit = units.Gyr

data["time-width[Myr]"].name = "time-width"
data["time-width"].unit = units.Myr

snap = snap.sort_values(by=["snaps"])
snap = snap.reset_index(drop=True)

z_snap = []
lookback_snap = []
time_snap = []

for i in snap["snaps"]:
    z_snap.append(data["redshift"][i])
    time_snap.append(data["time"][i])
    lookback_snap.append(data["lookback-time"][i])

y0 = [0.5] * len(data["lookback-time"])
y1 = [-0.5] * len(lookback_snap)

fig, axs = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(hspace=0)

bins = np.linspace(0, 14, 29)

axs[0].hist(data["lookback-time"], bins=bins, color="lightgrey", edgecolor="darkgrey")
axs[0].hist(lookback_snap, bins=bins, color="royalblue", edgecolor="navy")
axs[0].axvspan(8, 11, color="crimson", alpha=0.1)

axs[1].scatter(data["lookback-time"], y0, color="lightgrey", edgecolor="darkgrey", label="FIRE Full")
axs[1].scatter(lookback_snap, y1, color="royalblue", edgecolor="navy", label="FIRE FlatHub")

axs[1].set_ylim([-2, 2])
axs[1].set_yticks([])

axs[1].axvspan(8, 11, color="crimson", alpha=0.1)

axs[0].set_ylabel("Bin Count")
axs[1].set_xlabel("Lookback Time (Gyr)")

axs[1].legend()

plt.show()
