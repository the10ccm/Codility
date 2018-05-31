import pprint
import operator
import re

from helpers import timer


# 1.1 BinaryGap
# Find longest sequence of zeros in binary representation of an integer.
def binary_gaps(number):
    s = "{:b}".format(number)
    zeros = re.findall(r'0+', s)
    try:
        max_string = max(zeros)
    except ValueError:
        return 0
    return len(max_string)

# print(binary_gaps(101))


# 2.1 CyclicRotation
# Rotate an array to the right by a given number of steps.
@timer()
def rotate_array(array, times):
    for i in range(times):
        c = array.pop()
        array.insert(0, c)
    return array


@timer()
def rotate_array2(array, times):
    return array[-times:] + array[:-times]


from collections import deque

@timer()
def rotate_array3(array, times):
    q = deque(array)
    return q.rotate(times)

# 0.000614 s
#rotate_array(list('0123456789'*100), 900)
# 0.000008 s
#rotate_array2(list('0123456789'*100), 900)
# 0.000020 s
#rotate_array3(list('0123456789'*100), 900)

class Rotator:
    """The same as cyclic_rotation() except it does just as an iterator."""
    def __init__(self, array, pos):
        self.array = array
        self.pos = pos
        self.next_pos = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self.next_pos == None and self.next_pos == self.pos:
            raise StopIteration
        if self.next_pos == None:
            self.next_pos = self.pos
        pos = self.next_pos
        self.next_pos = self.next_pos + 1
        if self.next_pos == len(self.array):
            self.next_pos = 0
        return self.array[pos]

#r = Rotator(l, 3)
#print(list(r))


# 2.2 OddOccurrencesInArray
# Find value that occurs in odd number of elements.
@timer()
def odd_occurances(arr):
    d = dict()
    for i in arr:
        d.setdefault(i, 0)
        d[i] += 1
    d = filter(lambda x: x[1] == 1, d.items())
    return d[0][0]


from collections import Counter

@timer()
def odd_occurances2(arr):
    return Counter(arr).most_common()[-1]

from collections import Counter

def find_odd_occurence(array):
    if not len(array) % 2:
        raise ValueError("The array does not have contain an odd number of elements")
    counter = Counter(array)
    numbers = [k for k, v in counter.items() if v % 2]
    return numbers

l = [12, 3, 45, 78, 12, 3, 12]
#print(find_odd_occurence(l))

#odd_occurances(list('1234567887654321'*1001+'9'))
#odd_occurances2(list('1234567887654321'*1001+'9'))


# 3.1 TapeEquilibrium
# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
@timer()
def tape_eq(array):
    dif = []
    for border in range(1, len(array)):
        dif.append(abs(sum(array[:border]) - sum(array[border:])))
    return min(dif)

@timer()
def tape_eq2(array):
    dif = [abs(sum(array[:border]) - sum(array[border:]))
               for border in range(1, len(array))]
    return min(dif)

#print(tape_eq([3, 1, 2, 4, 3]*1000))
#print(tape_eq2([3, 1, 2, 4, 3]*1000))


# 3.2 FrogJmp
# Count minimal number of jumps from position X to Y.
import math

def get_frog_jumps(start, finish, step):
    steps = (finish - start) / float(step)
    return math.ceil(steps)



# 3.3 PermMissingElem
# Find the missing element in a given permutation.
def sum_numbers(n):
    return int(n * (n + 1) / 2)

def find_missing_element(array):
    """Find the missing element in a given permutation.

        A zero-indexed array A consisting of N different integers is given.
        The array contains integers in the range [1..(N + 1)], which means
        that exactly one element is missing.
    """
    n = len(array) + 1
    el = sum_numbers(n)
    return el - sum(array)

from random import choice
l = list(range(1, 1001))
l.remove(989)

#print(find_missing_element(l))


# 4.2 PermCheck
# Check whether array A is a permutation.
def is_permitation(array):
    if max(array) == len(set(array)):
        return True
    return False

#print('-'*100)
#print(is_permitation([4, 1, 3, 2]))
#print(is_permitation([4, 1, 2]))


