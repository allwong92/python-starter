import random as rd
def ex1():
    sum = 0
    result = []

    
    for x in range(10):
        random_number = rd.randint(0,100)
        sum += random_number
        result.append(random_number)
        
    print(f"Sum is: {sum}")
    print(result)


if __name__ == '__main__':
    ex1()