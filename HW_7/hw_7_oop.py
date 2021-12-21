from abc import ABC, abstractmethod

stages = {0: 'None', 1: 'Flowering', 2: 'Green', 3: 'Red'}


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits, pests):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests

    def show_the_garden(self):
        print(f"I have {self.vegetables} and {self.fruits} and {self.pests}")


class Vegetables(ABC):

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def is_ripe(self):
        pass


class Fruits(ABC):

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def is_ripe(self):
        pass


class Tomato(Vegetables):
    def __init__(self, tomatoes_index, vegetable_type):
        self.tomatoes_index = tomatoes_index
        self.vegetable_type = vegetable_type
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.grow_info()

    def is_ripe(self):
        if self.state == 3:
            return

    def grow_info(self):
        print(f'{self.vegetable_type} - {self.tomatoes_index}: {stages[self.state]}')

    def check_state(self):
        return self.state


class TomatoBush:
    def __init__(self, number_of_tomatoes, number_of_pests):
        self.number_of_tomatoes = [Tomato('Cherry', index) for index in range(number_of_tomatoes)]
        self.number_of_pests = [Pests('Bugs', index, self.number_of_tomatoes) for index in range(number_of_pests)]

    def grow_all(self):
        for tomato in self.number_of_tomatoes:
            tomato.grow()

    def is_ripe_all(self):
        return all([tomato.is_ripe() for tomato in self.number_of_tomatoes])

    def harvest(self):
        self.number_of_tomatoes = []

    def is_ripe_pest(self):
        return any([tomato.check_state() > 1 for tomato in self.number_of_tomatoes])

    def plant_destroyer(self):
        self.number_of_tomatoes = []


class Apple(Fruits):
    def __init__(self, apple_index, fruit_type):
        self.apple_index = apple_index
        self.fruit_type = fruit_type
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.grow_info()

    def is_ripe(self):
        if self.state == 3:
            return

    def grow_info(self):
        print(f'{self.fruit_type} - {self.apple_index}: {stages[self.state]}')

    def check_state(self):
        return self.state


class AppleTree:
    def __init__(self, number_of_apples, number_of_pests):
        self.number_of_apples = [Apple('White', index) for index in range(number_of_apples)]
        self.number_of_pests = [Pests('Worms', index, self.number_of_apples) for index in range(number_of_pests)]

    def grow_all(self):
        for apple in self.number_of_apples:
            apple.grow()

    def is_ripe_all(self):
        return all([apple.is_ripe() for apple in self.number_of_apples])

    def harvest(self):
        self.number_of_apples = []

    def is_ripe_pest(self):
        return any([apple.check_state() > 1 for apple in self.number_of_apples])

    def plant_destroyer(self):
        self.number_of_apples = []


class Gardener:
    insects = {'Bugs': False, 'Worms': False}

    def __init__(self, name, plants_list, pests_list):
        self.name = name
        self.plants_list = plants_list
        self.pests_list = pests_list

    def number_of_it(self):
        self.plants_list = []

    def take_care(self):
        print("watering the plants")
        for plant in self.plants_list:
            plant.grow_all()

    def harvest(self):
        harvesting_plants = []

        harvesting_plants += (plant for plant in self.plants_list if isinstance(plant, AppleTree)
                              and self.insects['Worms'])
        harvesting_plants += (plant for plant in self.plants_list if isinstance(plant, TomatoBush)
                              and self.insects['Bugs'])

        will_be_eaten = [plant for plant in self.plants_list if plant not in harvesting_plants]

        for plant in will_be_eaten:
            plant.plant_destroyer()

        for plant in self.plants_list:
            if plant.is_ripe_all:
                print('Harvesting...')
                plant.harvest()
            else:
                print("It's not ready for harvest")

    def insects_disinfection(self, pests_type):
        for x in range(len(self.pests_list)):
            for y in range(len(self.pests_list[x])):
                if self.pests_list[x][y].pest_type == pests_type:
                    self.pests_list[x][y].the_kill()
                    self.pests_list[x][y] = False
                    self.insects[pests_type] = True

        for x in self.insects.keys():
            if self.insects[x]:
                print(f'{x} are killed.')


class Pests:
    def __init__(self, pest_type, pests_quantity, plants_list):
        self.pest_type = pest_type
        self.pests_quantity = pests_quantity
        self.plants_list = plants_list

    def eat_plants(self):
        for plant in self.plants_list:
            if plant.is_ripe_pest():
                plant.harvest()
                print('Tasty plant')
            else:
                print('Nothing to eat')

    def the_kill(self):
        del self

    def __del__(self):
        pass


apple_tree = AppleTree(3, 2)
tomato_bush = TomatoBush(2, 1)
print(tomato_bush.number_of_tomatoes)
print(apple_tree.number_of_apples)

gardener = Gardener("Homer", [apple_tree, tomato_bush], [apple_tree.number_of_pests, tomato_bush.number_of_pests])

pest = Pests('Worms', 2, [apple_tree])

gardener.take_care()
pest.eat_plants()
gardener.take_care()
pest.eat_plants()
gardener.insects_disinfection('Worms')
gardener.take_care()
gardener.harvest()