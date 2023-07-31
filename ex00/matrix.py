class Matrix:
    shape = tuple()

    def T():
        pass

    def __init__(self, arg):
        if isinstance(arg, list):
            self.data = arg
            self.shape = (len(arg), len(arg[0]))
        elif isinstance(arg, tuple):
            self.shape = arg
            self.data = []
            for i in range(self.shape[0]):
                self.data.append([])
                for j in range(self.shape[1]):
                    self.data[i].append(0)
        else:
            raise TypeError("Argument must be of type List of List or tuple.")
        print("Matrix init")
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
        if (self.shape[0] != 1) ^ (self.shape[1] != 1):
            print("Is vector")
    def dot(self, v):
        if not isinstance(v, Vector):
            raise TypeError("Argument 'v' must be of type Vector.")
        pass