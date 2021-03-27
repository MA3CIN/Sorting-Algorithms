def Bubble_Sort(Array):
    for Iteracja in range(len(Array)):
        for Element in range (0, len(Array)-Iteracja-1): #Ostatni el zawsze posortowany w danej iteracji
            if Array[Element] > Array[Element+1] :
                Array[Element], Array[Element+1] = Array[Element+1], Array[Element]
                # Swap wartosci bez uzycia pamieci