from random import randint as r
import functools
import time


def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.10f} secs")
        return result

    return _wrapper


def prep(a):
    a = str(a)
    return '0' * (6 - len(a)) + a if a[0] != '-' else '-' + '0' * (6 - len(a)) + a.replace('-', '')


@timer
def radix(mas):
    l = len(mas[0])
    for i in range(l-1, 0, -1):
        digits = [[] for k in range(10)]
        for j in mas:
            match j[i]:
                case '0':
                    digits[0].append(j)
                case '1':
                    digits[1].append(j)
                case '2':
                    digits[2].append(j)
                case '3':
                    digits[3].append(j)
                case '4':
                    digits[4].append(j)
                case '5':
                    digits[5].append(j)
                case '6':
                    digits[6].append(j)
                case '7':
                    digits[7].append(j)
                case '8':
                    digits[8].append(j)
                case '9':
                    digits[9].append(j)
        mas = []
        for digit in digits:
            mas += digit
    return list(map(lambda x: int(x), mas))


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


timed_quicksort = timer(quicksort)
a = [r(0, 1000) for i in range(1000)]
mas = list(map(prep, a))
#print(a)
radix(mas)
timed_quicksort(a)
