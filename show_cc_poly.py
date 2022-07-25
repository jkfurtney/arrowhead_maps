import numpy as np
import pandas as pd
import matplotlib; matplotlib.rcParams["savefig.directory"] = "."
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 18})

x,y = np.genfromtxt("cook_county_minnesota.poly", skip_header=2, skip_footer=2).T
plt.plot(x,y,"-o")
plt.gca().set_aspect(1)
plt.show()
