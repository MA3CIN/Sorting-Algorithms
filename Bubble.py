<<<<<<< HEAD
def Bubble_Sort(Array):
    for Iteracja in range(len(Array)):
        for Element in range (0, len(Array)-Iteracja-1): #Ostatni el zawsze posortowany w danej iteracji
            if Array[Element] > Array[Element+1] :
                Array[Element], Array[Element+1] = Array[Element+1], Array[Element]
=======
def Bubble_Sort(Array):
    for Iteracja in range(len(Array)):
        for Element in range (0, len(Array)-Iteracja-1): #Ostatni el zawsze posortowany w danej iteracji
            if Array[Element] > Array[Element+1] :
                Array[Element], Array[Element+1] = Array[Element+1], Array[Element]
>>>>>>> 52d5b35f3523f7f0ba51c4cee78c9a17da9217c8
                # Swap wartosci bez uzycia pamieci