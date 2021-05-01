def Bubble_Sort(Array):
    for Iteracja in range(len(Array)):
        for Element in range (0, len(Array)-Iteracja-1): #Ostatni el zawsze posortowany w danej iteracji
            if Array[Element] > Array[Element+1] :
                Array[Element], Array[Element+1] = Array[Element+1], Array[Element]
                # Swap wartosci bez uzycia pamieci

ExampleArray = [12,11,10,13,5,6]
if __name__ == '__main__':
    Bubble_Sort(ExampleArray)
    for i in range(len(ExampleArray)):
        print("% d" % ExampleArray[i])