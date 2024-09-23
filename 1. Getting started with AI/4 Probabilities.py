import random

def main():

    randomNumber = random.random()
    favorite = ""
    if randomNumber < 0.8:
        favorite = "dogs"
    elif  randomNumber >= 0.8 and randomNumber < 0.9:
        favorite = "cats"
    else:
        favorite = "bats"

    print("I love " + favorite) 


main()