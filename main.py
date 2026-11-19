import json


def film_numbers(film_urls):
    """Extract the final numeric ID from every SWAPI film URL."""
    return [url.rstrip("/").split("/")[-1] for url in film_urls]


# ============================================================
# MISSION 1 - FIND THE PLANET
# Person 2 is C-3PO. His homeworld URL leads to planet 1: Tatooine.
# ============================================================

planet_json = """
{
    "name": "Tatooine",
    "rotation_period": "23",
    "orbital_period": "304",
    "diameter": "10465",
    "climate": "arid",
    "gravity": "1 standard",
    "terrain": "desert",
    "surface_water": "1",
    "population": "200000",
    "residents": [
        "https://swapi.dev/api/people/1/",
        "https://swapi.dev/api/people/2/",
        "https://swapi.dev/api/people/4/"
    ],
    "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/4/",
        "https://swapi.dev/api/films/5/",
        "https://swapi.dev/api/films/6/"
    ],
    "url": "https://swapi.dev/api/planets/1/"
}
"""

planet = json.loads(planet_json)

planet_films = film_numbers(planet["films"])

print("MISSION 1")
print(f"Planet name: {planet['name']}")
print(f"Climate: {planet['climate']}")
print(f"Terrain: {planet['terrain']}")
print(f"Appeared in films: {', '.join(planet_films)}")


# ============================================================
# BONUS MISSION - FIND THE STARSHIP
# Person 14 is Han Solo. His first starship is starship 10:
# the Millennium Falcon.
# ============================================================

starship_json = """
{
    "name": "Millennium Falcon",
    "model": "YT-1300 light freighter",
    "manufacturer": "Corellian Engineering Corporation",
    "cost_in_credits": "100000",
    "length": "34.37",
    "max_atmosphering_speed": "1050",
    "crew": "4",
    "passengers": "6",
    "cargo_capacity": "100000",
    "consumables": "2 months",
    "hyperdrive_rating": "0.5",
    "MGLT": "75",
    "starship_class": "Light freighter",
    "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/3/"
    ],
    "url": "https://swapi.dev/api/starships/10/"
}
"""

starship = json.loads(starship_json)
starship_films = film_numbers(starship["films"])

print("\nBONUS MISSION")
print(f"Starship name: {starship['name']}")
print(f"Crew: {starship['crew']}")
print(f"Consumables: {starship['consumables']}")
print(f"Appeared in films: {', '.join(starship_films)}")

