# COVER PAGE
# Name: iancarlo betancourt rodriguez
# Student ID: 2630113
# Group: IM 1-2

# EXECUTIVE SUMMARY
# A string is a data type that stores text (letters, numbers and symbols between
# quotes). Strings are immutable: we cannot change a letter inside a string, any
# change makes a new string.
# With strings we can join them (+), get their length (len), take parts of them
# (slicing), search with "in", and change them with methods like strip(),
# lower(), upper() and title().
# It is important to clean the text the user types (remove extra spaces, use the
# same case) because people write in many different ways, and if we do not
# clean it the comparisons fail and we get bad data.
# This file has 6 problems. Each one has a description, inputs, outputs,
# validations and test cases, and uses strings to format names, validate
# emails, check palindromes, count words, classify passwords and make labels.

# GOOD PRACTICES
# - Strings are immutable: every change makes a new string.
# - Clean the input with strip() and lower() before comparing it.
# - Use constants instead of magic numbers.
# - Validate in order: first that it is not empty, then the format.
# - Use clear variable names and clear error messages.

# Constants
MIN_NAME_WORDS = 2
MIN_PHRASE_LENGTH = 3
MIN_PASSWORD_LENGTH = 8
LABEL_LENGTH = 30


# Problem 1: Full name formatter (name + initials)
# Description: Cleans a full name, shows it in Title Case and shows the
# initials, like J.C.T.
# Inputs: full_name (string)
# Outputs: Formatted name and Initials
# Validations: full_name cannot be empty after strip() and must have at least
# two words. Extra spaces between the words are ignored.
# Test cases:
# 1) Normal: "juan carlos tovar" -> Formatted name: Juan Carlos Tovar,
#    Initials: J.C.T.
# 2) Border: "  ANA   lopez " -> Formatted name: Ana Lopez, Initials: A.L.
# 3) Error: "Madonna" (only one word) -> Error: invalid input
#    Error: "   " (only spaces) -> Error: invalid input
print("Problem 1")
full_name = input("Enter your full name: ").strip()

if full_name != "":
    # separate the words: every space ends a word
    # (I add a space at the end so the last word is also saved)
    words_list = []
    current_word = ""
    for char in full_name + " ":
        if char == " ":
            if current_word != "":
                words_list.append(current_word)
            current_word = ""
        else:
            current_word = current_word + char

    if len(words_list) >= MIN_NAME_WORDS:
        formatted_words = []
        initials = ""
        for word in words_list:
            formatted_words.append(word.title())
            initials = initials + word[0].upper() + "."
        print("Formatted name:", " ".join(formatted_words))
        print("Initials:", initials)
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")
print()


# Problem 2: Simple email validator (structure + domain)
# Description: Checks if an email has a basic correct format: exactly one "@",
# at least one "." after the "@" and no spaces. If it is valid, it also shows
# the domain (the part after the "@").
# Inputs: email_text (string)
# Outputs: Valid email (true/false) and Domain (only if it is valid)
# Validations: email_text cannot be empty after strip().
# Test cases:
# 1) Normal: "student@upv.edu.mx" -> Valid email: true, Domain: upv.edu.mx
# 2) Border: "a@b.c" -> Valid email: true, Domain: b.c
#    Border: "name@domain" (no dot after the @) -> Valid email: false
#    Border: "user@@mail.com" (two @) -> Valid email: false
# 3) Error: "   " (only spaces) -> Error: invalid input
print("Problem 2")
email_text = input("Enter an email: ").strip()

if email_text != "":
    # count the @ and save everything that comes after the @ in domain_part
    at_count = 0
    domain_part = ""
    for char in email_text:
        if char == "@":
            at_count += 1
        elif at_count >= 1:
            domain_part = domain_part + char

    is_valid_email = at_count == 1 and "." in domain_part and " " not in email_text

    if is_valid_email:
        print("Valid email: true")
        print("Domain:", domain_part)
    else:
        print("Valid email: false")
else:
    print("Error: invalid input")
print()


# Problem 3: Palindrome checker (ignoring spaces and case)
# Description: Checks if a phrase reads the same from left to right and from
# right to left, ignoring spaces and upper or lower case. It makes a list of
# the letters, copies it, reverses the copy and compares both lists.
# Inputs: phrase (string)
# Outputs: Normalized phrase and Is palindrome (true/false)
# Validations: phrase cannot be empty after strip() and it needs at least 3
# letters after removing the spaces.
# Test cases:
# 1) Normal: "Anita lava la tina" -> Normalized phrase: anitalavalatina,
#    Is palindrome: true
# 2) Border: "aba" (the shortest valid phrase) -> Is palindrome: true
#    Border: "Hola mundo" -> Normalized phrase: holamundo,
#    Is palindrome: false
# 3) Error: "ab" (less than 3 letters) -> Error: invalid input
#    Error: "   " (only spaces) -> Error: invalid input
print("Problem 3")
phrase = input("Enter a phrase: ").strip()

if phrase != "":
    # lowercase and without spaces
    normalized_phrase = ""
    for char in phrase.lower():
        if char != " ":
            normalized_phrase = normalized_phrase + char

    if len(normalized_phrase) >= MIN_PHRASE_LENGTH:
        letters_list = list(normalized_phrase)
        reversed_list = letters_list.copy()
        reversed_list.reverse()

        print("Normalized phrase:", normalized_phrase)
        if letters_list == reversed_list:
            print("Is palindrome: true")
        else:
            print("Is palindrome: false")
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")
print()


