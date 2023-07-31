class Matrix:
    shape = tuple()

    def T():
        pass

    def __init__(self, arg):
        if isinstance(arg, list):
            if not arg or not len(arg) or not isinstance(arg[0], list):
                raise TypeError("Argument must be a list of lists")
            self.data = arg
            self.shape = (len(arg), len(arg[0]))
            for row in self.data:
                if not isinstance(row, list):
                    raise TypeError("Argument must be a list of lists")
                if len(row) != self.shape[1]:
                    raise TypeError("Bad dimentions for matrix")
        elif isinstance(arg, tuple):
            self.shape = arg
            self.data = []
            for i in range(self.shape[0]):
                self.data.append([])
                for j in range(self.shape[1]):
                    self.data[i].append(0)
        else:
            raise TypeError("Argument must be of type List of Lists or tuple.")
    #add:only matrices of same dimensions.
    def __add__():
        pass
    def __radd__():
        pass
    #sub:only matrices of same dimensions.
    def __sub__():
        pass
    def __rsub__():
        pass
    #div:onlyscalars.
    def __truediv__():
        pass
    def __rtruediv__():
        pass
    #mul:scalars,vectors and matrices,can have errors with vectors and matrices,
    #returns a Vector if we perform Matrix * Vector mutliplication.
    def __mul__():
        pass
    def __rmul__():
        pass
    def __str__():
        pass
    def __repr__():
        pass

class Vector(Matrix):
    def __init__(self, arg):
        super().__init__(arg)
        if not (self.shape[0] != 1) ^ (self.shape[1] != 1):
            raise TypeError("Argument is not a Vector")
    def dot(self, v):
        if not isinstance(v, Vector):
            raise TypeError("Argument must be of type Vector.")
        pass
