import os
import sys
import subprocess as sp
from pathlib import PurePath

PARSER_PATH = sys.modules[__name__].__file__

def shp_to_topojson(infile,outfile):
    """
    shp_to_topojson converts a shapefile file
    specification (i.e. a .shp, .dbf, and .shx files) into a topojson.
    This function uses GDAL's ogr2ogr cli-tool
    
    :param infile: string with the path to the input shapefile
    :param outfile: string with the path to the destination topojson
    """
    cmd = "ogr2ogr"
    driver = "GeoJSON"

    st,r = sp.getstatusoutput(cmd + " --version")

    tmp_outfile = infile + ".json"

    if st == 0:
        process_shp = sp.Popen([cmd, "-f", driver, tmp_outfile, infile])
        process_shp.wait()
    else:
        print("Couldn't find {}, please install GDAL".format(cmd))   

    cmd = os.path.join(PurePath(PARSER_PATH).parents[2], "node_modules/topojson-server/bin/geo2topo")

    st,r = sp.getstatusoutput(cmd + " --version")

    if (st == 0) and (process_shp.poll() != None):
        process_geojson = sp.Popen([cmd, tmp_outfile, "--out", outfile])
        process_geojson.wait()
        os.remove(tmp_outfile)
    else:
        print("Couldn't find geo2topo at {}".format(cmd))
