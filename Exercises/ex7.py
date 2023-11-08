import random as rd
def ex7():
    

    while True:
        random = rd.randint(1, 100)

        if random < 10:
            print(f"{random}: You Lose.")
        elif random > 10 and random < 50:
            print(f"{random}: Try Again.")
        else:
            print(f"{random}: You Win!")


if __name__ == '__main__':
    ex7()