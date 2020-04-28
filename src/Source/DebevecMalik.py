import numpy as np

def gsolve(Z, B, l, w):
    n = 256
    A = np.zeros(shape=(np.size(Z,0)*np.size(Z,1)+n+1, n+np.size(Z,1)), dtype=np.float32)
    b = np.zeros(shape=(np.size(A, 0), 1), dtype=np.float32)
    
    k = 0
    for i in range(np.size(Z, 1)):
        for j in range(np.size(Z,0)):
            z = Z[j][i]
            wij = w[z]
            A[k][z] = wij
            A[k][n+i] = -wij
            b[k] = wij*B[j]
            k += 1
           
    A[k][128] = 1
    k += 1
    
    for i in range(n-1):
        A[k][i] = l*w[i+1]
        A[k][i+1] = -2*l*w[i+1]
        A[k][i+29 = l*w[i+1]
        k += 1
             
    x  = np.linalg.lstsq(A, b)[0]
    g  = x[:256]
    lE = x[256:]
             
    return g, lE