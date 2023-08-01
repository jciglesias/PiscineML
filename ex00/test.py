from matrix import Matrix, Vector

if __name__=="__main__":
    try:
        m1 = Matrix([[0.0,1.0],[2.0,3.0],[4.0,5.0]])
        m2 = Matrix([[0.0,1.0,2.0],[3.0,4.0,5.0]])
        print(m1.shape)
        print(m1.T())
        print(m1.T().shape)
        v1=Vector([[1,2,3]])#create a row vector
        print(v1)
        v2=Vector([[1],[2],[3]])#create a column vector
        print(v2)
        # v3=Vector([[1,2],[3,4]])#return an error
        print(v1.dot(v2))
        print(m1 + m1)
        print(v1 + v2.T())
        print(v1 - v2.T())
        print(v1 / 2)
        print(2 / v1)
        print(repr(v1))
        print(repr(m1))
        print(m1 * 2)
        print(m2*m1)
    except TypeError as e:
        print(e)