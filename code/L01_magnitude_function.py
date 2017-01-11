def computeMagnitude(array):
    '''
    this function computes the magnitude of any given vector
    imput is a numpy array
    requires: numpy
    '''
    import numpy as np
    import math
    
    array_sq = np.square(array)
    array_sum_sq = np.sum(array_sq)
    magnitude = math.sqrt(array_sum_sq)
    magnitude = np.round(magnitude,3)
    
    return magnitude
    
