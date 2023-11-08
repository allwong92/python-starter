def ex13():

    while True:
        first_int = input("Enter first integer: ")

        if first_int == 'exit':
            break

        second_int = input("Enter second integer: ")

        if second_int == 'exit':
            break

        try:
            
            first_int = int(first_int)
            second_int = int(second_int)

            print(f"Answer: {(first_int + second_int)}")

        except:
            print("You've reached an exception. ")


if __name__ == '__main__':
    ex13()