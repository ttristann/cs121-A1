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
