from random import randint
from bubblesort import bubblesort
from quicksort import quicksort
from radix_LSD import radix
from counting_sort import counting
from timer import timer
from pigeonhole_sort import pigeonhole
from bubblesort import bubblesort


def __main__():
    a = [randint(0, 1000) for i in range(40)]

    algos = [quicksort, radix, counting, bubblesort]

    if input('Print lists? (y/n)') == 'y':
        print(f'Input list:\n{a}')
        for i in algos:
            print(timer(i)(a))
        print(timer(a.sort)())
    else:
        for i in algos:
            timer(i)(a)
        timer(a.sort)()

if __name__ == "__main__":
    __main__()

