#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Iterate over tickets and insert into hashtable
    for tk in tickets:

        hash_table_insert(hashtable, tk.source, tk.destination)
    
    # Get first route
    first_route = hash_table_retrieve(hashtable, 'NONE')
    route[0] = first_route

    for i in range(1, len(route)):
        route[i]  = hash_table_retrieve(hashtable, route[i-1])
    # Return the route excluding the last
    return route[:-1]

        