# Problem 4: Sentence word stats (lengths and first/last word)
# Description: Separates the words of a sentence and shows the number of words,
# the first word, the last word, the shortest word and the longest word. If two
# words have the same length, the first one is used.
# Inputs: sentence (string)
# Outputs: Word count, First word, Last word, Shortest word and Longest word
# Validations: sentence cannot be empty after strip().
# Test cases:
# 1) Normal: "The quick brown fox jumps" -> Word count: 5, First word: The,
#    Last word: jumps, Shortest word: The, Longest word: quick
# 2) Border: "Hello" (only one word) -> Word count: 1, First word: Hello,
#    Last word: Hello, Shortest word: Hello, Longest word: Hello
# 3) Error: "   " (only spaces) -> Error: invalid input
print("Problem 4")
sentence = input("Enter a sentence: ").strip()

if sentence != "":
    # separate the words (same idea as Problem 1)
    words_list = []
    current_word = ""
    for char in sentence + " ":
        if char == " ":
            if current_word != "":
                words_list.append(current_word)
            current_word = ""
        else:
            current_word = current_word + char

    first_word = words_list[0]
    last_word = words_list[len(words_list) - 1]
    shortest_word = words_list[0]
    longest_word = words_list[0]
    for word in words_list:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    print("Word count:", len(words_list))
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)
else:
    print("Error: invalid input")
print()


# Problem 5: Password strength classifier
# Description: Classifies a password as weak, medium or strong. The rules I
# used are:
# - weak: less than 8 characters.
# - strong: 8 or more characters and it has an uppercase letter, a lowercase
#   letter, a digit and a symbol (anything that is not a letter or a digit).
# - medium: 8 or more characters but it is missing at least one of those 4.
# Inputs: password_input (string)
# Outputs: Password strength (weak, medium or strong)
# Validations: the password cannot be empty (I check it with strip(), but I do
# not change the password because spaces can be part of it).
# Test cases:
# 1) Normal: "Abcdef1!" -> Password strength: strong
# 2) Border: "Abcdefg1" (8 characters, no symbol) -> Password strength: medium
#    Border: "Abcdef1" (only 7 characters) -> Password strength: weak
# 3) Error: "" (empty) -> Error: invalid input
print("Problem 5")
password_input = input("Enter a password: ")

if password_input.strip() != "":
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    for char in password_input:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            has_upper = True
        elif char in "abcdefghijklmnopqrstuvwxyz":
            has_lower = True
        elif char in "0123456789":
            has_digit = True
        else:
            has_symbol = True

    if len(password_input) < MIN_PASSWORD_LENGTH:
        print("Password strength: weak")
    elif has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    else:
        print("Password strength: medium")
else:
    print("Error: invalid input")
print()


# Problem 6: Product label formatter (fixed-width text)
# Description: Makes a one-line label with the format
# "Product: <NAME> | Price: $<PRICE>" that has exactly 30 characters. If it is
# shorter, spaces are added at the end. If it is longer, it is cut at 30.
# Decision: to keep it simple, the price must be a whole number (no decimals).
# Inputs: product_name (string), price_text (whole number)
# Outputs: Label (between quotes so the spaces can be seen)
# Validations: product_name cannot be empty after strip() and the price must be
# a whole number greater than 0.
# Test cases:
# 1) Normal: "Milk", 22 -> Label: "Product: Milk | Price: $22    "
#    (26 characters + 4 spaces)
# 2) Border: "Chocolate bar", 5 -> Label: "Product: Chocolate bar | Price"
#    (the label was longer than 30, so it is cut)
# 3) Error: "Milk", abc -> Error: invalid input
#    Error: "Milk", 0 -> Error: invalid input
print("Problem 6")
product_name = input("Enter product name: ").strip()
price_text = input("Enter price (whole number): ").strip()

# the price is valid if it is not empty and every character is a digit
price_ok = price_text != ""
for char in price_text:
    if char not in "0123456789":
        price_ok = False

if product_name != "" and price_ok:
    price_value = int(price_text)
    if price_value > 0:
        label = f"Product: {product_name} | Price: ${price_value}"
        # cut the label to 30 characters (if it was longer)
        label = label[:LABEL_LENGTH]
        # add spaces at the end until it has 30 characters
        for i in range(LABEL_LENGTH - len(label)):
            label = label + " "
        print(f'Label: "{label}"')
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")


# CONCLUSIONS
# I learned that strings are very important because all the data the user types
# arrives as text. Methods like strip(), lower() and title() help to clean the
# text before comparing it, and slicing helps to take only the part we need,
# like the first 30 characters of a label. Strings are immutable, so every
# change makes a new string and we have to save it in a variable. I also learned
# that it is better to validate first that the text is not empty and then check
# its format, so we avoid errors and bad data. Loops are useful to go through a
# string letter by letter.

# REFERENCES
# 1) Python documentation - Built-in Types: Text Sequence Type (str):
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python documentation - String Methods:
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Python Tutorial - An Informal Introduction to Python (strings):
#    https://docs.python.org/3/tutorial/introduction.html
# 4) Python Tutorial - More Control Flow Tools (for statements and range):
#    https://docs.python.org/3/tutorial/controlflow.html
# 5) Python Tutorial - Input and Output (formatted string literals):
#    https://docs.python.org/3/tutorial/inputoutput.html.python.org/3/tutorial/inputoutput.html