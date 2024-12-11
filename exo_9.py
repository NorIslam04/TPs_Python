from dataclasses import dataclass
import os
@dataclass
class City:
    name: str
    population: int

citys = []
while True:
    city_name = str(input("city: "))
    if city_name == "stop":
        break
    city = City(name=city_name, population=len(city_name) * 1000000)
    citys.append(city)

citys.sort(key=lambda city: city.population, reverse=True)
os.system("cls")
for city in citys:
    print(f"City: {city.name}, Population: {city.population}")
    