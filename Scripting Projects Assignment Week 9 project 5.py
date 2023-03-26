def isSorted(lst):
    if len(lst) <= 1:
        return True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False

    return True
print(isSorted([1,2,3,4,5]))
print(isSorted([1,2,3,5,4]))
