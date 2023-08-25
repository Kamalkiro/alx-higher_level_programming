#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
        A fnct that returns square value of all elmts in a
        multi dimensional list been passed as argts
        Returns a new matrix that have same size as size of the
        matrix passed to it as argts
        You are allowed to use regular loops, map...
    '''

    new_list = []
    if len(matrix) == 0:
        return new_list

    new_list = [[i*i for i in j] for j in matrix]
    return new_list
