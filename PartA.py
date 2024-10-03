import re
from collections import defaultdict
"""
Automatically opens, closes, and reads the text inside the input file.
After reading it and converting the text to a string object, regex is
used to filter to find the alphanumeric text to be converted into token. 

Since this function goes through the whole input text file to filter only
alphanumeric text, the runtime complexity of is O(n)
"""
def tokenize(TextFilePath):
    with open(TextFilePath, 'r') as main_file:
        main_text = main_file.read()
    
    tokens_list = re.findall(r'\b[a-zA-Z0-9]+\b', main_text)
    
    return tokens_list