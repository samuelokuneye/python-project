cal_to_units = 24
name_of_units = "hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * cal_to_units} {name_of_units}"
    elif num_of_days == 0:
        return "please enter a number greater than 0"
    else:
        return "please enter a valid positive number"

user_input = input("Hi user, enter the number od days and i'll convert to hours.\n")
def validate_and_execute():
    if user_input.isdigit():
        user_input_value = int(user_input)
        calculated_value = days_to_units(user_input_value) #calling the returned valu of the funtion as a variable
        print(calculated_value)
    else:
        print("enter a valid number. dont ruin my program")
validate_and_execute()