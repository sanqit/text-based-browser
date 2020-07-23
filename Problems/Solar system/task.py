planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
with open("planets.txt", "w", encoding="utf-8") as planets_file:
    planets_file.writelines([planet + "\n" for planet in planets])
