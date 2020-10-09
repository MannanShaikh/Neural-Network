import numpy as np
x = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
w = np.array([[1, 1]])
w_t = w.transpose()
function = np.dot(x, w_t)
sigmoid = 1/(1 + np.exp(-function))
for a in sigmoid:
    if a < 0.5:
        {
            print(0)
        }
    else:
        {
            print(1)
        }
