import subprocess as sp

def shp_to_geojson(infile,outfile):
    cmd = "ogr2ogr"
    driver = "\"GeoJSON\""

    st,r = sp.getstatusoutput(cmd + " --version")

    if st == 0:
        process = sp.Popen([cmd, "-f", driver, outfile, infile])
    else:
        print("Couldn't find {}, please install GDAL".format(cmd))    
