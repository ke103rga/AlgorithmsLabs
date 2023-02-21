import pandas as pd
import os
import random


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, capacity=100):
        self.amount_of_comparisons = 0
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        if isinstance(key, str):
            sum = 0
            for ch in key:
               sum += ord(ch)
            return int(0.618033 * len(key) * sum) % self.capacity
        elif isinstance(key, int):
            return key % self.capacity
        else:
            raise ValueError("You can use only int or str types like a key.")

    def __setitem__(self, key, value):
        self.size += 1
        index = self.hash(key)
        new_pair = Pair(key, value)
        #bucket = self.buckets[index]
        if self.buckets[index] is None:
            self.buckets[index] = [new_pair]
        else:
            for pair in self.buckets[index]:
                self.amount_of_comparisons += 1
                if pair.key == key:
                    pair.value = value
                    return
            self.buckets[index].append(new_pair)

    def __getitem__(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if bucket is None:
            raise KeyError(f"The key {key} doesn't exist")
        for pair in bucket:
            if pair.key == key:
                return pair.value
        raise KeyError(f"The key {key} doesn't exist")

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if bucket is None:
            print("none")
            raise KeyError(f"The key {key} doesn't exist")
        for ind, pair in enumerate(bucket):
            if pair.key == key:
                del bucket[ind]
                return
        raise KeyError(f"The key '{key}' doesn't exist")

    def __str__(self):
        result = ""
        for bucket in self.buckets:
            if bucket is not None:
                for pair in bucket:
                    result += f"({pair.key}: {pair.value})"
        return result


def test_hash_table():
    ht = HashTable()
    ht["a"] = 1
    ht["b"] = 2
    ht["c"] = 2
    ht["d"] = 21
    ht[1] = 2
    ht[59] = 23
    print(ht)
    print(ht["a"])

    del ht["a"]
    print(ht)


def task1():
    hash_table = HashTable()
    s = "abcd aaa df cd"
    for ch in s:
        if ch.isalpha():
            hash_table[ch] = hash_table.get(ch, 0) + 1
    print("The counts of every letter in string:")
    print(hash_table)

    print("The amount of paticular letter 'a':")
    print(hash_table["a"])


def compare_amount_of_comparisons(words):
    capacity_range = [20, 50, 100, 500, 1000, 10000]
    results = []

    for capacity in capacity_range:
        hash_table = HashTable(capacity=capacity)
        for word in words:
            hash_table[word] = hash_table.get(word, 0) + 1
        results.append({"capacity": capacity, "amount_of_comparisons": hash_table.amount_of_comparisons})

    results = pd.DataFrame(results)
    print(results)


def task2():
    hash_table = HashTable(capacity=100)
    words = []

    with open("C:\\Users\\User1\\PythonProg\\PycharmProjects\\AlgorithmsLabs\\Lab4\\text", "r") as text_file:
        for line in text_file:
            words.extend(line.split())
        for word in words:
            hash_table[word] = hash_table.get(word, 0) + 1
    print("The counts of every word in text:")
    print(hash_table)

    print("The amount of particular word 'had':")
    print(hash_table["had"])

    print("Amounts of comparisons in tables with different capacity:")
    compare_amount_of_comparisons(words)

    for word in words:
        if word.startswith("t"):
            del hash_table[word]
    print("Hash table after deleting all the words which starts with 't':")
    print(hash_table)


def generate_numbers_file(n_numbers):
    cur_dir = os.getcwd()
    result_filename = f"{cur_dir}\\numbers_{n_numbers}"
    numbers = [random.randint(0, 100) for _ in range(0, n_numbers)]
    with open(result_filename, "w") as result_file:
        for number in numbers:
            print(number, file=result_file)
    return result_filename


def task3():
    hash_table = HashTable(capacity=100)
    num_file = generate_numbers_file(20)
    with open(num_file, "r") as num_file:
        for line in num_file:
            number = int(line)
            hash_table[number] = hash_table.get(number, 0) + 1
    print("Hash table after inserting all numbers:")
    print(hash_table)

    n_numbers_range = [50, 100, 500, 1000, 10000]
    results = []

    for n_numbers in n_numbers_range:
        num_file = generate_numbers_file(n_numbers)
        with open(num_file, "r") as num_file:
            for line in num_file:
                number = int(line)
                hash_table[number] = hash_table.get(number, 0) + 1
        results.append({"n_numbers": n_numbers, "amount_of_comparisons": hash_table.amount_of_comparisons})

    print("Amounts of comparisons in tables which were filled by different numbers of digits:")
    print(pd.DataFrame(results))


task3()



