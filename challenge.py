def add_prefix_un(word):
    # Check if the word already starts with "un"
    if word.startswith("un"):
        print(word)  # If it does, print the word as it is
    else:
        new_word = "un" + word  # If it doesn't, add "un" as a prefix to the word
        print(new_word)  # Print the new word with the prefix

# Test the function with different words
add_prefix_un("happy")  # Should print "unhappy"
add_prefix_un("unhappy")  # Should print "unhappy" (already starts with "un")
add_prefix_un("manageable")  # Should print "unmanageable"
add_prefix_un("necessary")  # Should print "unnecessary"


def make_word_groups(vocab_words: list):
    # Create an empty list to store the modified words
    new_words = []

    # Iterate over the vocab_words starting from the second word
    for word in vocab_words[1:]:
        # Check if the word starts with the first word in the list
        if word.startswith(vocab_words[0]):
            new_words.append(word)  # If it does, add the word to the new_words list
        else:
            new_word = vocab_words[0] + word  # If it doesn't, concatenate the first word with the current word
            new_words.append(new_word)  # Add the new word to the new_words list

    # Join the modified words using " :: " as a separator
    output_words = " :: ".join(new_words)

    # Print the resulting string of joined words
    print(output_words)

# Test the function with different lists of words
make_word_groups(['en', 'close', 'joy', 'lighten'])  # Should print "en :: enclosure :: enjoy :: enlightenment"
make_word_groups(['en', 'enclose', 'joy', 'enlighten'])  # Should print "en :: enclose :: enjoy :: enlighten"
make_word_groups(['pre', 'serve', 'dispose', 'position'])  # Should print "pre :: preserve :: predispose :: preposition"
make_word_groups(['auto', 'didactic', 'graph', 'mate'])  # Should print "auto :: autodidactic :: autograph :: automate"
make_word_groups(['inter', 'twine', 'connected', 'dependent'])  # Should print "inter :: intertwine :: interconnected :: interdependent"


def remove_suffix_ness(word):
    # Check if the word ends with "ness"
    if word.endswith("ness"):
        # Check if the character at index -5 (5th from the end) is "i"
        if word[-5] == "i":
            new_word = word[:-5] + "y"  # If it is, remove "ness" and replace "i" with "y"
            print(new_word)
        else:
            new_word = word[:-4]  # If it's not "i", remove "ness" without any changes
            print(new_word)
    else:
        print(word)  # If the word doesn't end with "ness", print the word as it is

# Test the function with different words
remove_suffix_ness("heaviness")  # Should print "heavy"
remove_suffix_ness("sadness")  # Should print "sad"
remove_suffix_ness("eager")  # Should print "eager" (no "ness" suffix)


import string

def adjective_to_verb(sentence, index):
    try: 
        index = int(index)  # Convert the index variable to an integer
    except ValueError:
        print("The index variable must be an integer.")
        return
    
    words = sentence.split(" ")  # Split the sentence into a list of words
    
    # Iterate over the words in the list
    for count, word in enumerate(words):
        # Iterate over each character in the word
        for character in word:
            if character in string.punctuation:
                # Remove any punctuation characters from the word
                no_punctuation_word = word.replace(character, "")
                words[count] = no_punctuation_word  # Replace the word with the modified word without punctuation
    
    # Check if the word at the given index ends with "en"
    if words[index].endswith("en"):
        print(words[index].strip("."))  # If it does, print the word without the trailing period
    else:
        new_word = words[index] + "en"  # If it doesn't, add "en" as a suffix to the word
        print(new_word)

# Test the function with different sentences and indices
adjective_to_verb("I need to make that bright.", -1)  # Should print "brighten"
adjective_to_verb("It got dark as the sun set.", 2)  # Should print "darken"