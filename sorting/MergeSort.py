def merge(left, right, merged_arr):
    lenL = len(left)
    lenR = len(right)
    i, j, k = 0, 0, 0
    while i < lenL and j < lenR:
        if left[i] <= right[j]:
            merged_arr[k] = left[i]
            i += 1
        else:
            merged_arr[k] = right[j]
            j += 1
        k += 1
    while i < lenL:
        merged_arr[k] = left[i]
        i += 1
        k += 1

    while j < lenR:
        merged_arr[k] = right[j]
        j += 1
        k += 1

    return


def merge_sort(arr_to_sort):
    size = len(arr_to_sort)
    if size < 2:
        return
    mid = size // 2
    left = arr_to_sort[:mid]
    right = arr_to_sort[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr_to_sort)


test_array = [1,2]
print("Original Array: ", test_array)
merge_sort(test_array)
print(test_array)
