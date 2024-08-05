import datetime
name=input("What is your name?\n")
age=int(input("How old are you?\n"))
current_year=datetime.date.today().year
hundred_year=100-age+current_ year
print("Hello", name)
print("You will be 100 years old in the year", hundred_year)