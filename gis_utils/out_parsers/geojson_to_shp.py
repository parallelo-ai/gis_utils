import subprocess as sp

def geojson_to_shp(infile,outfile):
    """
    geojson_to_shp converts a geojson file into a shapefile file
    specification (i.e. a .shp, .dbf, and .shx files)
    
    :param infile: string with the path to the input geojson
    :param outfile: string with the path to the destination shapefile
    """
    cmd = "ogr2ogr"
    driver = "\"ESRI Shapefile\""

    st,r = sp.getstatusoutput(cmd + " --version")

    if st == 0:
        process = sp.Popen([cmd, "-f", driver, outfile, infile])
    else:
        print("Couldn't find {}, please install GDAL".format(cmd))    
