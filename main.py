from random import randint as r
from quicksort import quicksort
from radix_LSD import radix
from counting_sort import counting
from timer import timer
from pigeonhole_sort import pigeonhole




def __main__():
    a = [r(0, 1000) for i in range(25)]
    print(f'Input list:\n{a}')
    algos = [quicksort, radix, counting, pigeonhole]
    for i in algos:
        print(timer(i)(a))

if __name__ == "__main__":
    __main__()

