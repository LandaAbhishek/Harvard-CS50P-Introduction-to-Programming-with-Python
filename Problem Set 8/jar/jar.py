# defining jar application
def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)

# function for cookie jar
class Jar:
    # initialize jar
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    # jar display
    def __str__(self):
        return "🍪" * self._size

    # deposit cookies to jar
    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Deposit error")
        self.size += n

    # withdraw cookies from jar
    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Withdraw error")
        self.size -= n

    # set jar capacity
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("@capacity.setter error")
        self._capacity = capacity

    # set jar size
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("@size.setter error")
        self._size = size

# calling main function
if __name__ == "__main__":
    main()
