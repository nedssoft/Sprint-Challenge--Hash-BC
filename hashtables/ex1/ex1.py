#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):
        weight = weights[i]
        # Insert the wight into the hashtable
        hash_table_insert(ht, weight, i)

        weight_diff = limit - weight

        value = hash_table_retrieve(ht, weight_diff)

        if value and length == 2:
            return (1,0)
        if value:
            return (i, value)
        

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
