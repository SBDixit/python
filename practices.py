
# # Q 1.  Python program to interchange first and last elements in a list.

# def first_last_list(new_list):   

#     new_list [0], new_list[-1] = new_list[-1],new_list[0]
#     return new_list

# new_list = [12,13,15,6,34,86]
# print(first_last_list(new_list))


# #Q 2 .Python program to swap two elements in a list

# def swap(element,post_1,post_2):
#     element[post_1],element[post_2]=element[post_2],element[post_1]
#     return  element

# element =[12,18,14,16,45,65]

# post_1 = input("Enter the POSITION_1: ")
# post_2 = input("Enter the POSITION_2: ")
# print("After swaping the elements of List : " + swap(element,str(post_1,post_2)))

# Q 3. Ways to find length of list

# element =[12,18,14,16,45,65]
# print("THE LENGTH OF THE LIST IS : "+ str(len(element)))


#Q 4. Maximum and Minimum of two numbers in Python


#def max_num(num_1,num_2):
#     if num_1 >= num_2:
#         return num_1
#     else:
#         return num_2
    
# num_1 = input("Enter num1 : ")
# num_2 =input("Enter num_2 : ")
# print("MAXIMUM NUMBER AMONG THESE TWO NUMBER IS: "+str(max_num(num_1,num_2)))

# def min_num(no1,no2):
#     if no1 <= no2:
#         return no1
#     else:
#         return no2
    
# no1 = input("Enter num1 : ")
# no2 =input("Enter num_2 : ")
# print("MINIMUM NUMBER AMONG THESE TWO NUMBER IS: "+str(min_num(no1,no2)))


# Q5.. Ways to check if element exists in list and find the element occurences also .

# list = ["abc","bca","mca","bca","bba","mba"]
# Finding_Element = input("Enter the finding element : ")

# if   Finding_Element in list and  list.count(Finding_Element):
#     print("YES it exists "+ str(list.count(Finding_Element)))
# else:
#     print("NO, the lists don't having that.")

# find sum and average of List in Python

sum_list = [45,12,36,48,12,18,24,56,34]






