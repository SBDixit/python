import re


def max_num(no1,no2,no3):
    if no1>=no2 and no1>=no3:
       return no1 
    elif no2>=no1 and no2>=no3:
        return no2
    else:
        return no3

print("THE BIGGEST NUMBER AMONG THESE THREE IS : " + str( max_num(99,70,705)))