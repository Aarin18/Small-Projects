name : str = input ("Hey typr your name: ")
# "s" + "t" = "st"
print(" Hello " + name + " welcome to my game! ")

should_we_play = input ( " Do you want to play? " ).lower() # this will be make it in to lower cases no metter whant the user types
# 1 < 2 #true 1 > 2 # False 1 >= 2 #false  1 <= 2 #false 1 != 2 #true

if should_we_play == "yes" or should_we_play == "y":
    print("We are gone play!")
    weapon = input(" Choice a wepon (sword/axe):").lower()

# elif should_we_play == "YES":
#     print("WE ARE GONNE PLAY!")

# elif should_we_play == "Yes":
#     print("WE ARE GONNE PLAY!")  this is also a good way to write this or make this project
    direction = input (" Do you want to go left or right ? (left/right)") .lower()
    if direction == "left":
        print("Okey we went left and fell fo a cliff , game over , try again")

    elif direction == "right":
        print("WE went right")
        choice = input ("Okay , you now see a bridge , do you want to swim under it or cross it ? (swim/cross)").lower()
        if choice == "swim" and weapon == "axe":
            print("You got eaten by an alligater , you die , the end!")
            if weapon == "axe":
                print("You killed the alligater but becouse of the boold lose you die , the end!! ")

        else:
            print("You found the gold and you won!!!")


    else:
        print(" Sorry not valid replay , you Die! ")    
else:
    print("We are NOT playing...")

# if should_we_play != "no":
#     print("We are NOT playing...")   is also currct if we dont want to use else statment