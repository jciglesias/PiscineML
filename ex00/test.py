import matrix

if __name__=="__main__":
    m = [[2], [1]]
    try:
        m = matrix.Vector(m)
    except TypeError as e:
        print(e)