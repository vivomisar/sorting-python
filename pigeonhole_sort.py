def pigeonhole(mas):
    d = {}
    for i in mas:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d