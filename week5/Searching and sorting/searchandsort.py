# binary search
def Ordered_binary_Search(list, number):
    # searches for length of list
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2  # middle point of list
        if list[midpoint] == number:
            return True
        else:
            if number < list[midpoint]:
                return binarySearch(list[:midpoint], number)
            else:
                return binarySearch(list[midpoint+1:], number)


def binarySearch(alist, number):

    first = 0             # first number of list
    last = len(alist) - 1  # last number of list
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == number:
            found = True
        else:
            if number < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))

# src https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-3.php
