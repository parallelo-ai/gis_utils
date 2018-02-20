import os
import sys
import subprocess as sp
from pathlib import PurePath

PARSER_PATH = sys.modules[__name__].__file__

def geojson_to_topojson(infile,outfile):
    cmd = os.path.join(PurePath(PARSER_PATH).parents[2],"node_modules/topojson-server/bin/geo2topo")

    st,r = sp.getstatusoutput(cmd + " --version")

    if st == 0:
        process = sp.Popen([cmd, infile, "--out", outfile])
    else:
        print("Couldn't find geo2topo at {}".format(cmd))
