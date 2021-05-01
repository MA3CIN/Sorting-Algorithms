def bubble_Sort(array):
    for Iteracja in range(len(array)):
        for Element in range (0, len(array)-Iteracja-1):  # Ostatni el zawsze posortowany w danej iteracji
            if array[Element] > array[Element+1] :
                array[Element], array[Element+1] = array[Element+1], array[Element]
                # Swap wartosci bez uzycia pamieci


ExampleArray = [12, 11, 10, 13, 5, 6]
if __name__ == '__main__':
    bubble_Sort(ExampleArray)
    for i in range(len(ExampleArray)):
        print("% d" % ExampleArray[i])