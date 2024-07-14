"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0):
        """make generator, starting at given number"""
        self.start, self.next = start, start

    
    def __repr__(self):
        """Returns data in SerialGenerator in formatted way"""
        return f"<SerialGenerator start={self.start} next={next.start}"

    def generate(self):
        """generate the next serial number in sequence"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """reset next to equal start"""
        self.next = self.start