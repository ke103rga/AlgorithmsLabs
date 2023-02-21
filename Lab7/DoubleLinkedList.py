class Patient:
    def __init__(self, name, age, sex=None, diagnosis=None):
        self.name = name
        self.age = age
        self.sex = sex
        self.diagnosis = diagnosis
        self.next_ = None
        self.prev_ = None

    def copy(self):
        return Patient(self.name, self.age, self.sex, self.diagnosis)

    def __str__(self):
        return f"(Name: {self.name}, Age: {self.age}, Sex: {self.sex})"


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_element(self, patient):
        new_patient = patient.copy()
        if self.head is None:
            self.head = new_patient
            self.tail = new_patient
        else:
            self.tail.next_ = new_patient
            new_patient.prev_ = self.tail
            new_patient.next_ = None
            self.tail = new_patient

    def extend(self, patients):
        for patient in patients:
            self.append_element(patient)

    def select(self, **properties):
        selected = DoubleLinkedList()
        cur_patient = self.head
        while cur_patient:
            for property_name, property_value in properties.items():
                if getattr(cur_patient, property_name) == property_value:
                    selected.append_element(cur_patient)
            cur_patient = cur_patient.next_
        print()
        return selected

    def compare(self, patient1, patient2, *properties, asc=True):
        asc = 1 if asc is True else -1
        for property_name in properties:
            elem1_property = getattr(patient1, property_name)
            elem2_property = getattr(patient2, property_name)
            if elem1_property > elem2_property:
                return -1 * asc
            elif elem1_property < elem2_property:
                return 1 * asc
        return 0

    def insert_element(self, patient, *properties, asc=True):
        if self.head is None:
            self.append_element(patient)
        else:
            new_patient = patient.copy()
            if self.compare(self.head, new_patient, *properties, asc=asc) < 0:
                new_patient.next_ = self.head
                self.head.prev_ = new_patient
                self.head = new_patient
                return
            cur_node = self.head.next_
            while cur_node:
                if self.compare(cur_node, new_patient, *properties, asc=asc) < 0:
                    cur_node.prev_.next_ = new_patient
                    cur_node.prev_.next_.prev_ = cur_node.prev_
                    cur_node.prev_.next_.next_ = cur_node
                    cur_node.prev_ = cur_node.prev_.next_
                    return
                else:
                    cur_node = cur_node.next_
            self.append_element(new_patient)

    def sort(self, *properties, asc=True):
        sorted = DoubleLinkedList()
        if self.head is None or self.head.next_ is None:
            return self
        cur_patient = self.head
        while cur_patient:
            sorted.insert_element(cur_patient, *properties, asc=asc)
            cur_patient = cur_patient.next_
        return sorted

    def __str__(self):
        for_print = ""
        cur_patient = self.head
        while cur_patient:
            for_print += f"{cur_patient.__str__()}\n"
            cur_patient = cur_patient.next_
        return for_print


def test():
    print("Let's create a list with the same amount of males and females with different ages")
    patient1 = Patient("Sasha", 18, "female")
    patient2 = Patient("Misha", 7, "male")
    patient3 = Patient("Danil", 19, "male")
    patient4 = Patient("Sveta", 38, "female")
    patient5 = Patient("Pavel", 43, "male")
    patient6 = Patient("Dasha", 2, "female")
    patients = [patient1, patient2, patient3, patient4, patient5, patient6]

    lst = DoubleLinkedList()
    lst.extend(patients)
    print("The list that we've just created:")
    print(lst, end="\n\n")

    print("Now we can separate it into two categories: males and females")
    males = lst.select(sex="male")
    females = lst.select(sex="female")
    print("Selected men:")
    print(males, end="\n\n")
    print("Selected women:")
    print(females, end="\n\n")

    print("And our last step is to sort the both of separated lists by age.")
    sorted_males = males.sort("age")
    sorted_females = females.sort("age")
    print("Sorted men:")
    print(sorted_males, end="\n\n")
    print("Sorted women:")
    print(sorted_females, end="\n\n")


test()

