import os 
import geojson
import shapefile
import multiprocessing as mp

def geojson_to_shp(geojson_file_name,shp_file_name=None):
    """
    Converts a geojson file into a shapefile. This is a serial process
    """
    if shp_file_name == None:
        shp_file_name = geojson_file_name.split(os.path.sep)[-1].split(".")[0]

    # Open the GeoJSON and load it to memory
    geoj = geojson.load(open(geojson_file_name,"r"))

    w = shapefile.Writer()

    # Get the number of features
    features = len(geoj["features"])
    
    i = 0
    while i < features:
        # Paranoid to prevent exceptions u
        try:
            w.shape(geoj[i]["geometry"])
        except:
            break
        i += 1

    w.save('test.shp')