# 4.3 MissingInteger
# Find the minimal positive integer not occurring in a given sequence.
def find_missing_element(array):
    coherent = set(range(1, max(array)))
    return coherent - set(array)

#print('-'*100)
#print(find_missing_element([1, 3, 6, 1, 4, 2]))


# 4.4 MaxCounters
# Calculate the values of counters after applying all alternating
# operations: increase counter by 1; set value of all counters to current maximum.
def run_max_counters(n, array):
    counters = dict.fromkeys(range(1, n+1), 0)
    for i in array:
        if i > n:
            # RESET counters
            # search the max counter
            counter, value = max(d.items(), key=operator.itemgetter(1))
            counters = dict.fromkeys(counters, 0)
            continue
        counters[i] += 1
    return counters

def run_max_counters2(n, array):
    counters = [0] * n
    for i in array:
        if i > n:
            # reset counters to max value
            counters = [max(counters)] * n
            continue
        counters[i-1] += 1
    return counters

#print('-'*100)
#print run_max_counters2(3, [1, 2, 2, 1, 3, 4, 2, 2, 3])


# 5.1 PassingCars
# Count the number of passing cars on the road.
#[0, 1, 0, 1, 1] = (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

def passing_cars(array):
    first, second = array[0], array[0] ^ 1
    passed = 0
    while passed <= 7:
        passed += array.count(second)
        try:
            array = array[array.index(first, 1):]
        except ValueError, e:
            break
    return passed

#print('-'*100)
#print(passing_cars([0,1,0,1,1,0,0,1]))


# 5.2 CountDiv
# Compute number of integers divisible by k in range [a..b].
@timer()
def count_div(a, b, k):
    return len(filter(lambda x: x %k, xrange(a, b+1)))

#print(count_div(1, 2000000, 2))


@timer()
def count_div2(a, b, k):
    return reduce(operator.add, itertools.imap(lambda x: operator.eq(0, x % k), xrange(a, b+1)))

#print(count_div2(6, 11, 2))
#print(count_div2(1, 2000000, 2))


# 5.3 MinAvgTwoSlice
# Find the minimal average of any slice containing at least two elements.
def get_min_avg_slice(array):
    length = len(array)
    avgs = []
    for l in range(2, length+1):
        pos = 0
        while (pos + l < length + 1):
            avg = sum(array[pos: pos+l]) / float(l)
            avgs.append((pos, l, avg, array[pos: pos+l]))
            pos += 1
    return min(avgs, key=operator.itemgetter(2))[0]

a = [4, 2, 1, 1, 1, 1, 8]

#res=get_min_avg_slice(a)
#pprint.pprint(res)


# 5.4 GenomicRangeQuery
# Find the minimal nucleotide from a range of sequence DNA.
def get_genomic_range(dna, p, q):
    nucleotides = [('A', 1), ('C', 2), ('G', 3), ('T', 4)]
    nucleotides = sorted(nucleotides, key=operator.itemgetter(1))
    factors = []
    for i, pk in enumerate(p):
        seq = dna[pk:q[i]+1]
        #print i, pk, q[i], seq
        for n in nucleotides:
            if n[0] in seq:
                factors.append(n[1])
                break
    return factors

#print(get_genomic_range('CAGCCTA', [2, 5, 0], [4, 5, 6]))


# 6.1 Distinct
# Compute number of distinct values in an array.
@timer()
def distinct(array):
    counter = 0
    while array:
        el = array.pop()
        if not el in array:
            counter += 1
            continue
        else:
            try:
                while True:
                    array.remove(el)
            except ValueError:
                continue
    return counter


from collections import Counter

@timer()
def distinct2(array):
    c = Counter(array)
    res = filter(lambda x: x[1] == 1, c.items())
    return len(res)


@timer()
def distinct3(array):
    return len(filter(lambda x: array.count(x)==1, array))


l = range(1, 11) * 1000 + [0, 12]

# elapsed: 0.240349 s
print(distinct(l[:]))
# elapsed: 0.002091 s
print(distinct2(l[:]))
# elapsed: 1.023475 s
print(distinct3(l[:]))


