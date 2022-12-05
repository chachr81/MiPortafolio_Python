import geojson
import random

# Crea una lista de coordenadas aleatorias en Chile
coordinates = []
for i in range(10):
    lon = random.uniform(-75, -69)
    lat = random.uniform(-55, -17)
    coordinates.append((lon, lat))

# Crea un objeto GeoJSON de tipo MultiPoint con las coordenadas aleatorias
multipoint = geojson.MultiPoint(coordinates)

# Crea un objeto Feature con el MultiPoint y algunos atributos
properties = {"name": "Aleatorio", "description": "10 puntos aleatorios en Chile"}
feature = geojson.Feature(geometry=multipoint, properties=properties)

# Crea un objeto FeatureCollection con el Feature
feature_collection = geojson.FeatureCollection([feature])