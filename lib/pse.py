# clarifying questions
# What if there is a tie for most frequent value at the k boundary?
#   We will return A correct answer, but no guarantees about which one
# What if k is invalid?
#   We will assume that the code will end up raising an error of some kind
# What if there are negative nums?
#   They should just work, like a positive number.

# Logical steps
# 1. Build a frequency map of the list elements and their count
# 2. Get the unique elements of the list into a new list, from map keys
# 3. sort the unique values based on their counts
# 4. return the first k values

# takes an array of values and generates a frequency map
def make_counts(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        # count = counts.get(num, 0)
        # counts[num] = count + 1

    return counts

# partitions an array of values using the supplied counts until the pivot is
# at k, which means everything with larger counts is before k
# adapted from the partition phase of Quick Sort
def partition(arr, counts, k):
    start = 0
    end = len(arr)  # using convention that end of range is exclusive
    pc = start  # location of pivot candidate (pc)

    while pc != k:
        pp = end - 1  # the position of the pivot (pp) value we'll be using
        pivot = counts[arr[pp]]  # look up the count of the value stored in the pivot
        for i in range(start, pp):  # we don't want to include the pivot in the range
            count = counts[arr[i]]  # count of the current index value
            if count > pivot:
                # this is larger than pivot, so should come ahead of it
                arr[i], arr[pc] = arr[pc], arr[i]
                pc += 1  # the pivot candidate is now 1 location later

        arr[pc], arr[pp] = arr[pp], arr[pc]  # swap the pivot value to the final location of the candidate

        # Quick Sort would partition the left AND the right
        # Here, we only need to partition to the left OR the right. Which ever direction
        # we need to move in order to find the value that belongs in position k
        if pc < k:
            # we haven't partitioned enough values larger than k
            start = pc + 1  # we need to move to the right of the current pivot
        elif pc > k:
            # there are too many values larger than the pivot
            end = pc  # narrow the region to the left og the current pivot
        else:
            return  # the k most frequent values are ahead of the pivot

        pc = start  # reset the candidate to the start of the new range

def most_frequent_k_elements(arr, k):
    counts = make_counts(arr)  # time: O(n), space: O(n)
    uniq_nums = list(counts.keys())  # O(n), O(n)
    uniq_nums.sort(key=lambda num: counts[num], reverse=True)  # O(n log n), O(n) (assuming merge sort)
    # uniq_nums.sort(key=counts.get, reverse=True)
    # partition(uniq_nums, counts, k) # O(n), O(1)
    return uniq_nums[:k]  # O(n), O(n)
