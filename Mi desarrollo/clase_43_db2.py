from enum import Enum
from collections import Counter
from collections import defaultdict
import requests
import json

# Traer las apis

scifi_api = "https://api.sampleapis.com/movies/scifi-fantasy"
mystery_api = "https://api.sampleapis.com/movies/mystery"

# Traer el URL para poder convertirlo en una lista con diccionarios

scifi_response = requests.get(scifi_api)
mystery_response = requests.get(mystery_api)

scifi_movies: list[dict] = scifi_response.json()
mystery_movies: list[dict] = mystery_response.json()

# imprimir el resultado para ver las listas con las que estamos tratando

print("Sci-fi movies info:")
print(f"The size of the sci-fi movies API is {len(scifi_movies)}")
print(f"These are the initial rows in the sci-fi movies API: {scifi_movies}")

print("")
print("Mystery movies info:")
print(f"The size of the mystery movies API is {len(mystery_movies)}")
print(f"These are the initial rows in the sci-fi movies API: {mystery_movies}")

# Enum movies


class Movies:
    GREAT = "Must watch and never gets boring"
    GOOD = "You have to see it!"
    ACCEPTABLE = "You can see it"
    REGULAR = "If you have other options choose those"
    BAD = "I would not watch it"
    TERRIBLE = "Avoid it!"
