#friends = ["kevin","jhon","Karen","Mike","Jim"]
#print(friends)

# modification :
#finding friends with index 
#Index_friends = ["kevin","jhon","Karen","Mike","Jim"]
#print(friends[2])


                          
# ------------------------ LISTS FUNCTIONS -------------------------
lucky_number = [4,8,10,54,6,9,0]
friends = ["kevin","jim","karen","oscar","mota","jim"]

print(friends.extend(lucky_number))

friends.insert(2,"BABLU")
print("INSERTING THE LIST ELEMENTS BY THERE INDEX : " + friends)
print("      ")

friends.append("creed")
print("APPENDING THE ELEMENT IN THE LIST : " + friends)
print("      ")

friends.remove("mota")
print("REMOVING THE ELEMENT FROM THE LIST : " + friends)
print("      ")

friends.clear(friends)
print("CLEARING THE LIST : " + friends)
print("      ")

friends.pop(friends)
print("POPING THE LAST ELEMENT OF THE LIST : " + friends)
print("      ")

print("COUNTING THE MULTI ELEMENT IN THE LIST : " + friends.count("jim"))
print("      ")

print("FINDING THE ELEMENT OF THE LIST : " + friends.index("kevin"))
print("      ")

lucky_number.sort()
print("ARRANGING THE LIST OF ELEMENT IN INCREASING ORDER OF THE LIST : " + lucky_number)
print("      ")

lucky_number.reverse
print("REVERSE PRINT OF THE ELEMENTS OF THE LIST : " +lucky_number)
print("      ")

friends2 = friends.copy()
print("COPYING THE FRIENDS ELEMENT TO FRIENDS2 : "+ friends2)