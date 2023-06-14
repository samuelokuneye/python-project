#this program obtains goal and its deadline as input from users
# and displays the remaining time  to the deadline (ttd) to them
from datetime import datetime

user_input = input("dear user, please enter your goal and the deadline separated by colon\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]
deadline_time = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
ttd = deadline_time - today_date
print(f"dear user, the time till deadline for your goal; {goal} is {ttd} days")

print(f"dear user, the remaining days to your goal; {goal} is {ttd.days} days") #convert to days
ttd_hour = int(ttd.total_seconds()/60/60) #convert to hours
print(f"dear user, the remaining time to your goal; {goal} is {ttd_hour} hours")