import dataclasses
from collections import namedtuple


# 1  Make the class with composition.
class Laptop:
    def __init__(self):
        unit_1 = Battery("The laptop doesn't have the power without this component")
        unit_2 = Screen("The laptop can't show content without this component")
        unit_3 = Keyboard("You can't add information without this component")
        self.units = (unit_1, unit_2, unit_3)


class Battery:
    def __init__(self, power):
        self.power = power


class Screen:
    def __init__(self, monitor):
        self.monitor = monitor


class Keyboard:
    def __init__(self, letters):
        self.letters = letters


the_laptop = Laptop()
print(the_laptop.units[0].power)
print(the_laptop.units[1].monitor)
print(the_laptop.units[2].letters)


# 2 Make the class with aggregation
class Guitar:
    def __init__(self, guitarstring):
        self.guitarstring = guitarstring


class GuitarString:
    def __init__(self):
        pass


the_string = GuitarString()
guitar = Guitar(the_string)


# 3 Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
class Calc:
    @staticmethod
    def add_nums(x, y, z):
        return x + y + z


calc = Calc()
print(calc.add_nums(5, 20, 60))


# 4
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pasta({self.ingredients!r})'

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


carbonara_Pasta = Pasta.carbonara()
bolognaise_Pasta = Pasta.bolognaise()
print(carbonara_Pasta)
print(bolognaise_Pasta)


# 5
class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value <= self.max_visitors_num:
            self._visitors_count = value
        else:
            self._visitors_count = self.max_visitors_num


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)


# 6 Create dataclass

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


my_address_book = AddressBookDataClass(key=22,
                                       name='The Dude',
                                       phone_number='234-92-07',
                                       address='Hollywood Street',
                                       email='the_dude@gmail.com',
                                       birthday='20th of June',
                                       age=28)
print(my_address_book)
print(my_address_book.name)
print(my_address_book.email)

# 7 NamedTuple
AddressBookDataClass2 = namedtuple('AddressBookDataClass2',
                                   ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

my_second_address_book = AddressBookDataClass2(32, 'Mega Dude', '432-29-70', 'New-York Street', 'mega_dude@gmail.com',
                                               '20th of June', 28)
print(my_second_address_book)
print(my_second_address_book.name)
print(my_second_address_book.email)


# 8
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook: {self.key}, {self.name}, {self.phone_number}, {self.address}, {self.email}, ' \
               f'{self.birthday}, {self.age}'


one_more_ab = AddressBook(33, 'The Mega Dude', '324-92-07', 'Grove Street', 'the_mega_dude@gmail.com', '20th of June',
                          28)
print(one_more_ab)


# 9
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.county = country

    @property
    def what_is_the_age(self):
        return f'This person name is {self.name}, and he is {self.age} old'


the_person = Person('John', 36, 'USA')
print(the_person.what_is_the_age)
the_person.age = 40
print(the_person.what_is_the_age)


# 10
class Student:
    id = 8
    name = "Homer"
    email = "a_student_email@gmail.com"

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


homer = Student(8, "Homer", "a_student_email@gmail.com")
print(getattr(homer, 'email'))
print(getattr(homer, 'name'))
setattr(homer, 'student_email', "new_student_email@gmail.com")
print(getattr(homer, 'student_email'))


# 11
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Get value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print('Set value')
        if value < -273:
            raise ValueError('Temperature below -273 is not possible')
        self._temperature = value


converter = Celsius(30)
print(converter.temperature)
print(converter.to_fahrenheit())
converter = Celsius(-300)
print(converter.temperature)
