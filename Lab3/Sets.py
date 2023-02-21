import random


class MySet:
    def __init__(self, iterable=None):
        if iterable is None:
            self.data = []
        else:
            self.data = self.drop_dublicates(iterable)

    def drop_dublicates(self, iterable):
        used_elements = []
        unique = []
        for index, elem in enumerate(iterable):
            if elem not in used_elements:
                unique.append(elem)
                used_elements.append(elem)
        return unique

    def add(self, element):
        if element not in self.data:
            self.data.append(element)

    def intersection(self, other_set):
        result = MySet()
        for elem in self.data:
            if elem in other_set.data:
                result.add(elem)
        return result

    def difference(self, other_set):
        result = MySet()
        for elem in self.data:
            if elem not in other_set.data:
                result.add(elem)
        return result

    def union(self, other_set):
        result = self.copy()
        for elem in other_set.data:
            result.add(elem)
        return result

    def copy(self):
        return MySet(self.data.copy())

    def __str__(self):
        return self.data.__str__()


def random_guests_filling(members):
    min_amount_of_guests = int(0.6 * len(members))
    max_amount_of_guests = len(members)
    guests = {}
    for member in members:
        amount_of_guests = random.randint(min_amount_of_guests, max_amount_of_guests)
        guests[member] = set(filter(lambda guest: guest != member, random.sample(members, amount_of_guests)))
    return guests


def test_set():
    s = MySet([1, 1, 2, 3, 2, 3, 3, 4])
    s1 = MySet([3, 4, 5, 5, 6, 7, 8, 8, 9, 5, 7])
    print(f"The first set: {s}")
    print(f"The second set: {s1}")

    print(f"The intersection of sets: {s.intersection(s1)}")
    print(f"The difference of sets: {s.difference(s1)}")
    print(f"The union of sets: {s.union(s1)}")


def common_guests_searching(random=False):
    members = ["Masha", "Tanya", "Lena", "Dasha", "Artem", "Misha", "Gosha", "Danil"]
    if random:
        test_guests = random_guests_filling(members)
    else:
        test_guests = {"Masha": ["Tanya", "Artem", "Tanya", "Artem", "Dima"],
                       "Tanya": ["Dima", "Artem"],
                       "Artem": ["Tanya", "Masha", "Artem", "Dima"],
                       "Dima": ["Artem", "Masha", "Dima"]}

    print("The list of guests for every owner:")
    for owner, guests in test_guests.items():
        print(f"{owner}: {guests}")

    guests_sets = [MySet(guests) for guests in test_guests.values()]
    common_guests = guests_sets[0]
    for guests_set in guests_sets[1:]:
        common_guests = common_guests.intersection(guests_set)

    print(f"Common guests are: {common_guests}")


common_guests_searching(random=False)