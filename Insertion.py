<<<<<<< HEAD
def insertionSort(Array):
    for i in range(1,len(Array)):
        key = Array[i]
        j = i-1
        while j>=0 and key < Array[j]:
            Array[j+1] = Array[j]
            j -= 1
        Array[j+1] = key

ExampleArray = [12,11,10,13,5,6]
insertionSort(ExampleArray)
for i in range(len(ExampleArray)):
=======
def insertionSort(Array):
    for i in range(1,len(Array)):
        key = Array[i]
        j = i-1
        while j>=0 and key < Array[j]:
            Array[j+1] = Array[j]
            j -= 1
        Array[j+1] = key

ExampleArray = [12,11,10,13,5,6]
insertionSort(ExampleArray)
for i in range(len(ExampleArray)):
>>>>>>> 52d5b35f3523f7f0ba51c4cee78c9a17da9217c8
    print ("% d" % ExampleArray[i])