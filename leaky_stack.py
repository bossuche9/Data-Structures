"""
Implement all the missing functionality in the code with docstrings.

Name: <add your name here>
Citations: <any websites/people that you consulted while writing this code>
"""
from pythonds3.basic import UnorderedList

class LeakyStack(UnorderedList):
    """Docstring
    """

    def __init__(self, capacity):
        """
        """
        super().__init__()
        # Complete this.
        self.maxsize = capacity
        self.stack = UnorderedList()

    def __len__(self):
        """
        """
        return super().__len__()

    def is_empty(self):
        """
        """
        return self.stack.is_empty()

    def push(self, item):
        """
        """
        if self.stack.size() > self.maxsize:
            current = self.stack._head
            previous = None

            while current.get_next() is not None:
             previous = current
             current = current.get_next()
            if previous is not None:
                previous.set_next(None)
            else:
                self.stack._head = None
        self.stack.add(item)

    def pop(self):
        """
        """
        return self.stack.remove(self._head)

    def peek(self):
        """
        """
        return self._head.get_data()

    def size(self):
        """
        """
        return self.stack.size()

    def __str__(self):
        """String representation
        """
        return 'Leaky Stack'