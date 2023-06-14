cal_to_units = 24
name_of_units = "hours"
user_input = input("Hi user, enter the number od days and i'll convert to hours.\n")
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * cal_to_units} {name_of_units}"
def validate_and_execute():
    if user_input.isdigit():
        user_input_value = int(user_input)
        if user_input_value > 0:
            calculated_value = days_to_units(user_input_value) #calling the returned valu of the funtion as a variable
            print(calculated_value)
        elif user_input_value == 0:
            print("please enter a number greater than 0")
    else:
        print("enter a valid number. dont ruin my program")

validate_and_execute()