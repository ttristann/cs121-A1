import os, sys
from collections import defaultdict
"""
Automatically opens, closes, and reads the text inside the input file.
Each line is processed one at a time to efficiently use memory usage 
and then each character is read from each line to determine if the 
character is alphanumeric. If so, it becomes token and gets yielded,
while other characters are ignored. 

Since the size of a text file is dependent on the amount of characters
inside it and the function goes through the whole input text file once, 
looking at every character of each line to filter only alphanumeric text, 
the runtime complexity of the function is O(n).
"""
def tokenize(TextFilePath):
    try:
        with open(TextFilePath, 'r', encoding = "utf-8") as main_file:
            current_token = [] # the collector of each char that builds up to a token
            for line in main_file:
                for char in line:
                    if ('A' <= char <='Z') or ('a' <= char <= 'z') or ('0' <= char <= '9'): # checking for alphanumeric value
                        current_token.append(char.lower()) # O(1) - lowers the char to account for capitalization
                    else:
                        if current_token:
                            yield ''.join(current_token) # O(n) - uses join to build together word that counts as a token
                            current_token = [] # resets it to make a new token
            if current_token:
                yield ''.join(current_token) # accounts for the last token to be yielded
    except FileNotFoundError as file_error:
        print(f"The file does not exist: {TextFilePath}")
    except UnicodeDecodeError as decode_error:
        print(f"The file cannot be decoded: {TextFilePath}")

"""
Creates a default dictionary object to keep track the frequencies of 
the tokens while iterating through the stream of tokens that are 
generated or yielded from the tokenize function. 

The function iterates through stream of tokens of varying sizes only
one time, so the runtime complexity of this function is O(n). 
"""
def computeWordFrequencies(tokens): 
    main_dict = defaultdict(int) # keeps track of tokens and their frequencies
    for token in tokens: # O(n) - iterates through the yielded tokens
        main_dict[token] += 1
    
    return main_dict

"""
Sorts in descending order of the passed argument of an object that holds 
the tokens and their frequencies  which is assumed to be a dictionary 
in this case. Then, the tokens are printed in descending order based on
the token's frequency in the format of: <token> - <frequency>.

The runtime complexity of this function is O(nlogn) because the function has
to sort the passed argument in descending order while the other operations of
creating the dictionary, iterating over it, and printing are all O(n) which 
are less significant to the sorting runtime complexity. 
"""
def printFrequencies(token_dict):
    sorted_dict = dict(sorted(token_dict.items(), key=lambda x: x[1], reverse=True)) # O(nlogn) - sorting algorithm is O(nlogn)
    for token, count in sorted_dict.items(): # O(n) - iterates through the keys of the sorted dictionary
        print(f'{token} - {count}')



"""
Main program that executes all of the defined functions above.
It takes an input from the terminal for a path or name of the
text file to be processed and validated, calls the defined functions above 
with the proper arguments stemming from the input, and prints
the token frequencies. 
"""
if __name__ == '__main__':
    try:
        main_file = tokenize(sys.argv[1])
        main_dict = computeWordFrequencies(main_file)
        printFrequencies(main_dict)
    except IndexError as error:
        print(f"Arguments cannot be indexed properly")