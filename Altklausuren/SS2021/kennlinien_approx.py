import numpy as np
def kennlinie(x, a=1, b=1):
    return (x/a * np.abs(np.tanh(x/b)))