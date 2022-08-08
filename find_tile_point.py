import json
from scipy.spatial import cKDTree
import utm
from get_mn_laz_file import get_laz_tile
import numpy as np
import pandas as pd
import matplotlib; matplotlib.rcParams["savefig.directory"] = "."
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 18})


cabin = 47.82009580911151, -90.10145633950037
*cabin,_,_ = utm.from_latlon(*cabin)

land_boundaries = ((47.820372,     -90.102616),
                   (47.8185696,   -90.1026207),
                   (47.8185901  -90.100027),
                   (47.8203893  -90.1000255))

# parcel ID
# 55-229-3350

time_index = json.load(open("tile_index.json"))

names = []
mid_points = []

x, y = [],[]

for name, (_, _, midp) in time_index.items():
    names.append(name)
    mid_points.append(midp)
    x.append(midp[0])
    y.append(midp[1])
    #plt.text(x[-1], y[-1], name)
# plt.plot(x,y, "o")
# plt.plot(cabin[0], cabin[1], "o", color="red")
# plt.show()

tree = cKDTree(mid_points)
cabin_tile = names[tree.query(cabin)[1]]

cabin_laz = cabin_tile.replace(".txt", ".laz")

local_fn = get_laz_tile(cabin_laz)

import laspy
import open3d as o3d

las = laspy.read(local_fn)

point_data = np.stack([las.X, las.Y, las.Z], axis=0).transpose((1, 0))
geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])

# how to look up
