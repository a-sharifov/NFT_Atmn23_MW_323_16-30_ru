class Animal:
    def __init__(self, kind, weight):
        self.kind = kind
        self.weight = weight


class Zoo:
    def __init__(self, animals):
        self.animals = animals

    def get_all_kinds(self):
        kinds = ""
        for animal in self.animals:
            kinds += f" {animal.kind}"
        return kinds

    def add(self, animal):
        self.animals.remove(2)



dog = Animal(
    "dog",
    22,
)
cat = Animal(
    "cat",
    44,
)

zoo = Zoo([dog, cat])
print(zoo.get_all_kinds())
