get minnesota-latest.osm.pbf from http://download.geofabrik.de/north-america/us.html


Get the Cook county Minnesota outline from here
https://public.opendatasoft.com/explore/dataset/us-county-boundaries/export/?disjunctive.statefp&disjunctive.countyfp&disjunctive.name&disjunctive.namelsad&disjunctive.stusab&disjunctive.state_name&q=cook+mn
save as json.

Convert the json into a poly file with `convert_poly.py`

osmosis --read-xml file=minnesota-latest.osm --bounding-polygon file=cook_county_minnesota.poly --write-xml file=cook_county_mn.osm



https://resources.gisdata.mn.gov/pub/data/elevation/lidar/county/cook/
