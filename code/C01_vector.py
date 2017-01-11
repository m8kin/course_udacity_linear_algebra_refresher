
# create a class Vector
class Vector(object):
    
    # initialiser function
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    # prints vector function
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    # test if 2 vectors are equal function
    def __eq__(self, v):
        return self.coordinates == v.coordinates
