from matrix import Matrix, Vector

if __name__=="__main__":
    try:
        m1 = Matrix([[0.0,1.0],[2.0,3.0],[4.0,5.0]])
        print(m1.shape)
        print(m1.T())
        print(m1.T().shape)
    except TypeError as e:
        print(e)