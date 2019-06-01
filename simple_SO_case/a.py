def linear(a, b):
    ''' Solve ax + b = 0

        >>> linear(3, 5)
        -1.6666666666666667

    '''
    if a == 0 and b != 0:
        raise ValueError('No solutions')
    return -b  / a
