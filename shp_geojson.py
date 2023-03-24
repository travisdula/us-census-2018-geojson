import json
import os

import shapefile

for file in os.listdir("./data"):
    if file.endswith(".zip"):
        name = file[:-4]
        geojson_data = shapefile.Reader("./data/"+name).__geo_interface__
        with open ("./json/"+name+".json", "w") as f:
            json.dump(geojson_data, f)
