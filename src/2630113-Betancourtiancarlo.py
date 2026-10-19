# COVER PAGE
# Name: <Your iancarlo betancourt rodriguez
# Student ID: 2630113
# Group: IM 1-2

# EXECUTIVE SUMMARY
# A list keeps many items in order and it can be changed. A tuple also keeps
# items in order, but it cannot be changed.
# Mutable means we can add, remove or change items (lists). Immutable means we
# cannot change it after creating it (tuples).
# To connect two pieces of data (for example a product name and its price) I
# use two lists where the data is in the same position. For example, the name
# at position 0 matches the price at position 0.
# This file has 6 problems. Each one has a description, inputs, outputs,
# validations and test cases. They use lists and tuples in practical examples
# like shopping lists, coordinates, catalogs, grades and contacts.

# GOOD PRACTICES
# - Use lists when you need to add or remove items often.
# - Use tuples for data that should not change, like coordinates.
# - When two lists go together, keep them in the same order and the same size.
# - Do not change a list while you are looping through it.
# - Use clear variable names and clear messages for the user.

# Constant
PASSING_GRADE = 70.0


# Problem 1: Shopping list basics (list operations)
# Description: Makes a list of products from a text separated by commas, adds a
# new product at the end, shows how many products there are and checks if a
# product is in the list.
# Decision: if the initial list ends up empty, it is an error.
# Inputs: initial_items_text (string), new_item (string), search_item (string)
# Outputs: Items list, Total items and Found item (true/false)
# Validations: the three texts cannot be empty and the list needs at least one
# product.
# Test cases:
# 1) Normal: "apple,banana,orange", "grape", "banana"
#    -> Items list: ['apple', 'banana', 'orange', 'grape'], Total items: 4,
#       Found item: true
# 2) Border: "apple", "pear", "kiwi"
#    -> Items list: ['apple', 'pear'], Total items: 2, Found item: false
# 3) Error: ",," (no products), "grape", "banana" -> Error: invalid input
print("Problem 1")
initial_items_text = input("Enter initial items separated by commas: ").strip()
new_item = input("Enter a new item: ").strip()
search_item = input("Enter an item to search: ").strip()

if initial_items_text != "" and new_item != "" and search_item != "":
    # add a comma at the end so the last product is also saved
    initial_items_text = initial_items_text + ","
    items_list = []
    current_item = ""
    for char in initial_items_text:
        if char == ",":
            clean_item = current_item.strip()
            if clean_item != "":
                items_list.append(clean_item)
            current_item = ""
        else:
            current_item = current_item + char

    if len(items_list) > 0:
        items_list.append(new_item)
        print("Items list:", items_list)
        print("Total items:", len(items_list))
        if search_item in items_list:
            print("Found item: true")
        else:
            print("Found item: false")
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")
print()


# Problem 2: Points and distances with tuples
# Description: Saves two 2D points in tuples, calculates the distance between
# them and makes a new tuple with the midpoint.
# Inputs: x1, y1, x2, y2 (float)
# Outputs: Point A, Point B, Distance and Midpoint
# Validations: the 4 inputs must be numbers (negatives and decimals are ok).
# Test cases:
# 1) Normal: (0, 0) and (3, 4) -> Point A: (0.0, 0.0), Point B: (3.0, 4.0),
#    Distance: 5.0, Midpoint: (1.5, 2.0)
# 2) Border: (2, 2) and (2, 2) -> Distance: 0.0, Midpoint: (2.0, 2.0)
# 3) Error: x1 = abc -> Error: invalid input
print("Problem 2")
x1_text = input("Enter x1: ").strip()
y1_text = input("Enter y1: ").strip()
x2_text = input("Enter x2: ").strip()
y2_text = input("Enter y2: ").strip()

# check each text letter by letter: only digits, one dot and one minus sign
# at the beginning are allowed
numbers_text = [x1_text, y1_text, x2_text, y2_text]
all_valid = True
for text in numbers_text:
    dots = 0
    minus_signs = 0
    digits = 0
    for char in text:
        if char == ".":
            dots += 1
        elif char == "-":
            minus_signs += 1
        elif char in "0123456789":
            digits += 1
        else:
            all_valid = False
    if dots > 1 or minus_signs > 1 or digits == 0:
        all_valid = False
    if minus_signs == 1 and text[0] != "-":
        all_valid = False

