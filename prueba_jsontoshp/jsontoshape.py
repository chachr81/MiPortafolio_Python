import json
from shapefile import Writer

# Abrimos el archivo GeoJSON en modo lectura
with open(r"C:\proyectos_dev\python_dev\varios\coordenadas.geojson", "r") as f:
    # Cargamos el contenido del archivo como un objeto JSON
    geojson = json.load(f)

# Creamos un nuevo archivo shapefile
w = Writer(shapeType=1)

# Agregamos los campos x y y al archivo shapefile
w.field("x", "F", decimal=6)
w.field("y", "F", decimal=6)

# Recorremos cada punto en el archivo GeoJSON y agregamos su geometría y registro de campos al archivo shapefile
for feature in geojson["features"]:
    if feature["type"] == "Point":
        w.point(feature["coordinates"][0], feature["coordinates"][1])
        w.record(feature["coordinates"][0], feature["coordinates"][1])

# Establecemos el código EPSG 4326 como sistema de coordenadas para el archivo shapefile
w.prj = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]]'
# type: ignore
# Guardamos el archivo shapefile
w.save(r"C:\proyectos_dev\python_dev\varios\coordenadas.shp")
