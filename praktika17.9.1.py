def Bubble(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


def BinarySearch(array, element):
    if element < array[0] or element > array[-1]:
        return False
    first = 0
    last = len(array)
    while first < last - 1:
        mid = (first + last) // 2
        if element > array[mid]:
            first = mid
        else:
            last = mid
    return first


array = [int(x) for x in input("Введите числа в любом порядке, через пробел: ").split()]
element = int(input("Введите любое целое число: "))
Bubble(array)
print(array)
print(BinarySearch(array, element))
