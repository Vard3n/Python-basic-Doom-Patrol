# 1
class Vehicle:
    car_type = 'usual car'

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage



# 2
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed,mileage)
        self.capacity = capacity

    def seating_capacity(self):
        print(f'Bus contains {self.capacity} seats')


School_bus = Bus(220, 15, 60)
# 3
print(type(School_bus))

# 4
print(isinstance(School_bus, Vehicle))


# 5
class School:

    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6
class SchoolBus(School, Bus):

    def bus_school_color(self):
        print("This Bus is yellow")


#7
class Bear:
    animal_type = "Brown Bear"

    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f"A Bear makes a sound {self.sound}")

class Wolf:
    animal_type2 = "Grey Wolf"

    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f"A Wolf makes a sound {self.sound}")

Big_Bear = Bear('Rrrrraarrrrgh')
Wild_Wolf = Wolf('Auuuuuu')

all_wild_animals = (Big_Bear, Wild_Wolf)

for animal_sound in all_wild_animals:
    animal_sound.make_sound()

#8
class City:
    city_type = 'regular city'

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __call__(self):
        if self.population < 1500:
            print(f"Your city {self.name} is too small")
        else:
            print("Big City Life")

Some_city = City('Pythonvile', 550)
My_city = City('Lviv', 1000000)

all_cities= (Some_city, My_city)

for population_check in all_cities:
    population_check()

