## Exercise 1: Practicing print with tabs and new lines.
# print("Twinkle, twinkle little star.\n\tHow I wonder what you are.\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.")

# ## Exercise 2: Practicting importing a module
# import sys
# print("Python version")
# print(sys.version)
# print("Version info.")
# print (sys.version_info)

# ## Exercise 3: Practicing modules and variables.
# import datetime
# now = datetime.datetime.now()
# print("The current date and time: ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# ## Exercise 4: Practicing importina  module and using maths.
# from math import pi
# r = float(input ("Input the radius of the circle: "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r **2))

# ## Exercise 5: Practicing variables and print.
# fname = input("What is your first name? ")
# lname = input("What is your last name? ")
# print("Welcome to the Matrix, " + lname, fname)

# ## Exercise 6: Practicing accepting a sequence of comma-sep'd numbers from user and generate a list and tuple with those #.
# values = input("Input some comma separated numbers: ")
# list = values.split(",")
# tuple = tuple(list)
# print('List: ', list)
# print('Tuple: ', tuple)

# ## Offshoot Exercise: Tinkering with csv
# import csv
# with open('numbers.csv', newline='') as csvfile:
#     numread = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in numread:
#         print(', '.join(row))


## Exercise 7: Playing around with time, split.
# repr() fnction returns a printable representation of the given object.

# import time
#
# filename = input("Please input the name of your filename: ")
# file_ext = filename.split(".")
# print("The file extension is: " + repr(file_ext[-1]))

# ## Exercise 8: printing first and last colors from a list. Lists.
# color_list = [
#     "Red",
#     "Green",
#     "White",
#     "Black"
# ]
#
# print("The first color is " + color_list[0], "and the last color is " + color_list[-1])


# ## Exercise 9: Display examination schedule, extracting from exam_st_date.
#
# exam_st_date = (11, 12, 2014)
# print("The exam will take place on: %i/%i/%i"%exam_st_date)
# # Note to self, play around with datetime and what I can do with it.
