import re
from collections import defaultdict
"""
Automatically opens, closes, and reads the text inside the input file.
After reading it and converting the text to a string object, regex is
used to filter to find the alphanumeric text to be converted into token. 

Since this function goes through the whole input text file to filter only
alphanumeric text, the runtime complexity of the function is O(n).
"""
def tokenize(TextFilePath):
    with open(TextFilePath, 'r') as main_file:
        main_text = main_file.read()
    
    tokens_list = re.findall(r'\b[a-zA-Z0-9]+\b', main_text)
    tokens_list = [token.lower() for token in tokens_list]
    
    return tokens_list

"""
Creates a default dictionary object to keep track the frequencies of 
the tokens while iterating through the list of tokens that are
passed to the function. 

The function iterates through the passed argument of list of tokens,
so the runtime complexity of this function is O(n). 
"""
def computeWordFrequencies(tokens): 
    main_dict = defaultdict(int)
    for token in tokens:
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
    sorted_dict = dict(sorted(token_dict.items(), key=lambda x: x[1], reverse=True))
    for token, count in sorted_dict.items():
        print(f'{token} - {count}')



"""
Main program that executes all of the defined functions above.
It takes an input from the terminal for a path or name of the
text file to be processed, calls the defined functions above 
with the proper arguments stemming from the input, and prints
the token frequencies. 
"""
if __name__ == '__main__':
    main_input = input("path or name of the text file: ")
    tokens = tokenize(main_input)
    token_dict = computeWordFrequencies(tokens)
    printFrequencies(token_dict)