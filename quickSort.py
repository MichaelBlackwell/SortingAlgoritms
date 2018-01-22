# Quick Sort
# Complexity O(nlogn) for best cases
#            O(n^2) for average and worst cases

def quickSort(inputList):

    less = []
    pivotList = []
    more = []

    if len(inputList) <= 1:
        return inputList
    else:
        pivot = inputList[0]
        for i in inputList:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        print("input list: ")
        print(inputList)

        print("less list: ")
        print(less)

        print("pivot list: ")
        print(pivot)

        print("more list: ")
        print(more)



        less = quickSort(less)
        more = quickSort(more)

        r = less + pivotList + more
        print("returned list: ")
        print(r)
        print()

        return r


A = [1,5,8,3,0,9,2,7,4,6]

print("unsorted list: ")
print(A)

B = quickSort(A)

print("sorted list: ")
print(B)

