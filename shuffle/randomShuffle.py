import random


def shuffle(arr_to_shuffle):
    rand_values = [random.random() for i in range(len(arr_to_shuffle))]
    print("Random values " + str(rand_values))
    rand_indexes = [i for i in range(len(arr_to_shuffle))]
    print("Random indexes " + str(rand_indexes))
    rand_indexes.sort(key=lambda k: rand_values[k])
    print("Sorting Random indexes " + str(rand_indexes))
    arr_to_shuffle = [arr_to_shuffle[x] for x in rand_indexes]
    return arr_to_shuffle

test_arr = range(1, 10)
print(test_arr)
test_arr = shuffle(test_arr)
print(test_arr)