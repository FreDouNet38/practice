import random

rand_numb = random.randint(1, 30)
user_answer = 0
tries = 5


print("\n\nYOU'RE PLAYING GUESS!\n\n\nI picked a number between 1 and 30 \n\nCan you guess which one? \n\nGive it a try\n")

    
while user_answer != rand_numb and tries > 0:

    user_answer = input()
    user_answer = int(user_answer)
    
    if user_answer < rand_numb:
        print("\nToo low!! Higher\n")

        tries -= 1
        print("You have", tries, "tries left.\n")

    elif user_answer > rand_numb:
        print("\nToo high! Lower\n")

        tries -= 1
        print("You have", tries, "tries left.\n")

    else:
        print("Congratulations!!! YOU WIN!!")

if tries == 0:
    print("YOU LOSE")
    
