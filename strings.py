# split is a function that breaks a string sentence into different words, which can then be organized by indexing

def first_word(s: str) -> str:
    return s.split()[0]

def first_word(s: str) -> str:
    word = ""
    for char in s:
        if char == " ":
            break
        word += char
    return word

def first_word(s: str) -> str: #we are creating a new function called first_word that finds the first word in a sentence of strings and the return / output of this function will also be a string
    word = "" #an empty space to hold the string
    for char in s: # you are seperating the words manually instead pf using .split 
        if char == " ":  # but if that char is an empty space then you break because it must be only words 
            break # to break means to avoid it fyfiy
        word += char # but if it is not an empty space you add that word to the empty string called word
    return word # You will keep on adding all these words together and then return the final string which is a sentence 

def print_words(s: str):
    word = ""
    for char in s:
        if char == " ":
            if word:  # Print word when space is encountered
                print(word)
                word = ""  # Reset for next word
        else:
            word += char  # Build the word
    
    if word:  # Print the last word (since it won't be followed by a space)
        print(word)

# Example Usage:
print_words("Hello world this is Python")
