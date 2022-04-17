import random


def partition(arr_to_part, start, end):
    # partition keeping end element as pivot
    pivot = arr_to_part[end]
    print("Start : " + str(start) + " End: " + str(end) + " Pivot = " + str(pivot))
    print("org arr : " + str(arr_to_part))
    # p_idx is the partiton index
    # Invariant-> all elements to the left of p_idx will be less than equal to pivot
    # all elements to the right of p_idx will be greater than pivot
    p_idx = start
    for i in range(start, end):
        if arr_to_part[i] <= pivot:
            # swap the el[p_idx], el[i] and increment the p_idx
            arr_to_part[i], arr_to_part[p_idx] = arr_to_part[p_idx], arr_to_part[i]
            p_idx += 1

    print("Partition index = " + str(p_idx))
    # move the pivot to p_idx
    arr_to_part[p_idx], arr_to_part[end] = arr_to_part[end], arr_to_part[p_idx]
    print("after partitioning : " + str(arr_to_part))
    return p_idx


def qs_driver(arr_to_sort, start, end):
    if start < end:
        par_idx = partition(arr_to_sort, start, end)
        qs_driver(arr_to_sort, start, par_idx - 1)
        qs_driver(arr_to_sort, par_idx + 1, end)


def quick_sort(arr_to_sort):
    qs_driver(arr_to_sort, 0, len(arr_to_sort) - 1)


test_arr = [10, 11, 12, 9, 8, 7, 1, 2]

print(test_arr)
quick_sort(test_arr)
print(test_arr)
