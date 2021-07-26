import numpy as np

class first_n(object):

    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur

        raise StopIteration()


sum_of_first_n = sum(first_n(5))
print(sum_of_first_n)



##########################################

# a generator that yields items instead of returning a list


def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_of_fN = sum(firstn(5))
print(sum_of_fN)


######################

print(sum((n for n in range(100000000000))))

