import os
from collections import defaultdict
"""
Automatically opens, closes, and reads the text inside the input file.
Each line is processed one at a time to efficiently use memory usage 
and then each character is read from each line to determine if the 
character is alphanumeric. If so, it becomes token and gets yielded,
while other characters are ignored. 

Since this function goes through the whole input text file, looking at 
every character of each line to filter only alphanumeric text, the 
runtime complexity of the function is O(n).
"""
def tokenize(TextFilePath):
    with open(TextFilePath, 'r') as main_file:
        current_token = []
        for line in main_file:
            for char in line:
                if char.isalnum():
                    current_token.append(char.lower()) 
                else:
                    if current_token:
                        yield ''.join(current_token)
                        current_token = []

        if current_token:
            yield current_token

"""
Creates a default dictionary object to keep track the frequencies of 
the tokens while iterating through the stream of tokens that are 
generated or yielded from the tokenize function. 

The function iterates through stream of tokens of varying sizes,
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
text file to be processed and validated, calls the defined functions above 
with the proper arguments stemming from the input, and prints
the token frequencies. 
"""
if __name__ == '__main__':
    """
    Asks for an input, if input is valid, it will continue out
    of the loop, otherwise it will loop back to ask for input again.
    """
    while True:
        main_input = input("Path or Name of the text file: ")
        if os.path.exists(main_input) : break
        else: print(f"Invalid File: {main_input}")
    tokens = tokenize(main_input)
    token_dict = computeWordFrequencies(tokens)
    printFrequencies(token_dict)