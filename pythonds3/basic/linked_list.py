#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""

from abc import ABC, abstractmethod
from typing import Any, Union


class LinkedListNode:
    """A node of a linked list"""

    def __init__(self, node_data: Any) -> None:
        """Create new node"""
        self._data = node_data
        self._next: Union["LinkedListNode", None] = None

    def get_data(self) -> Any:
        """Get node data"""
        return self._data

    def set_data(self, node_data: Any) -> None:
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self) -> Union["LinkedListNode", None]:
        """Get next node"""
        return self._next

    def set_next(self, node_next: Union["LinkedListNode", None]) -> None:
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self) -> str:
        """String"""
        return str(self._data)


class LinkedList(ABC):
    """Linked List class implementation"""

    def __init__(self) -> None:
        """Create a linked list"""
        self._head: Union["LinkedListNode", None] = None
        self._count = 0

    def is_empty(self) -> bool:
        """Is the list empty"""
        return self._head is None

    def size(self) -> int:
        """Size of the list"""
        return self._count

    def __len__(self) -> int:
        """Size of the list"""
        return self._count

    def __str__(self) -> str:
        """List as a string"""
        list_str = "["
        current = self._head

        while current:
            list_str += str(current)
            if current.next:
                list_str += ", "
            current = current.next
        list_str += "]"
        return list_str

    @abstractmethod
    def add(self, value: Any) -> None:
        """Add a new node"""
        raise NotImplementedError

    @abstractmethod
    def remove(self, value):
        """Remove a node with a specific value"""
        ...

    @abstractmethod
    def search(self, value: Any) -> bool:
        """Search for a node with a specific value"""
        raise NotImplementedError


class UnorderedList(LinkedList):
    """Unordered linked list implementation"""

    def __init__(self) -> None:
        """Create an unordered linked list"""
        LinkedList.__init__(self)

    def add(self, value: Any) -> None:
        """Add a new node"""
        new_node = LinkedListNode(value)
        new_node.set_next(self._head)
        self._head = new_node
        self._count = self._count + 1

    def remove(self, value: Any) -> None:
        """Remove a node with a specific value"""
        current = self._head
        prev = None

        while current:
            if current.data == value:
                if prev is None:
                    self._head = current.next
                else:
                    prev.next = current.next
                self._count = self._count - 1
                return
            prev = current
            current = current.next
        raise ValueError(f"{value} is not in the list")

    def search(self, value: Any) -> bool:
        """Search for a node with a specific value"""
        current = self._head

        while current:
            if current.data == value:
                return True
            current = current.next
        return False


class OrderedList(LinkedList):
    """Ordered linked list implementation"""

    def __init__(self) -> None:
        """Create an ordered linked list"""
        LinkedList.__init__(self)

    def add(self, value: Any) -> None:
        """Add a new node"""
        current = self._head
        prev = None
        new_node = LinkedListNode(value)

        while current and current.data < value:
            prev = current
            current = current.next

        if prev is None:
            new_node.next = self._head
            self._head = new_node
        else:
            new_node.next = current
            prev.next = new_node
        self._count = self._count + 1

    def remove(self, value: Any) -> None:
        """Remove a node with a specific value"""
        # NOTE: This is an exercise
        ...

    def search(self, value: Any) -> bool:
        """Search for a node with a specific value"""
        # NOTE: This is an exercise
        
