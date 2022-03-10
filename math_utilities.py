
def linear_interpolation( x, x0, x1, y0, y1):
    m = (y1-y0)/(x1-x0)
    b = y0 - m * x0
    print('m: {}'.format(m))
    print('b: {}'.format(b))
    return (x-x0)*m + y0