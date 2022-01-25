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

    #CR What is the meaning of self.serial, clarify next coming out? or current serial?
    
    def __init__(self, start=100):
        """ Create serial generator with start"""
        self.start = start
        self.next = start

    def generate(self):
        """ Increments self.serial by one and returns """
        self.next += 1
        return self.next - 1

    def reset(self):
        """ Resets to starting argument """
        self.next = self.start - 1