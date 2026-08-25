import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here

    n = len(x)
    dot_p = 0
    
    for i in range(n):
        dot_p = dot_p + (x[i] * y[i])

    return float(dot_p)