# ce code contient une partie de roulette au casino

import random
from math import ceil

money = 1000
play = True

print("Welcome, let's play roulette")

while play:
    pick = -1

    while pick < 0 or pick > 49:
        pick = int(input("\nPick a number between 1 and 49 : "))
    
        if pick < 0 or pick > 49:
            print("I said between 0 and 49!! Try again")
        else:
            bet = int(input("How much do you want to bet? "))
    

    while bet > money:
        print("You don't have enough money")
        bet = int(input("How much do you want to bet this time? "))
    
    else:
        print("\nLet's spin the ball")

#la bille s'arrête sur un chiffre compris entre 1 et 49

    rand_numb = random.randrange(50)
    print("\nThe ball stopped on the", rand_numb)

#le jeu en lui même

    if pick == rand_numb:
        print("\nYou win", bet*3,"$")
        money += ceil(bet*3)
        print("\nYou have", money, "$ now.")

    elif rand_numb%2 == 0 and pick%2 == 0:
        print("\nYou were right betting black, you win", bet*0.5,"$")
        money += ceil(bet*0.5)
        print("\nYou have", money, "$ now.")
    
    elif rand_numb%2 != 0 and pick%2 != 0:
        print("\nYou were right betting red, you win", bet*0.5,"$")
        money += ceil(bet*0.5)
        print("\nYou have", money, "$ now.")

    else:
        print("\nYou lose!")
        money -= bet
        print("\nYou have", money, "$ now. ")

    if money <= 0:
        print("\nYou can't play anymore")

    leave = input("\nDo you wish to leave the casino with your money? (y/n) ")
    if leave == "y":
        print("\nSee you soon")
        play = False
    else:
        play = True

    

