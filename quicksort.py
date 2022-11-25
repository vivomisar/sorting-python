def quicksort(mas):
    if len(mas) <= 1:
        return mas
    pivot = mas[len(mas) // 2]
    less = []
    greater = []
    equal = []
    for i in mas:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)
    return quicksort(less) + equal + quicksort(greater)