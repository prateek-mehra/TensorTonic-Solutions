import numpy as np
import math

def eu_norm(x):

    eu_norm = 0
    for ele in x:
        eu_norm = eu_norm + ele*ele

    eu_norm = math.sqrt(eu_norm)

    return eu_norm

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here

    if eu_norm(a) == 0 or eu_norm(b) == 0:
        return 0.0

    dot_p = 0

    n = len(a)
    
    for i in range(n):
        dot_p = dot_p + (a[i] * b[i])

    dot_p = float(dot_p)

    cos_sim = dot_p / eu_norm(a)
    cos_sim = cos_sim / eu_norm(b)

    return cos_sim
    
    