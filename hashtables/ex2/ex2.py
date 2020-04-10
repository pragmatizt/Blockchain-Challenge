#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


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

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # First item has a 'NONE' value
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    # Start with 1, since 0th is confirmed
    for index in range(1, length):
        # Next destination uses the previous key as destination value
        route[index] = hash_table_retrieve(hashtable, route[index-1])

    # Remove the destination 'NONE' value
    return route[0:length-1]

