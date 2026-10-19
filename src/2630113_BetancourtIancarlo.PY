# COVER PAGE
# Name: Iancarlo Betancourt Rodriguez
# Student ID: 2630113
# Group: IM 1-2

# EXECUTIVE SUMMARY
# int is for whole numbers (age, hours) and float is for numbers with decimals
# (salary, temperature, bmi). The difference is that int has no decimal part.
# A boolean is a value that is only True or False. We get it from comparisons
# like >, <, >=, <=, == and !=, and we can join them with and, or, not.
# It is important to validate ranges and avoid dividing by zero because if not
# the program gives wrong results or crashes.
# This file has 6 problems. Each one has a description, inputs, outputs,
# validations and test cases, and uses int, float and bool to make decisions.

# GOOD PRACTICES
# - Use int for counters and float for numbers with decimals.
# - Save intermediate results in variables so I do not repeat operations.
# - Validate the data before doing operations (no negative hours or salary).
# - Use clear variable names and clear messages for the user.
# - True means the condition is met and False means it is not.

# Constants
HIGH_TEMPERATURE_C = 30.0
KELVIN_OFFSET = 273.15
REGULAR_HOURS_LIMIT = 40
OVERTIME_MULTIPLIER = 1.5
DISCOUNT_MIN_PURCHASE = 1000.0
LOAN_MIN_INCOME = 8000.0
LOAN_MAX_DEBT_RATIO = 0.4
LOAN_MIN_CREDIT_SCORE = 650

# Note about validation: the input is a string, so first I check that it only
# has digits (and one "." if it is a float) with isdigit(). If it starts with
# "-" I remove it with [1:] to check the rest. Then I use float() or int().


# Problem 1: Temperature converter and range flag
# Description: Converts Celsius to Fahrenheit and Kelvin. is_high_temperature
# is true if temp_c is 30.0 or more.
# Inputs: temp_c (float)
# Outputs: Fahrenheit, Kelvin and High temperature (true/false)
# Validations: temp_c must be a number and Kelvin cannot be less than 0.
# Test cases:
# 1) Normal: temp_c = 35 -> Fahrenheit: 95.0, Kelvin: 308.15, High: true
# 2) Border: temp_c = 30 -> Fahrenheit: 86.0, Kelvin: 303.15, High: true
# 3) Error: temp_c = abc (or -300) -> Error: invalid input
print("Problem 1")
temp_text = input("Enter temperature in Celsius: ").strip()
temp_digits = temp_text
if temp_text.startswith("-"):
    temp_digits = temp_text[1:]

if temp_digits.replace(".", "", 1).isdigit():
    temp_c = float(temp_text)
    temp_k = temp_c + KELVIN_OFFSET
    if temp_k < 0:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= HIGH_TEMPERATURE_C
        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        if is_high_temperature:
            print("High temperature: true")
        else:
            print("High temperature: false")
else:
    print("Error: invalid input")
print()


# Problem 2: Work hours and overtime payment
# Description: Calculates the weekly pay. Up to 40 hours are paid normal and
# the extra hours are paid 150%. has_overtime is true if hours_worked > 40.
# Inputs: hours_worked (float), hourly_rate (float)
# Outputs: Regular pay, Overtime pay, Total pay and Has overtime (true/false)
# Validations: hours_worked >= 0 and hourly_rate > 0
# Test cases:
# 1) Normal: 45 hours, rate 100 -> Regular: 4000.0, Overtime: 750.0,
#    Total: 4750.0, Has overtime: true
# 2) Border: 40 hours, rate 100 -> Regular: 4000.0, Overtime: 0.0,
#    Total: 4000.0, Has overtime: false
# 3) Error: -5 hours, rate 100 -> Error: invalid input
print("Problem 2")
hours_text = input("Enter hours worked: ").strip()
rate_text = input("Enter hourly rate: ").strip()

