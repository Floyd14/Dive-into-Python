__author__ = 'Andrea'

'''Show usage for common Datatypes.

This contains some methods to show the common usage for the most important Datatypes like:

Native datatypes:
    Booleans are either True or False.
    Numbers can be integers (1 and 2), floats (1.1 and 1.2), fractions (1/2 and 2/3), or even complex numbers.
    Strings are sequences of Unicode characters, e.g. an html document.
    Bytes and byte arrays, e.g. a jpeg image file.
    Lists are ordered sequences of values.
    Tuples are ordered, immutable sequences of values.
    Sets are unordered bags of values.
    Dictionaries are unordered bags of key-value pairs.
    '''

def return_type_of_object():
    """Print types of some data

    :return: None
    """


    a=type(1)
    type(1.0)
    type(True)

    print("{0:s}".format(a) )


if __name__ == '__main__':
    return_type_of_object()
