# https://www.youtube.com/watch?v=rLyYb7BFgQI
# Initializers
class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating


smeg: Microwave = Microwave(brand='Smeg', power_rating='B')


print(smeg)
print(smeg.brand)
print(smeg.power_rating)


bosch: Microwave = Microwave(brand='Bosch', power_rating='C')
print(bosch.brand)
print(bosch.power_rating)
