import subprocess as sp

def shp_to_geojson(infile,outfile):
    """
    shp_to_geojson converts a shapefile file
    specification (i.e. a .shp, .dbf, and .shx files) into a geojson.
    This function uses GDAL's ogr2ogr cli-tool
    
    :param infile: string with the path to the input shapefile
    :param outfile: string with the path to the destination geojson
    """
    cmd = "ogr2ogr"
    driver = "GeoJSON"

    st,r = sp.getstatusoutput(cmd + " --version")

    if st == 0:
        process = sp.Popen([cmd, "-f", driver, outfile, infile])
    else:
        print("Couldn't find {}, please install GDAL".format(cmd))    
