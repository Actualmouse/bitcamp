class Jar:
    def __init__(self, capacity=12):
        if type(capacity) != int or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        cookie = ""
        for i in range(self.size):
            cookie += "🍪"
            
        return cookie

    def deposit(self, n):
        if type(n) != int or n < 0:
            raise ValueError
        elif self._size + n > self._capacity:
            raise ValueError
        self._size = self._size + n

    def withdraw(self, n):
        if type(n) != int or n < 0:
            raise ValueError
        elif self._size - n < 0 or self.size - n > self._capacity:
            raise ValueError
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size