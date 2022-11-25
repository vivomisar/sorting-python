def bubblesort(mas):
    for i in range(len(mas)):
        for j in range(len(mas)):
            if mas[j] > mas[i]:
                mas[i], mas[j] = mas[j], mas[i]
    return mas