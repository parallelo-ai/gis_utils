import os
import json
import shapefile
import multiprocessing as mp

def FeatureCollection(features):
    """
    FeatureCollection creates a `FeatureCollection` with the 
    features in `features`
    """
    return {"type": "FeatureCollection","features": features}
    # return {"type": "FeatureCollection","properties":{"features": len(features)},"features": features}


def Feature(iterator):
    """
    Generates a feature provided the iterator `iterator` that 
    implements the __geo__interface__
    """
    return {"type":"Feature", "geometry":iterator.__geo_interface__}


def shp_to_geojson(shp_file_name,geojson_file_name=None):
    """
    Converts a shp file into a geojson file. This 
    uses multiprocessing to critically accelerate the process.
    """
    # If no geojson_file_name is passed, use the shp_file_name without extension
    if geojson_file_name == None:
        geojson_file_name = shp_file_name.split(os.path.sep)[-1].split(".")[0]

    shpfile = shapefile.Reader(shp_file_name)

    pool = mp.Pool()
    features = pool.map(Feature,shpfile.iterShapes())

    f = open(geojson_file_name,"w")
    f.write(json.dumps(FeatureCollection(features),indent=2))
    f.close()
