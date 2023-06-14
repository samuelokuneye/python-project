cal_to_units = 24
name_of_units = "hours"
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * cal_to_units} {name_of_units}"
def validate_and_execute():
    try:
        user_input_value = int(number_of_days_element)
        if user_input_value > 0:
            calculated_value = days_to_units(user_input_value) #calling the returned valu of the funtion as a variable
            print(calculated_value)
        elif user_input_value == 0:
            print("please enter a number greater than 0")
    except ValueError:
        print("enter a valid number. dont ruin my program")
user_input = ""
while user_input != "exit":
    user_input = input("Hi user, enter the number of days as list of integers and i'll convert to hours.\n")
    #print(type(user_input.split()))
    #print(user_input)
    for number_of_days_element in user_input.split():
        validate_and_execute()

# enter the input value as 3 6 23 59
# to use ',', then define custom separator in user_input.split(","):