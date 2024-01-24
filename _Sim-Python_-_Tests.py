def test():
    a = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
    del a[2]
    return a

a = test()
print(a)
