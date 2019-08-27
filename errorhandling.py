# error handling is really important in coding.
# we have syntax error and exceptions
# syntax error happens due to the typos, etc. and usually programming languages can help alot with those
# exceptions, however, is harder to figure and more fatal. So in order to have a robust code you should 
# handle the errors and take care of the exceptions, and raise exceptions when necessary. 

""" Circuit failure example """

class Circuit:
    def __init__(self, max_amp):
        self.capacity = max_amp # max capacity in amps
        self.load = 0 # current load 

    def connect(self, amps):
        """
        function to check the connectivity 
        :param amps: int
        
        :return: None
        """
        if self.capacity += amps > max_amp:
            raise exceptions("Exceeding max amps!")
        elif self.capacity += amps < 0:
            raise exceptions("Capacity can't be negative")
        else:
            self.capacity += amps
    

