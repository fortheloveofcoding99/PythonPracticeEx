
# #  display your details like name, age, address in three different lines.
#
# a = input("Name:")
# b = input("Age:")
# c = input("Address:")
#
# def print_details(x, y, z):
#     print("Name: {}\nAge: {}\nAddress: {}".format(x,y,z))
#
# print_details(a,b,c)

# # Python program to solve (x + y) * (x + y)
#
# a = int(input("Value x:"))
# b = int(input("Value y:"))
#
# def value_squared(a,b):
#   c = (a+b)*(a+b)
#   print("{}*{}+2*{}*{}+{}*{}={}".format(a,a,a,b,b,b,c))
#
# value_squared(a,b)

# distance between 2 points on a 2d graph

import math

a = [3,2]
b = [5,1]

c = math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
print(c)