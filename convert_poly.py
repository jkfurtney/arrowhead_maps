import json
import numpy as np

data = np.array(json.load(open("us-county-boundaries.json"))[0]["fields"]["geo_shape"]["coordinates"])[0]

with open("cook_county_minnesota.poly", "w") as f:
    print("polygon\n1", file=f)
    np.savetxt(f, data)
    print("END\nEND\n", file=f)
