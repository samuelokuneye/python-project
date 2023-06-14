from user import User

user_one = User("samuel okuneye", "sam@sam.com", "DevSecOps Engineer","admin123")
user_two = User("demola neye", "dem@sam.com", "DevOps Engineer","admin1234567")

user_one.change_job("SRE")
user_one.get_user_info()
user_two.get_user_info()