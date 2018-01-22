# Insertion Sort
# Complexity O(n) for best cases
#            O(n^2) for average and worst cases

def insertionSort(inputList):

    #loop for every value in list
    for index in range(1, len(inputList)):

        #indexValue is value to be moved
        indexValue = inputList[index]

        print("value to be moved:")
        print(indexValue)

        testIndex = index - 1

        #find a spot in sorted part of list for indexValue (left hand side of list)
        while testIndex > -1 and inputList[testIndex] > indexValue:
            inputList[testIndex + 1] = inputList[testIndex]
            testIndex -= 1
        inputList[testIndex + 1] = indexValue

        print("partially sorted list: ")
        print(inputList)
    return inputList


A = [1,5,8,3,0,9,2,7,4,6]

print("unsorted list: ")
print(A)

B = insertionSort(A)

print("sorted list: ")
print(B)