if all_valid:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)

    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)
else:
    print("Error: invalid input")
print()


# Problem 3: Product catalog with two lists
# Description: Has a list of product names and a list of prices (same order).
# Asks for a product name and a quantity and calculates the total if the
# product exists. The name is changed to lowercase so "Apple" and "apple" work
# the same.
# Inputs: product_name (string), quantity (int)
# Outputs: Unit price, Quantity and Total (or "Error: product not found")
# Validations: quantity must be an integer greater than 0, product_name cannot
# be empty and the product must be in the list of names.
# Test cases:
# 1) Normal: apple, 3 -> Unit price: 10.0, Quantity: 3, Total: 30.0
# 2) Border: banana, 1 -> Unit price: 5.5, Quantity: 1, Total: 5.5
# 3) Error: grape, 2 -> Error: product not found
#    Error: apple, 0 -> Error: invalid input
print("Problem 3")
product_names = ["apple", "banana", "orange", "milk"]
product_prices = [10.0, 5.5, 8.0, 22.0]

product_name = input("Enter product name: ").strip().lower()
quantity_text = input("Enter quantity: ").strip()

# quantity must have only digits
quantity_ok = quantity_text != ""
for char in quantity_text:
    if char not in "0123456789":
        quantity_ok = False

if product_name != "" and quantity_ok:
    quantity = int(quantity_text)
    if quantity > 0:
        # look for the product, position -1 means "not found"
        position = -1
        for i in range(len(product_names)):
            if product_names[i] == product_name:
                position = i

        if position != -1:
            unit_price = product_prices[position]
            total_price = unit_price * quantity
            print("Unit price:", unit_price)
            print("Quantity:", quantity)
            print("Total:", round(total_price, 2))
        else:
            print("Error: product not found")
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")
print()


# Problem 4: Student grades with lists
# Description: Has a list of student names and a list where each item is the
# list of grades of that student (same order). Calculates the average and says
# if the student passed (average >= 70.0) with the boolean is_passed. The name
# uses title() so "alice" and "Alice" work the same.
# Inputs: student_name (string)
# Outputs: Grades, Average and Passed (or "Error: student not found")
# Validations: student_name cannot be empty, the student must be in the list
# and the list of grades cannot be empty.
# Test cases:
# 1) Normal: Alice -> Grades: [90.0, 85.0, 100.0], Average: 91.67, Passed: true
# 2) Border: Bob -> Grades: [60.0, 70.0, 80.0], Average: 70.0, Passed: true
# 3) Error: Zoe -> Error: student not found
#    Error: Diana (empty list) -> Error: invalid input
print("Problem 4")
student_names = ["Alice", "Bob", "Carlos", "Diana"]
all_grades = [
    [90.0, 85.0, 100.0],
    [60.0, 70.0, 80.0],
    [50.0, 60.0, 65.0],
    [],
]

student_name = input("Enter student name: ").strip().title()

if student_name != "":
    # look for the student, position -1 means "not found"
    position = -1
    for i in range(len(student_names)):
        if student_names[i] == student_name:
            position = i

    if position != -1:
        grades_list = all_grades[position]
        if len(grades_list) > 0:
            total_grades = 0
            for grade in grades_list:
                total_grades = total_grades + grade
            average = total_grades / len(grades_list)
            is_passed = average >= PASSING_GRADE
            print("Grades:", grades_list)
            print("Average:", round(average, 2))
            if is_passed:
                print("Passed: true")
            else:
                print("Passed: false")
        else:
            print("Error: invalid input")
    else:
        print("Error: student not found")
else:
    print("Error: invalid input")
print()


# Problem 5: Word frequency counter (two lists)
# Description: Reads a sentence, changes it to lowercase, splits it into a list
# of words (each space ends a word) and counts how many times each word appears
# using a list of different words and a list of counts (same order). At the end
# it shows the most common word (if there is a tie, the first one is used).
# Decision: punctuation is not removed, so "hi," and "hi" count as different
# words.
# Inputs: sentence (string)
# Outputs: Words list, Frequencies and Most common word
# Validations: sentence cannot be empty and the list of words cannot be empty.
# Test cases:
# 1) Normal: "The cat and the dog"
#    -> Words list: ['the', 'cat', 'and', 'the', 'dog'],
#       Frequencies: the: 2, cat: 1, and: 1, dog: 1,
#       Most common word: the
# 2) Border: "Hello" -> Words list: ['hello'], Frequencies: hello: 1,
#    Most common word: hello
# 3) Error: "   " (only spaces) -> Error: invalid input
print("Problem 5")
sentence = input("Enter a sentence: ").strip()

