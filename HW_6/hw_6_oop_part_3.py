import time
import uuid
import random
from abc import ABC, abstractmethod


class Animal(ABC):
    types = ("Herbivores", "Predator")

    def __init__(self, power, speed):
        self.id = uuid.uuid4()
        self.max_power = power
        self.current_power = power
        self.speed = speed
        self.out_of_power = False

    def eat(self, power):
        self.current_power += power
        if self.current_power + power >= self.max_power:
            self.current_power = self.max_power

    def draining_power(self, power):
        self.current_power -= power
        if self.current_power <= 0:
            self.out_of_power = True

    @abstractmethod
    def get_name(self):
        pass

    def animal_info(self):
        return self.get_name() + " " + str(self.id)


class Predator(Animal):

    def get_name(self):
        predator = ["Wolf", "Bear", "Lynx", "Boar"]
        return random.choice(predator)


class Herbivorous(Animal):

    def get_name(self):
        herbivorous = ["Rabbit", "Deer", "Woodpecker", "Squirrel"]
        return random.choice(herbivorous)


class Forest:

    def __init__(self):
        self.animals = dict()

    def add_animal(self, animal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal):
        del self.animals[animal.id]

    def get_animal_count(self):
        return len(self.animals)

    def animal_id(self, hunter_id=None):
        if not isinstance(hunter_id, type(None)):
            key_list = list(key for key in self.animals.keys() if key != hunter_id)

        else:
            key_list = list(self.animals.keys())

        animal_key = random.choice(key_list)
        return self.animals[animal_key]

    def hunting_possibility(self):
        if self.get_animal_count() <= 1:
            return False
        return True

    @staticmethod
    def animal_list():
        for animal in my_forest.animals.keys():
            print(my_forest.animals[animal].animal_info())

    def predator_left(self):
        for key in self.animals.keys():
            if isinstance(self.animals[key], Predator):
                return True

        return False

    def the_hunt(self):
        hunter = Forest.animal_id(self)

        if isinstance(hunter, Herbivorous):
            hunter.eat(50)

        prey = Forest.animal_id(self, hunter.id)

        if hunter.speed > prey.speed and hunter.current_power > prey.current_power:
            hunter.eat(50)
            prey.out_of_power = True
        else:
            hunter.draining_power(30)
            prey.draining_power(30)

        if hunter.out_of_power:
            self.remove_animal(hunter)

        if prey.out_of_power:
            self.remove_animal(prey)


class AnimalGenerator:

    def __iter__(self):
        return self

    def __next__(self):
        animal_type = random.choice(Animal.types)

        if animal_type == "Predator":
            new_animal = Predator(random.randint(25, 100),
                                  random.randint(25, 100))
        else:
            new_animal = Herbivorous(random.randint(25, 100),
                                     random.randint(25, 100))

        return new_animal


if __name__ == "__main__":
    nature = AnimalGenerator()
    my_forest = Forest()

    for i in range(10):
        animal = next(nature)
        my_forest.add_animal(animal)

    print("Animal Population")
    my_forest.animal_list()

    print("Hunting season is opened!")

    time.sleep(3)

    while my_forest.predator_left() and my_forest.hunting_possibility():
        my_forest.the_hunt()

    print("Any survivals?")
    my_forest.animal_list()
