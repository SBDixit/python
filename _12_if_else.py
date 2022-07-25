is_male = True
is_tall = False

if is_male and is_tall :
    print("you are a tall man .")
elif is_male and not (is_tall):
    print("You are a short man .")
elif not(is_male) and is_tall:
    print("You are not a male but a tall .")
else:
    print("You are niether male nor tall.")
