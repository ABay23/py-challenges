
# Write a program that uses a print function to say 'hello world' as shown in 'Desired Output'.
# the code below almost works
# prinq("hello world")
# print("hello world")

print("Hey thanks for reviewing my code!")

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly.

def user_for_h():
    h = input("Enter your hours: ")
    rate = input("Enter your hourly Rate: ")
    hflo = float(h)
    h_rate = float(rate)
    #Baseline Hours 40
    if hflo - 40 <= 0:
        ot = 0
        gross = hflo * h_rate
    else:
        ot = hflo - 40
        ot_rate = h_rate * 1.5
        gross = (40 * h_rate) + (ot * ot_rate)
    return gross

# print(user_for_h())
def score_calc():
    s = input("Enter Score: ")
    try:
        score = float(s)
        if score > 1:
            raise ValueError("Score must be lower than 1!")
    except ValueError:
        print('Score must be lower than 1!')
        return
        
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('C')
    else:
        print('F')

# score_calc()

# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
# Do not name your variable sum or use the sum() function.

def computepay(h, r):
    if h - 40 <= 0:
        ot = 0
        gross = h * r
    else:
        ot = h - 40
        ot_rate = r * 1.5
        gross = (40 * r) + (ot * ot_rate)
    return gross

h = input("Enter your hours: ")
rate = input("Enter your hourly Rate: ")
hflo = float(h)
h_rate = float(rate)
# Baseline Hours 40
print("Pay", computepay(hflo, h_rate))

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except 
# and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

def prompt_one():
    min_num = None
    max_num = 0
    while True:
        user_i = input('Enter a number: ')
        if user_i == 'done':
            break
        try:
            num_x = int(user_i)
        except:
            print('Invalid Input')
            continue
        if min_num == None:
            min_num = num_x
        min_num = min(min_num, num_x)
        max_num = max(max_num, num_x)
    print('Maximum is ', max_num)
    print('Minimum is ', min_num)
        
prompt_one()
