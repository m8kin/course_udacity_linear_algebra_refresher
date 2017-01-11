
def unitVector(array):
    '''
    this function Normalises a vector of any magnitude to a magnitude of 1
    it first calculates the magntude and then divides each element in the array by this
    imput is a numpy array
    requires: numpy
    '''
    import numpy as np
    import math
    
    array_sq = np.square(array)
    array_sum_sq = np.sum(array_sq)
    magnitude = math.sqrt(array_sum_sq)
    unit_vector = np.divide(array,magnitude)
    unit_vector = np.round(unit_vector,3)
    
    return unit_vector
    
    