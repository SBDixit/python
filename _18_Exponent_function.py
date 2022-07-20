
def raise_base_pow(base_num,power_num):
    result = 1 
    for index in range (power_num):
        result = result * base_num
    return result

print("Power the of a given number : " + str(raise_base_pow(5,4)))