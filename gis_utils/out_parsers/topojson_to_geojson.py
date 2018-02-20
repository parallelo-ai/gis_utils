import os
import sys
import subprocess as sp
from pathlib import PurePath

PARSER_PATH = sys.modules[__name__].__file__

def topojson_to_geojson(infile,outfile):
    cmd = os.path.join(PurePath(PARSER_PATH).parents[2],"node_modules/topojson-client/bin/topo2geo")
    
    st,r = sp.getstatusoutput(cmd + " --version")

    if st == 0:
        process = sp.Popen([cmd, infile, "--out", outfile])
    else:
        print("Couldn't find topo2geo at {}".format(cmd))
