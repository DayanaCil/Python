# get the below as output
# 1
# #     "Hi there 'banofee'
# # I want you so much  now \:-\
# # "
print(f"\t \"Hi there \'banofee\' \n I want you so much now \\:-\\ \n \" ")
# 2
# # Take an input of name from the user and print the name as below
# # "Hi name,your reverse is eman,1st letter is n and last letter is e,lenght of your name is 4"
username= input("what is your name?")
print(f" \"Hi {username}, your reverse is {username[::-1]} 1st letter is {username[0]} and last "
      f"letter is {username[-1]}, length of your name is {len(username)} ")


# 3.
# #Explain with print in your own words how is strings immutable and how u prove it.
name= "KiranDayana"
name.replace('K', 'D')
print(f"{name.replace('K', 'D')}")
# 4
# ask for users year of birth and print their age

birthdate =int(input("what is your year of birth?"))
print(f"My age is {2020-(birthdate)}")

