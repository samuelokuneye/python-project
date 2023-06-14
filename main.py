cal_to_units = 24 * 60 *60
name_of_units = "seconds"

def days_to_units():
    print(f"20 days are {20 * cal_to_units} {name_of_units}")
    print("all is good")

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * cal_to_units} {name_of_units}")
    print("all is good")

days_to_units(30)
days_to_units(50)
days_to_units(70)
days_to_units(100)


def scope_check(num_of_days, custom_msg):
    print(f"{num_of_days} days are {num_of_days * cal_to_units} {name_of_units}")
    print(custom_msg)
scope_check(10, "I am happy")
scope_check(12, "awesome")

