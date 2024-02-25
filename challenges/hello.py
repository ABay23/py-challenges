
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

print(user_for_h())