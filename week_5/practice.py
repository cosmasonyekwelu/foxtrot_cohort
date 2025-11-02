# https://www.youtube.com/watch?v=rLyYb7BFgQI
# Initializers
# Dunder Methods
class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned on')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave ({self.brand}) is now turned off')
        else:
            print(f'Microwave ({self.brand}) is already turned off')

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f'Running ({self.brand} for {seconds}) seconds')
        else:
            print('Turn on your microwave first...')

    def __add__(self, others):
        return f'{self.brand} + {others.brand}'

    def __str__(self) -> str:
        return f'{self.brand} (Rating: {self.power_rating})'

    def __repr__(self):
        return f'Microwave(brand="{self.brand}", power_rating="{self.power_rating}")'

    def __eq__(self, other):
        return self.brand == other.brand and self.power_rating == other.power_rating


smeg: Microwave = Microwave(brand='Smeg', power_rating='B')

# smeg.turn_on()
# smeg.turn_on()
# smeg.run(30)
# smeg.turn_off()
# smeg.run(10)

# print(smeg)
# print(smeg.brand)
# print(smeg.power_rating)


bosch: Microwave = Microwave(brand='Bosch', power_rating='C')
# print(bosch.brand)
# print(bosch.power_rating)
# bosch.turn_on()
# bosch.turn_off()
# bosch.run(2)

samsung: Microwave = Microwave(brand='Samsung', power_rating='C')
# print(smeg + bosch)
# print(smeg)
# print(bosch)
# print(repr(smeg))

samsung.turn_on()
samsung.run(5)
samsung.turn_off()