if sentence != "":
    # add a space at the end so the last word is also saved
    clean_sentence = sentence.lower() + " "
    words_list = []
    current_word = ""
    for char in clean_sentence:
        if char == " ":
            if current_word != "":
                words_list.append(current_word)
            current_word = ""
        else:
            current_word = current_word + char

    # list of different words
    unique_words = []
    for word in words_list:
        if word not in unique_words:
            unique_words.append(word)

    # list with how many times each different word appears
    counts_list = []
    for unique_word in unique_words:
        count = 0
        for word in words_list:
            if word == unique_word:
                count += 1
        counts_list.append(count)

    most_common_word = ""
    max_count = 0
    for i in range(len(unique_words)):
        if counts_list[i] > max_count:
            max_count = counts_list[i]
            most_common_word = unique_words[i]

    print("Words list:", words_list)
    print("Frequencies:")
    for i in range(len(unique_words)):
        print(unique_words[i] + ":", counts_list[i])
    print("Most common word:", most_common_word)
else:
    print("Error: invalid input")
print()


# Problem 6: Simple contact book (two lists)
# Description: Has a list of contact names and a list of phones (same order).
# Asks for an action (ADD, SEARCH or DELETE) and does what it says. ADD saves
# the contact or updates the phone if the contact already exists.
# Inputs: action_text (string), name (string) and phone (string, only for ADD)
# Outputs: Contact saved, Phone, Contact deleted or "Error: contact not found"
# Validations: action_text must be ADD, SEARCH or DELETE (changed to
# uppercase), name cannot be empty and, for ADD, phone cannot be empty.
# Test cases:
# 1) Normal: SEARCH, Alice -> Phone: 1234567890
# 2) Border: ADD, Alice, 9998887777 -> Contact saved: Alice 9998887777
#    (Alice already existed, so her phone is updated)
# 3) Error: EDIT -> Error: invalid input
#    Error: SEARCH, Zoe -> Error: contact not found
print("Problem 6")
contact_names = ["Alice", "Bob", "Carlos"]
contact_phones = ["1234567890", "5551234567", "5559876543"]

action_text = input("Enter action (ADD, SEARCH or DELETE): ").strip().upper()

if action_text == "ADD" or action_text == "SEARCH" or action_text == "DELETE":
    name = input("Enter contact name: ").strip().title()
    if name != "":
        # look for the contact, position -1 means "not found"
        position = -1
        for i in range(len(contact_names)):
            if contact_names[i] == name:
                position = i

        if action_text == "ADD":
            phone = input("Enter phone number: ").strip()
            if phone != "":
                if position != -1:
                    contact_phones[position] = phone
                else:
                    contact_names.append(name)
                    contact_phones.append(phone)
                print("Contact saved:", name, phone)
            else:
                print("Error: invalid input")
        elif action_text == "SEARCH":
            if position != -1:
                print("Phone:", contact_phones[position])
            else:
                print("Error: contact not found")
        else:
            if position != -1:
                contact_names.pop(position)
                contact_phones.pop(position)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")


# CONCLUSIONS
# I learned that lists are used when I need to add or remove items, because they
# are flexible and can be changed. Tuples are good for data that should not
# change, like the coordinates of a point. When two pieces of data go together,
# like a name and a price, I can use two lists in the same order and find the
# position of one to get the other. I also saw that we need to validate that
# the item exists and that the list is not empty to avoid errors, and that the
# same loop pattern is used to search, count and add numbers.

# REFERENCES
# 1) Python documentation - Built-in Types: list, tuple:
#    https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# 2) Python Tutorial - Data Structures:
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) Python Tutorial - More Control Flow Tools (for statements and range):
#    https://docs.python.org/3/tutorial/controlflow.html
# 4) Python documentation - Text Sequence Type (str methods):
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 5) Python Tutorial - An Informal Introduction to Python:
#    https://docs.python.org/3/tutorial/introduction.html