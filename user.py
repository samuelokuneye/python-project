class User:
    def __init__(self, my_name, my_email, my_job, pwd):   #this is the constructor
        self.name = my_name
        self.email = my_email
        self.current_job_title = my_job
        self.password = pwd

    def change_password(self, new_pwd):
        self.password = new_pwd

    def change_job(self, new_job):
        self.current_job_title = new_job
    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title} in London.\n Do contact {self.name} on {self.email}")


user_one = User("samuel okuneye", "sam@sam.com", "DevSecOps Engineer","admin123")
user_two = User("demola neye", "dem@sam.com", "DevOps Engineer","admin1234567")
user_one.get_user_info()
user_two.get_user_info()
