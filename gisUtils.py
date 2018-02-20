import argparse
import gis_utils.out_parsers as op

parser = argparse.ArgumentParser(description="Convert between Shapefiles, GeoJSON, and TopoJSON through wrappers and pure-python implementations of GIS format converters")

## Add the list of arguments
parser.add_argument('-is', '--in_shapefile', help="Shapefile format for input file.", type=str)
parser.add_argument('-ig', '--in_geojson', help="GeoJSON format for input file.", type=str)
parser.add_argument('-it', '--in_topojson', help="TopoJSON format for input file.", type=str)
parser.add_argument('-os', '--out_shapefile', help="Shapefile format for output file.", type=str)
parser.add_argument('-og', '--out_geojson', help="GeoJSON format for output file.", type=str)
parser.add_argument('-ot', '--out_topojson', help="TopoJSON format for output file.", type=str)

## Parse the input arguments 
args = parser.parse_args()

dict_args = vars(args)

## Organizing arguments
in_shapefile = args.in_shapefile
in_geojson = args.in_geojson
in_topojson = args.in_topojson
out_shapefile = args.out_shapefile
out_geojson = args.out_geojson
out_topojson = args.out_topojson

# The input files are the ones that make
# the conversion available
if in_shapefile != None:
    if out_geojson != None:
        op.shp_to_geojson(in_shapefile, out_geojson)
    
    if out_topojson != None:
        op.shp_to_topojson(in_shapefile, out_topojson)
    
if in_geojson != None:
    if out_shapefile != None:
        op.geojson_to_shp(in_geojson, out_shapefile)
    
    if out_topojson != None:
        op.geojson_to_topojson(in_geojson, out_topojson)
        
if in_topojson != None:
    if out_shapefile != None:
        op.topojson_to_geojson(in_topojson, out_geojson)

    if out_geojson != None:
        op.topojson_to_geojson(in_topojson, out_geojson)
