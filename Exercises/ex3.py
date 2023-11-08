def ex3():
    list = input("Enter a list of numbers: ").split(",")

    if list[0] == list[len(list)-1]:
        print("True")
        return True
    print("False")
    return False
    
if __name__ == '__main__':
    ex3()