def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"

def validate_and_execute(days_and_unit_dictionary):
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
        print("your entry is invalid. don't ruin my program")