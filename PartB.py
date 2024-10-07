import PartA as pA
import os

"""
need comments that explains the runtime of the 
following program

not sure if __name__ == '__main__' is needed
"""
if __name__ == '__main__':
    # asking and checking for the first text file
    while True:
        text_file_1 = input("Path or Name of the first file: ")
        if os.path.exists(text_file_1) : break
        else: print(f"Invalid File: {text_file_1}")
    # asking and checking for the second text file
    while True:
        text_file_2 = input("Path or Name of the second file: ")
        if os.path.exists(text_file_2) : break
        else: print(f"Invalid File: {text_file_2}")

    # tokenizing first file
    tokens1 = pA.tokenize(text_file_1)
    token_dict1 = pA.computeWordFrequencies(tokens1)
    # tokenizing second file
    tokens2 = pA.tokenize(text_file_2)
    token_dict2 = pA.computeWordFrequencies(tokens2)
    # finding the intersection
    common_tokens = token_dict1.keys() & token_dict2.keys()
    print(common_tokens)
    print(f"The two files have {len(common_tokens)} tokens in common which are:\n{common_tokens}")