import numpy as np

def als(V, err, maxiter):
    r = min(V.shape[0], V.shape[1]) - 1
    H = np.random.uniform(size=(r, V.shape[1]))
    H_inv = np.linalg.inv(H.dot(H.T))
    W_inv = np.empty(shape=(0, 0))
    i = 0
    error = np.inf
    while i < maxiter and error > err:
        
        Wt = H_inv.dot(H).dot(V.T)
        W = Wt.T
        W[W < 0] = 1e-7
        W_inv = np.linalg.inv(W.T.dot(W))
        H = W_inv.dot(W.T).dot(V)
        H[H < 0] = 1e-7
        factorization = W.dot(H)
        error = np.sqrt(np.sum((V - factorization)**2))
        i += 1

    return {
        "W": W,
        "H": H,
    }
