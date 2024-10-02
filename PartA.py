import re
from collections import defaultdict
"""
TO DO:
- play around with regex code
"""
# def tokenize(textFilePath):
#     with open(textFilePath, 'r') as main_file:
#         main_text = main_file.read()
    
#     tokens_list = re.findall(r'\b[a-zA-Z0-9]+\b', main_text)
#     print("inside\n")
#     print(tokens_list)
    
#     return tokens_list

# print(tokenize("/Users/tristangalang/Desktop/ICS/CS121/A1 - Text Processing/practice_file.txt"))

practice_string = "This isn't a practice for 5 dim-wits at the University of California, Irvine."
tokens = re.findall(r'\b[a-zA-Z0-9]+\b', practice_string)
print(tokens)