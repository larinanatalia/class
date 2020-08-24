class Animal:
    satiety = 'hungry'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        self.satiety = 'animal ate food'

class Bird(Animal):
    eggs =  'dont have eggs'

    def pick_eggs(self):
        self.eggs = 'we picked eggs'


class Goose(Bird):
    voice = 'krya-krya'



class Chicken(Bird):
    voice = 'kudakh-kudakh'

class Duck(Bird):
    voice = 'krya-krya'

class Cow(Animal):
    voice = 'muuuu'
    milk = 'we need milk'

    def get_milk(self):
        self.milk = 'milk received'

class Sheep(Animal):
    voice = 'beeee'
    wool = 'we dont have'

    def cut(self):
        self.wool = 'we cut the sheep'

class Goat(Animal):
    voice = 'meeee'
    milk = 'we need milk'

    def get_milk(self):
        self.milk = 'milk received'

goose_1 = Goose('Gray', 3)
goose_2 = Goose('White', 3.5)
cow = Cow('Manka', 500)
sheep_1 = Sheep('Barashek', 50)
sheep_2 = Sheep('Kudryavyy', 65)
chicken_1 = Chicken('KoKo', 1)
chicken_2 = Chicken('Kukareku', 0.8)
goat_1 = Goat('Roga', 41)
goat_2 = Goat('Kopyta', 45)
duck = Duck('Kryakva', 2)
print(3+3.5+500+50+65+1+0.8+41+45+2)
all_animal = [goose_1, goose_2, cow, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck]

def print_animal_data(animal_list: list) -> None:
    list_animal_weight = list()
    sum_animal_weight = 0
    list_animal_name = []
    for animal in animal_list:
        list_animal_weight.append(animal.weight)
    for weight in list_animal_weight:
        sum_animal_weight += weight
    print(sum_animal_weight)
    for animal in animal_list:
        list_animal_name.append(animal.name)
    all_animal_dict = dict(zip(list_animal_name, list_animal_weight))
    for key, value in all_animal_dict.items():
        if value == max(all_animal_dict.values()):
            print(key)


print_animal_data(all_animal)