# a negative number is not valid here, so the minus sign is not accepted
if hours_text.replace(".", "", 1).isdigit() and rate_text.replace(".", "", 1).isdigit():
    hours_worked = float(hours_text)
    hourly_rate = float(rate_text)
    if hourly_rate > 0:
        regular_hours = min(hours_worked, REGULAR_HOURS_LIMIT)
        overtime_hours = max(hours_worked - REGULAR_HOURS_LIMIT, 0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > REGULAR_HOURS_LIMIT
        print("Regular pay:", round(regular_pay, 2))
        print("Overtime pay:", round(overtime_pay, 2))
        print("Total pay:", round(total_pay, 2))
        if has_overtime:
            print("Has overtime: true")
        else:
            print("Has overtime: false")
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")


# Problem 3: Discount eligibility with booleans
# Description: The customer gets a 10% discount if is_student or is_senior is
# true, or if purchase_total is 1000.0 or more.
# Inputs: purchase_total (float), is_student_text (YES/NO),
# is_senior_text (YES/NO)
# Outputs: Discount eligible (true/false) and Final total
# Validations: purchase_total >= 0 and the texts must be YES or NO
# Test cases:
# 1) Normal: 500, yes, no -> Discount eligible: true, Final total: 450.0
# 2) Border: 1000, NO, NO -> Discount eligible: true, Final total: 900.0
#    Border: 999.99, NO, NO -> Discount eligible: false, Final total: 999.99
# 3) Error: 200, maybe, NO -> Error: invalid input
print("Problem 3")
purchase_text = input("Enter purchase total: ").strip()
is_student_text = input("Is the customer a student? (YES/NO): ").strip().upper()
is_senior_text = input("Is the customer a senior? (YES/NO): ").strip().upper()

# a negative number is not valid here, so the minus sign is not accepted
if purchase_text.replace(".", "", 1).isdigit():
    purchase_total = float(purchase_text)
    student_ok = is_student_text == "YES" or is_student_text == "NO"
    senior_ok = is_senior_text == "YES" or is_senior_text == "NO"
    if student_ok and senior_ok:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"
        discount_eligible = is_student or is_senior or purchase_total >= DISCOUNT_MIN_PURCHASE
        if discount_eligible:
            final_total = purchase_total * 0.9
            print("Discount eligible: true")
        else:
            final_total = purchase_total
            print("Discount eligible: false")
        print("Final total:", round(final_total, 2))
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")


# Problem 4: Basic statistics of three integers
# Description: Reads 3 integers and shows the sum, average, max, min and
# all_even (true if the three numbers are even).
# Inputs: n1, n2, n3 (int)
# Outputs: Sum, Average, Max, Min and All even (true/false)
# Validations: the three values must be integers (negatives are allowed)
# Test cases:
# 1) Normal: 4, 6, 8 -> Sum: 18, Average: 6.0, Max: 8, Min: 4, All even: true
# 2) Border: -3, 2, 4 -> Sum: 3, Average: 1.0, Max: 4, Min: -3, All even: false
# 3) Error: 5, x, 7 -> Error: invalid input
print("Problem 4")
n1_text = input("Enter first integer: ").strip()
n2_text = input("Enter second integer: ").strip()
n3_text = input("Enter third integer: ").strip()

n1_digits = n1_text
if n1_text.startswith("-"):
    n1_digits = n1_text[1:]
n2_digits = n2_text
if n2_text.startswith("-"):
    n2_digits = n2_text[1:]
n3_digits = n3_text
if n3_text.startswith("-"):
    n3_digits = n3_text[1:]

if n1_digits.isdigit() and n2_digits.isdigit() and n3_digits.isdigit():
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0
    print("Sum:", sum_value)
    print("Average:", round(average_value, 2))
    print("Max:", max_value)
    print("Min:", min_value)
    if all_even:
        print("All even: true")
    else:
        print("All even: false")
else:
    print("Error: invalid input")


# Problem 5: Loan eligibility (income and debt ratio)
# Description: A person is eligible if income >= 8000, debt_ratio <= 0.4 and
# credit_score >= 650. debt_ratio = monthly_debt / monthly_income.
# Inputs: monthly_income (float), monthly_debt (float), credit_score (int)
# Outputs: Debt ratio and Eligible (true/false)
# Validations: monthly_income > 0, monthly_debt >= 0, credit_score >= 0
# Test cases:
# 1) Normal: 10000, 3000, 700 -> Debt ratio: 0.3, Eligible: true
# 2) Border: 8000, 3200, 650 -> Debt ratio: 0.4, Eligible: true
# 3) Error: 0, 500, 700 -> Error: invalid input
print("Problem 5")
income_text = input("Enter monthly income: ").strip()
debt_text = input("Enter monthly debt payments: ").strip()
score_text = input("Enter credit score: ").strip()

# negative numbers are not valid here, so the minus sign is not accepted
if income_text.replace(".", "", 1).isdigit() and debt_text.replace(".", "", 1).isdigit() and score_text.isdigit():
    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(score_text)
    if monthly_income > 0:
        debt_ratio = monthly_debt / monthly_income
        eligible = monthly_income >= LOAN_MIN_INCOME and debt_ratio <= LOAN_MAX_DEBT_RATIO and credit_score >= LOAN_MIN_CREDIT_SCORE
        print("Debt ratio:", round(debt_ratio, 2))
        if eligible:
            print("Eligible: true")
        else:
            print("Eligible: false")
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")
print()


# Problem 6: Body Mass Index (BMI) and category flag
# Description: Calculates bmi = weight_kg / (height_m * height_m) and says if
# the person is underweight (< 18.5), normal (18.5 to 24.99) or
# overweight (>= 25.0).
# Inputs: weight_kg (float), height_m (float)
# Outputs: BMI, Underweight, Normal and Overweight (true/false)
# Validations: weight_kg > 0 and height_m > 0
# Test cases:
# 1) Normal: 70 kg, 1.75 m -> BMI: 22.86, Underweight: false, Normal: true,
#    Overweight: false
# 2) Border: 56.25 kg, 1.5 m -> BMI: 25.0, Underweight: false, Normal: false,
#    Overweight: true
# 3) Error: 70 kg, 0 m -> Error: invalid input
print("Problem 6")
weight_text = input("Enter weight in kg: ").strip()
height_text = input("Enter height in meters: ").strip()

# negative numbers are not valid here, so the minus sign is not accepted
if weight_text.replace(".", "", 1).isdigit() and height_text.replace(".", "", 1).isdigit():
    weight_kg = float(weight_text)
    height_m = float(height_text)
    if weight_kg > 0 and height_m > 0:
        bmi = weight_kg / (height_m * height_m)
        is_underweight = bmi < 18.5
        is_normal = bmi >= 18.5 and bmi < 25.0
        is_overweight = bmi >= 25.0
        print("BMI:", round(bmi, 2))
        if is_underweight:
            print("Underweight: true")
        else:
            print("Underweight: false")
        if is_normal:
            print("Normal: true")
        else:
            print("Normal: false")
        if is_overweight:
            print("Overweight: true")
        else:
            print("Overweight: false")
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")


# CONCLUSIONS
# I learned that int and float can be used together in real calculations, for
# example credit_score is an int and income is a float. Comparisons give a
# boolean (True or False) and with that the program can decide what to do using
# if. It is important to validate the data and avoid dividing by zero so the
# program does not crash. I also learned that "or" is easier to meet (discount)
# and "and" is stricter (loan). These patterns are used in payroll, discounts
# and loans.

# REFERENCES
# 1) Python documentation - Numeric Types (int, float):
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Python documentation - Boolean Type (bool):
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 3) Python Tutorial - An Informal Introduction to Python:
#    https://docs.python.org/3/tutorial/introduction.html
# 4) Python Tutorial - More Control Flow Tools (if statements):
#    https://docs.python.org/3/tutorial/controlflow.html
# 5) Python Tutorial - Floating-Point Arithmetic:
#    https://docs.python.org/3/tutorial/floatingpoint.html