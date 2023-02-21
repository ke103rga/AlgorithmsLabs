import datetime


class Node:
    def __init__(self, data, next_=None):
        self.data_ = data
        self.next_ = next_


class TestPerson:
    def __init__(self, surname, salary):
        self.surname = surname
        self.salary = salary

    def __str__(self):
        return f"(Surname: {self.surname}, Salary: {self.salary})"


class Person:
    def __init__(self,  department_number, surname, date_of_admission, salary=None, service_number=None,
                 percentage_of_allowances=None, percentage_of_tax_fees=None, number_of_days_worked=None,
                 number_of_working_days=None, accrued=None, withheld=None):
        self.service_number = service_number
        self.department_number = department_number
        self.surname = surname
        self.salary = salary
        self.date_of_admission = date_of_admission
        self.percentage_of_allowances = percentage_of_allowances
        self.percentage_of_tax_fees = percentage_of_tax_fees
        self.number_of_days_worked = number_of_days_worked
        self.number_of_working_days = number_of_working_days
        self.accrued = accrued
        self.withheld = withheld

    def __str__(self):
        return f"(Surname: {self.surname}, " \
               f"Department number: {self.department_number}, " \
               f"Date of admission: {self.date_of_admission})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_element(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_ = new_node
            self.tail = new_node

    def extend(self, iterable):
        for element in iterable:
            self.append_element(element)

    def search(self, **properties):
        cur_node = self.head
        while cur_node:
            if self.is_equal(cur_node.data_, **properties):
                return cur_node.data_
            cur_node = cur_node.next_

    def is_equal(self, node_data, **properties):
        for property_name, property_value in properties.items():
            if getattr(node_data, property_name) != property_value:
                return False
        return True

    def insert_element(self, element, *properties, asc=True):
        if self.head is None:
            self.append_element(element)
        else:
            new_node = Node(element)
            if self.compare(self.head.data_, new_node.data_, *properties, asc=asc) < 0:
                new_node.next_ = self.head
                self.head = new_node
                return
            prev_node = self.head
            cur_node = self.head.next_
            while cur_node:
                if self.compare(cur_node.data_, new_node.data_, *properties, asc=asc) < 0:
                    prev_node.next_ = new_node
                    new_node.next_ = cur_node
                    return
                else:
                    prev_node = cur_node
                    cur_node = cur_node.next_
            self.append_element(element)

    def compare(self, elem1, elem2, *properties, asc=True):
        asc = 1 if asc is True else -1
        for property_name in properties:
            elem1_property = getattr(elem1, property_name)
            elem2_property = getattr(elem2, property_name)
            if elem1_property > elem2_property:
                return -1 * asc
            elif elem1_property < elem2_property:
                return 1 * asc
        return 0

    def sort(self, *properties, asc=True):
        cur_node = self.head
        new_list = LinkedList()
        while cur_node:
            new_list.insert_element(cur_node.data_, *properties, asc=asc)
            cur_node = cur_node.next_
        return new_list

    def __str__(self):
        cur_node = self.head
        result = f""
        while cur_node:
            result += f"{cur_node.data_.__str__()}\n"
            cur_node = cur_node.next_
        return result


def test():
    person1 = TestPerson("a", 1000)
    person2 = TestPerson("b", 2000)
    person3 = TestPerson("c", 3000)
    person4 = TestPerson("d", 4000)
    person5 = TestPerson("e", 5000)
    persons = [person2, person3, person4, person1, person5]

    lst = LinkedList()
    lst.extend(persons)
    lst.append_element(person1)
    print("List after extending:")
    print(lst)

    print("Result of searching:")
    print(lst.search(surname="e", salary=5000), end="\n\n")

    # new_person = TestPerson("b", 30000)
    # lst.insert_element(new_person, "surname", "salary", asc=True)
    # print("Result of inserting:")
    # print(lst)

    sorted_list = lst.sort("surname", asc=True)
    print("Result of sorting:")
    print(sorted_list)


def show():
    person1 = Person(surname="Parker", department_number=101, date_of_admission=datetime.datetime.strptime('24052010', "%d%m%Y").date())
    person2 = Person(surname="Medisson", department_number=201, date_of_admission=datetime.datetime.strptime('24062010', "%d%m%Y").date())
    person3 = Person(surname="Abrams", department_number=101, date_of_admission=datetime.datetime.strptime('25052010', "%d%m%Y").date())
    person4 = Person(surname="Arab", department_number=301, date_of_admission=datetime.datetime.strptime('23112011', "%d%m%Y").date())
    person5 = Person(surname="Counter", department_number=101, date_of_admission=datetime.datetime.strptime('25082011', "%d%m%Y").date())
    persons = [person1, person2, person3, person4, person5]

    lst = LinkedList()
    lst.extend(persons)
    print("List after extending:")
    print(lst)

    print("Result of searching:")
    print(lst.search(surname="Abrams", department_number=101, date_of_admission=datetime.datetime.strptime('25052010', "%d%m%Y").date()), end="\n\n")

    sorted_list = lst.sort("department_number", "surname", asc=True)
    print("Result of sorting:")
    print(sorted_list)


show()
