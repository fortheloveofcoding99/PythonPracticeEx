# # # Write a Python program to list all files in a directory in Python.
# import os
#
# path = r'C:\Users\befor\PycharmProjects\pythonPracticeProject\BasicExercisePart1'
#
# for root, dirs, files in os.walk(path):
#     print(root)
#     print(dirs)
#     print(files)
#     for file in files:
#         print(file)
# # Write a Python program to print without newline or space.
# i = 0
# while (i<10):
#     print("*",end=' ')
#     i += 1
#
# for a in range(1,10):
#     print("$",end=" ")
#
# #  Write a Python program to determine profiling of Python programs.
# import cProfile
# import math
# import random
#
# letters_list = ["a","e","i","o","u"]
#
#
# def unlist(list1):
#     h = ''
#     word_list = []
#
#     while len(word_list) < math.factorial(len(list1)):
#         h = ''.join(random.sample(list1,len(list1)))
#         if h not in word_list:
#             word_list.append(h)
#     print(word_list)
#
#
# cProfile.run("unlist(letters_list)")

# align and concatenate 2 lists
#
# list1 = ["stuhl","wohnzimmer","schribtisch","Einzelzimmer"]
#
# list2 = ["tisch","badezimmer","kugelschriber","Doppelzommer"]
#
# print(zip(list1,list2))
#
# for l in list(zip(list1,list2)):
#     print(l)
#
#
# farben = ["rot","rosa","lila","blau"]
#
# dinge = ["Apfel","kleid","blumen","Meer"]
#
# print(dict(zip(farben,dinge)))

# Write a Python program to print to stderr.
# import sys
#
# a = '2'
# A = 2
#
# if type(a)==type(A):
#     print("same type")
# else:
#     sys.stderr.write("error\n")