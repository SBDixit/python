hidden_word = "ANT"
guess =" "
NO_counting = 0
NO_Chances = 3
out_of_guesses = False
print("HINT :: He/She is an insect , he/she can lift the weight 100time heavier his/her weight :")

while guess != hidden_word and not out_of_guesses:
    if NO_counting < NO_Chances:
        guess =input("Enter the guessing Word :: ")
        guess += 1
    else:
        
        out_of_guesses =True
if out_of_guesses :
    print("out_of_guesses , You lose the Game >><<")
else:
    print("YOU WON THE GAME *~*")
