
def linear_interpolation( x: float, x0: float, x1: float, y0: float, y1: float) -> float:
    m = (y1-y0)/(x1-x0)
    b = y0 - m * x0
    return (x-x0)*m + y0
