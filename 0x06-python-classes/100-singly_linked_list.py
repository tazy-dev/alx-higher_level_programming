#!/usr/bin/python3
'''
Defining classes of a single linked list
'''


class Node:
    '''
    A Single linked list Node class
    '''

    def __init__(self, data=0, next_node=None) -> None:
        '''
        Intialize a Node object

        Args:
            data (int): The data of the new node object
            next_node (Node): The next node in the list
        '''
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        '''
        Get the value of data
        '''
        return (self.__data)

    @data.setter
    def data(self, value):
        '''
        Set the value of data
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''
        Get the value of next_node attribute
        '''
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        '''
        Set the value of next_node attribute
        '''
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''
    A Single linked list  class
    '''

    def __init__(self):
        """
        Initalize a new SinglyLinkedList object
        """
        self.__head = None

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        linkedList = []
        Head = self.__head
        while Head is not None:
            linkedList.append(str(Head.data))
            Head = Head.next_node
        return ('\n'.join(linkedList))

    def sorted_insert(self, value):
        '''
        inserts a new Node into the correct sorted position
        in the list (increasing order)

        Args:
            value (int): The value to be inseted to the list
        '''
        node = Node(value)
        if self.__head is None:
            self.__head = node
        elif self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
        else:
            head = self.__head
            while (head.next_node is not None and head.next_node.data < value):
                head = head.next_node
            node.next_node = head.next_node
            head.next_node = node
