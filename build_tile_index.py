from glob import glob
import os
import json

data = {}


def get(line):
    return tuple(map(float,line.split(":")[1].strip().split(" ")))

def mid(minp, maxp, sf=None):
    if sf is None:
        sx = 1
        sy = 1
        sz = 1
    else:
        sx,sy,sz = sf
    return (sx*(minp[0]+maxp[0])/2.0,
            sy*(minp[1]+maxp[1])/2.0,
            sz*(minp[2]+maxp[2])/2.0)

for filename in glob("index/lasinfo/*.txt"):
    with open(filename, "r", encoding="Latin1") as f:
        sf = minp = maxp = None
        while True:
            line = f.readline()
            line = line.strip()
            if line.startswith("scale factor x y z:"):
                sf = get(line)
            elif line.startswith("min x y z:"):
                minp = get(line)
            elif line.startswith("max x y z:"):
                maxp = get(line)
                break

        assert sf
        assert minp
        assert maxp

        data[os.path.basename(filename)] = minp, maxp, mid(minp,maxp)[:2]

            # scale factor x y z:         0.01 0.01 0.01
            # offset x y z:               0 0 0
            # min x y z:                  648457.84 5342535.24 436.18
            # max x y z:                  650868.99 5346068.84 532.61
json.dump(data, open("tile_index.json", "w"))
