from varname import will


class AwesomeClass:
    def __init__(self):
        self.will = None

    def permit(self):
        self.will = will(raise_exc=False)
        if self.will == 'do':
            # let self handle do
            return self
        raise AttributeError('Should do something with AwesomeClass object')

    def do(self):
        if self.will != 'do':
            raise AttributeError("You don't have permission to do")
        return 'I am doing!'


awesome = AwesomeClass()
# awesome.do()  # AttributeError: You don't have permission to do
# awesome.permit()  # AttributeError: Should do something with AwesomeClass object
awesome.permit().do() == 'I am doing!'
