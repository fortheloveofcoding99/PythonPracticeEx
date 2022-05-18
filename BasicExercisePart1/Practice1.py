
# List1 = input("Numbers in CSV : ").split(",")
#
# foramtted_list = list(List1)
#
# print(foramtted_list)

#Enter the characters and concatenate into a string

# List2 = input("Enter characters in CSV :").split(",")
#
# formatted_list = list(List2)
#
# def concat_string(formatted_list):
#     string1 = ""
#
#     for i in formatted_list:
#         string1 = string1+i
#     print(string1)
#
# concat_string(formatted_list)

# #print even numbers in a list break if the number is equal to a given number
# List1 = input("Numbers in CSV : ").split(",")
#
# foramtted_list = list(List1)
#
# stop_num = input("what Number:")
# def filter_list(listx, y):
#     for x in listx:
#         if x == y:
#             print(x)
#             break
#         else:
#             if int(x)%2==0:
#                 print(x)
#
# filter_list(foramtted_list, stop_num)

# #print the list of farben not present in another list

Col_list = input("farben:").split(",")
unique_cols = set(Col_list)

Col_list1 = input("farben:").split(",")
unique_cols1 = set(Col_list1)
for x in Col_list:
    if x not in Col_list1:
        print(x)

print(unique_cols1.intersection(unique_cols))


