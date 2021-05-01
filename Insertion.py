def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


ExampleArray = [12, 11, 10, 13, 5, 6]
if __name__ == '__main__':
    insertionSort(ExampleArray)
    for i in range(len(ExampleArray)):
        print("% d" % ExampleArray[i])