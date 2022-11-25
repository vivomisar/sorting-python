def counting(mas):
    mn, mx = min(mas), max(mas)+1
    d = {i: 0 for i in range(mn, mx)}
    output = []
    for i in mas:
        d[i] += 1
    for i in range(mn, mx):
        output += [i] * d[i]
    return output
    