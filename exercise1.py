import datetime
name=input("please input your name:")
year=input("please enter your birth year:")
year=int(year)
curr_date=datetime.date.today()
curr_year=curr_date.year
age=curr_year-year+1
print("your name is: " , name)
print("your age is : ", age)