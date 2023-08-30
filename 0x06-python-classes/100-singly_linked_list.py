#!/usr/bin/python3

'''
    Defines a node of a singly linked list. And adds the node
    to an existing singly linked list
'''


class Node:
'''
    defines a node. A node has data(private iinstance attr data)
    and a next_node(private instance attr next_node). This is an
    element that points to the next node
'''

    def __init__(self, data, next_node=None)
    '''
        initalizes the private attributrs data and next_node
    '''

        self.__data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' data getter '''
        return self.__data

    @property
    def next_node(self):
        '''next_node getter'''
        return self.__next_node

    @setter.data
    def data(self, value):
        ''' data setter '''
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @setter.next_node
    def next_node(self, value):
        ''' next_node setter '''
        if isinstance(value, None) or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("node must be a Node object")

class SinglyLinkedList:
'''
    defines a singly linked list with a private attr head.
    It is printable
'''
    def __init__(self):
    ''' initialization of head '''
        self.__head = []

    def sorted_insert(self, value):
    ''' inserts a value at the top of the list.
        sorts the list in ascending order
    '''

        self.__head.append(value)
        self.__head.sort()

    def print_list(self, head):
    ''' prints the list '''
        for i in head:
            print("{}".format(head[i]))     
