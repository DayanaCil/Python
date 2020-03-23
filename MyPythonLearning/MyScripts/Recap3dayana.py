# create a list

cookiedough = ["flour","sugar,eggs", "butter", "vanillapaste","chocolate"]
print(cookiedough)

# # copy a list
cookiedough = ["flour","sugar,eggs", "butter", "vanillapaste","chocolate"]
chocolatecookie= cookiedough.copy()
print(chocolatecookie)

# # create a 3 dimensional list
# # of family->person of family->name,age,hobbies->x,y,z,sex

familia =[[["dad Rabbit", 30, "hopping"],["mum rabbit", 25, "cooking"],["baby rabbit", 5, "playing"]], [["dad elle"],["mum elle"],["baby elle"]]]
father1=(familia)[0][0][0]
father2=(familia)[1][0][0]
mother1=(familia)[0][1][0]
mother2=(familia)[1][1]
baby1=(familia)[0][2][0]
baby2=(familia)[1][2]
father_age=(father1),(familia)[0][0][1]
print(father1)
print(mother1)
print(baby1)
print(father_age)

# # show the list methods - Addition-3 and removal-3

basket=[23,34,56,8]
basket.append(500)
print(basket)

basket.insert(2, 300)
print(basket)

basket.extend([1,2,2,3])
print(basket)

basket.pop(2)
print(basket)

basket.remove(500)
print(basket)

print(basket.index(56))

# to clear
# # print(basket.clear())

