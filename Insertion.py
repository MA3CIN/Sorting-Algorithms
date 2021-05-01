def insertionSort(Array):
    for i in range(1,len(Array)):
        key = Array[i]
        j = i-1
        while j>=0 and key < Array[j]:
            Array[j+1] = Array[j]
            j -= 1
        Array[j+1] = key

ExampleArray = [12,11,10,13,5,6]
if __name__ == '__main__':
    insertionSort(ExampleArray)
    for i in range(len(ExampleArray)):
        print("% d" % ExampleArray[i])