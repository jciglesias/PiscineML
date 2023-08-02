from matrix import Matrix, Vector

if __name__=="__main__":
    try:
        m1 = Matrix([[0.0,1.0],[2.0,3.0],[4.0,5.0]])
        m2 = Matrix([[0.,2.,4.],[1.,3.,5.]])
        m3 = Matrix([[0.0,1.0,2.0,3.0], [0.0,2.0,4.0,6.0]])
        m4 = Matrix([[0.0,1.0], [2.0,3.0], [4.0,5.0], [6.0,7.0]])
        m5 = Matrix([[0.0,1.0,2.0], [0.0,2.0,4.0]])
        v1 = Vector([[1,2,3]])#create a row vector
        v2 = Vector([[1],[2],[3]])#create a column vector
        v3 = Vector([[2],[4],[8]])
        # v4 = Vector([[1,2],[3,4]])#return an error
        print(f"Expected: (3, 2)\noutput  : {m1.shape}")
        print(f"Expected: Matrix([[0.,2.,4.],[1.,3.,5.]])\noutput  : {m1.T()}")
        print(f"Expected: (2, 3)\noutput  : {m1.T().shape}")
        print(f"Expected: (2, 3)\noutput  : {m2.shape}")
        print(f"Expected: Matrix([[0.0,1.0],[2.0,3.0],[4.0,5.0]])\noutput  : {m2.T()}")
        print(f"Expected: (3,2)\noutput  : {m2.T().shape}")
        print(f"Expected: Matrix([[28.,34.],[56.,68.]])\noutput  : {m3 * m4}")
        print(f"Expected: Vector([[0],[6],[18]])\noutput  : {v2 * m5}")
        print(f"Expected: Vector([[3],[6],[11]])\noutput  : {v2 + v3}")

        print(v2 * v3)
        # print(v2)
        # print(v1.dot(v2))
        # print(m1 + m1)
        # print(v1 + v2.T())
        # print(v1 - v2.T())
        # print(v1 / 2)
        # print(2 / v1)
        # print(repr(v1))
        # print(repr(m1))
        # print(m1 * 2)
        # print(m3 * m4)
    except TypeError as e:
        print(e)