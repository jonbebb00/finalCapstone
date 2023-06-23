# finalCapstone

This README provides an overview and instructions for using the code contained in the associated file. The file includes four functions that perform various word manipulations: add_prefix_un, make_word_groups, remove_suffix_ness, and adjective_to_verb. Each function is described below along with examples of how to use them.

Functions
add_prefix_un(word)
This function checks if a word already starts with "un". If it does, the word is printed as it is. If not, the function adds "un" as a prefix to the word and then prints the new word with the prefix.

Usage:

python
Copy code
add_prefix_un("happy")  # Should print "unhappy"
add_prefix_un("unhappy")  # Should print "unhappy" (already starts with "un")
add_prefix_un("manageable")  # Should print "unmanageable"
add_prefix_un("necessary")  # Should print "unnecessary"
make_word_groups(vocab_words: list)
This function takes a list of words and creates a modified list based on the following rule: each word in the new list starts with the first word from the input list. If a word in the input list already starts with the first word, it is included as is. Otherwise, the first word is concatenated with the current word. The modified words are then joined using " :: " as a separator and printed.

Usage:

python
Copy code
make_word_groups(['en', 'close', 'joy', 'lighten'])  # Should print "en :: enclosure :: enjoy :: enlightenment"
make_word_groups(['en', 'enclose', 'joy', 'enlighten'])  # Should print "en :: enclose :: enjoy :: enlighten"
make_word_groups(['pre', 'serve', 'dispose', 'position'])  # Should print "pre :: preserve :: predispose :: preposition"
make_word_groups(['auto', 'didactic', 'graph', 'mate'])  # Should print "auto :: autodidactic :: autograph :: automate"
make_word_groups(['inter', 'twine', 'connected', 'dependent'])  # Should print "inter :: intertwine :: interconnected :: interdependent"
remove_suffix_ness(word)
This function checks if a word ends with "ness". If it does, it further checks if the character at index -5 (5th from the end) is "i". If it is, the function removes "ness" and replaces "i" with "y". Otherwise, it simply removes "ness" without any changes. If the word doesn't end with "ness", it is printed as it is.

Usage:

python
Copy code
remove_suffix_ness("heaviness")  # Should print "heavy"
remove_suffix_ness("sadness")  # Should print "sad"
remove_suffix_ness("eager")  # Should print "eager" (no "ness" suffix)
adjective_to_verb(sentence, index)
This function takes a sentence and an index as input. It attempts to convert the index variable to an integer and then splits the sentence into a list of words. Punctuation characters are removed from each word in the list. The function then checks if the word at the given index ends with "en". If it does, the word is printed without the trailing period (if present). If not, "en" is added as a suffix to the word, and the new word is printed.

Usage:

python
Copy code
adjective_to_verb("I need to make that bright.", -1)  # Should print "brighten"
adjective_to_verb("It got dark



