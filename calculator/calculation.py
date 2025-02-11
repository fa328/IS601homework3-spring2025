'''Calculations Class functions'''
class Calculations: # pylint: disable=too-few-public-methods
    '''Calculations functions'''
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self):
        '''Get result functions'''
        return self.operation(self.a, self.b)
