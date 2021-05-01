from random import randint
from timeit import repeat
from Insertion import insertionSort
from Bubble import Bubble_Sort


def BeginTheTest(algorithm,array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    smtn = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=smtn, repeat=10, number=10)
    print(f"Sorting Algorithm {algorithm}. Fastest time : {min(times)}")

    # ToDo Rozbicie na pliki, implementacje innych algorytmow, import sortow, gui?


if __name__ == "__main__":
    TestArray = [randint(0, 1000) for i in range(100)]

    # BeginTheTest(algorithm="sorted", array=TestArray)
