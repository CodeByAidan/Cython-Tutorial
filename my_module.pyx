cdef int c_fibonacci(int n):
    cdef int a = 0
    cdef int b = 1
    cdef int i, temp

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            temp = b
            b = a + b
            a = temp
        return b

def fibonacci(int n):
    return c_fibonacci(n)