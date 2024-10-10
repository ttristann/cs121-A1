import PartA as pA
import os, sys

"""
The main program calls the tokenize function for each text file inputted
into the terminal and then creates a set of unique of tokens generated
from the tokenize function. It then checks the intersection of those two
sets of unique tokens and counts it. 

Since the tokenize function being called twice which would be O(n) + O(m), 
the creation of the two unique sets of tokens which would be O(n1) + (m1), 
and finding the intersection of those two unique sets is O(min(n1, m1)),
the total runtime complexity is O(n + n1 + m + m1 + min(n1, m1)). 
However, this complexity can be simplified to just O(n + m) because usually
there would be less unique tokens than the total tokens (n > n1 & m > m1).
"""
def main_program():
    try:
        text_file_1 = pA.tokenize(sys.argv[1]) # O(n) - tokenizing first file if valid
        text_file_2 = pA.tokenize(sys.argv[2]) # O(n) - tokenizing second file if valid
        
        token_set_1 = {token for token in text_file_1} # O(n1) - set of only unique tokens in first text file
        token_set_2 = {token for token in text_file_2} # O(m1) - set of only unique tokens in second text file

        print(len(token_set_1 & token_set_2)) # O(min(n1,m1)) - counting the amount of similar tokens within both files

    except IndexError as index_error:
        print("Arguments cannot be index properly")
    except FileNotFoundError as file_error:
        print(f"The file does not exist: {file_error.filename}")
    except UnicodeDecodeError as decode_error:
        print(f"The file cannot be decoded: {sys.argv[decode_error.start]}")

if __name__ == '__main__':
    main_program()