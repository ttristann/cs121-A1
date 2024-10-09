import PartA as pA
import os, sys

"""
need comments that explains the runtime of the 
following program

not sure if __name__ == '__main__' is needed
"""
if __name__ == '__main__':
    try:
        text_file_1 = pA.tokenize(sys.argv[1]) # O(n) - tokenizing first file if valid
        text_file_2 = pA.tokenize(sys.argv[2]) # O(n) - tokenizing second file if valid

        token_set_1 = {token for token in text_file_1} # O(n1) - set of only unique tokens in first text file
        token_set_2 = {token for token in text_file_2} # O(m1) - set of only unique tokens in second text file

        print(len(token_set_1 & token_set_2)) # O(min(n1,m1)) - counting the amount of similar tokens within both files

    except IndexError as index_error:
        print("Arguments cannot be index properly")