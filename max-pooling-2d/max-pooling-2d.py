import numpy as np

def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    # Write code here
    X_arr = np.array(X)
    h, w = X_arr.shape
    h_out = h // pool_size
    w_out = w // pool_size

    # print(h_out, w_out)

    out = []

    for i in range((h_out)):
        pooled_row = []
        for j in range((w_out)):
            pooled_val = -100000000
            for a in range(pool_size):
                for b in range(pool_size):

                    if (i*pool_size + a) < h and (j*pool_size +b) < w:
                        # print(i, j, a, b)
                        # print("before")
                        pooled_val = max(pooled_val, X[i*pool_size+a][j*pool_size+b])
                        # print("after")

            pooled_row.append(pooled_val)
        out.append(pooled_row)

    return out