# %%

import time

import gizmo_analysis as gizmo
import halo_analysis as halo
import matplotlib.pyplot as plt
import numpy as np
import utilities as ut

# start = time.time()

DATA_DIR = "/Volumes/My Passport for Mac/m12i_res7100"

z_591 = 0.001435161
z_592 = 0.001275539

part = gizmo.io.Read.read_snapshots(["star"], "redshift", z_591, simulation_directory=DATA_DIR)

# end = time.time()
# print("Runtime " + str(round(end - start, 2)) + " seconds")

# %%
part.keys()
