import geojson

# Generamos una lista de coordenadas como la que hemos generado anteriormente
coordenadas = [(-67.68, 10.24), (-67.58, 10.30), (-67.50, 10.35),
               (-67.08, 10.24), (-67.14, 10.30), (-67.20, 10.37),
               (-70.66, -33.45), (-70.60, -33.42), (-70.57, -33.40),
               (-70.62, -33.38), (-70.65, -33.41), (-70.68, -33.45)]

# Creamos una lista vacía donde almacenaremos los puntos del archivo GeoJSON
puntos = []

# Iteramos sobre la lista de coordenadas
for x, y in coordenadas:
    # Creamos un punto utilizando las coordenadas x e y
    punto = geojson.Point((x, y))

    # Agregamos el punto a la lista de puntos
    puntos.append(punto)

# Creamos una FeatureCollection con la lista de puntos
feature_collection = geojson.FeatureCollection(puntos)

# Convertimos la FeatureCollection a un formato GeoJSON
geojson_str = geojson.dumps(feature_collection)

# Imprimimos el contenido del archivo GeoJSON
# print(geojson_str)

# Abrimos un archivo en modo escritura
with open('coordenadas.geojson', 'w') as f:
    # Escribimos el contenido del archivo GeoJSON en el archivo
    f.write(geojson_str)
