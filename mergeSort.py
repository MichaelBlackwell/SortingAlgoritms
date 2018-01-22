# MergeSort
# Complexity O(n Log n) for best, worst, and average cases

def merge(left, right):

    print("left: ")
    print(left)
    print("right: ")
    print(right)

    #list to be returned
    mergedList = []

    #Keep track of far left and right indexes
    leftIndex, rightIndex = 0, 0

    #loop until leftIndex and rightIndex are as large as their corresponding lists
    while leftIndex < len(left) and rightIndex < len(right):



        #This determines the direction of the sort
        if left[leftIndex] <= right[rightIndex]:
            mergedList.append(left[leftIndex])
            leftIndex += 1
        else:
            mergedList.append(right[rightIndex])
            rightIndex += 1

    if left:
        mergedList.extend(left[leftIndex:])

    if right:
        mergedList.extend(right[rightIndex:])

    print("merged list: ")
    print(mergedList)

    return mergedList

def mergeSort(inputList):
    #if the inputList is of size 1, stop recursion
    if len(inputList) <= 1:
        return inputList

    #split the inputList into two lists
    middleIndex = len(inputList) // 2
    left = inputList[:middleIndex]
    right = inputList[middleIndex:]

    #recursivly merge lists
    left = mergeSort(left)
    right = mergeSort(right)


    return list(merge(left,right))

A = [1,5,8,3,0,9,2,7,4,6]

print("unsorted list: ")
print(A)

B = mergeSort(A)

print("sorted list: ")
print(B)