import random
print("Guess a number from 1 to 100")


def game():
    random_number = random.randrange(1, 100)
    int_rand = int(random_number)
    guess_count = 0
    while 1 < 100:
        typed_number = int(input("Type your number here: "))
        guess_count = guess_count+1
        if int_rand == typed_number:
            print("Congrats you did it in ", guess_count, " tries!!!")
            break
        else:
            if int_rand > typed_number:
                print("Uh oh, To Low")
            else:
                if int_rand < typed_number:
                    print("Uh oh, To High")


game()
