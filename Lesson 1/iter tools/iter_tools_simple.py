# Simple implementation

def evens():
    """" Generate even integers, starting with 0. """

    n = 0
    while True:
        yield n
        n += 2

evens = evens()
print(list(next(evens) for _ in range(1_000)))

# With itertools
import itertools as it

counter = it.count(start=32, step=2)
print(list(next(counter) for _ in range(10)))