from helper import validate_and_execute

"""def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"

def validate_and_execute():
    try:
        user_input_value = int(days_and_unit_dictionary["days"])
        if user_input_value > 0:
            calculated_value = days_to_units(user_input_value, days_and_unit_dictionary["units"])
            print(calculated_value)
        elif user_input_value == 0:
            print("you entered a 0, please enter a positive number")
        else:
            print("you entered a negative number. there's no conversion for you")
    except ValueError:
        print("your entry is invalid. don't ruin my program")"""

user_input = ""
while user_input != "exit":
    user_input = input("hey user, please enter number of days and conversion unit\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "units": days_and_unit[1]}
    print(days_and_unit)
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute(days_and_unit_dictionary)
