import matplotlib, os; matplotlib.rcParams["savefig.directory"] = "."
import numpy as np
import pylab as plt
from get_mn_laz_file import get_tile_from_xy
import gpxpy
import gpxpy.gpx
import srtm
import utm


gpx_file = open('Morning_Run.gpx', 'r')
gpx = gpxpy.parse(gpx_file)
elevations = []
X = []
Y = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            x, y,_,_ = utm.from_latlon(point.latitude,point.longitude)
            X.append(x)
            Y.append(y)
            elevations.append(point.elevation)

elevation_data = srtm.get_data()
elevation_data.add_elevations(gpx)
elevations2 = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            elevations2.append(point.elevation)

# elevation_data.add_elevations(gpx, smooth=True)
# elevations3 = []
# for track in gpx.tracks:
#     for segment in track.segments:
#         for point in segment.points:
#             elevations3.append(point.elevation)


X = np.array(X)
Y = np.array(Y)
distances = np.sqrt((np.roll(X,1)-X)**2 + (np.roll(Y,1)-Y)**2)
plt.plot(np.cumsum(distances)/5280, elevations)
plt.plot(np.cumsum(distances)/5280, elevations2)
#plt.plot(np.cumsum(distances)/5280, elevations3)
plt.show()

tiles = set()
for x,y in zip(X,Y):
    tiles.add(get_tile_from_xy(x,y))
