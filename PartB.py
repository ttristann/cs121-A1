import PartA as pA
import os, sys

"""
need comments that explains the runtime of the 
following program

not sure if __name__ == '__main__' is needed
"""
if __name__ == '__main__':
    # # asking and checking for the first text file
    # while True:
    #     text_file_1 = input("Path or Name of the first file: ")
    #     if os.path.exists(text_file_1) : break
    #     else: print(f"Invalid File: {text_file_1}")
    # # asking and checking for the second text file
    # while True:
    #     text_file_2 = input("Path or Name of the second file: ")
    #     if os.path.exists(text_file_2) : break
    #     else: print(f"Invalid File: {text_file_2}")

    # # tokenizing first file
    # tokens1 = pA.tokenize(text_file_1)
    # token_dict1 = pA.computeWordFrequencies(tokens1)
    # # tokenizing second file
    # tokens2 = pA.tokenize(text_file_2)
    # token_dict2 = pA.computeWordFrequencies(tokens2)
    # # finding the intersection
    # common_tokens = token_dict1.keys() & token_dict2.keys()
    # print(f"The two files have {len(common_tokens)} tokens in common which are:\n{common_tokens}")
    try:
        text_file_1 = pA.tokenize(sys.argv[1]) # O(n) - tokenizing first file if valid
        text_file_2 = pA.tokenize(sys.argv[2]) # O(n) - tokenizing second file if valid

        token_dict_1 = pA.computeWordFrequencies(text_file_1) # O(n) - counting frequencies of tokens in first file
        token_dict_2 = pA.computeWordFrequencies(text_file_2) # O(n) - counting frequencies of tokens in second file

        print(len(token_dict_1.keys() & token_dict_2.keys())) # O(m+n) -  getting keys/tokens & O(min(m, n)) - intersection

    except IndexError as index_error:
        print("Arguments cannot be index properly")