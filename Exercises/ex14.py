def ex14():
     while True:
        first_int = input("Enter first integer: ")

        if first_int == 'exit':
            break

        second_int = input("Enter second integer: ")

        if second_int == 'exit':
            break
        
        op = input("Enter Operation (add, sub, mul, div): ")
        try:
            first_int = float(first_int)
            second_int = float(second_int)    

            match op:
                case 'add':
                    print(f"Answer: {(first_int + second_int)}")
                case 'sub':
                    print(f"Answer: {(first_int - second_int)}")
                case 'mul':
                    print(f"Answer: {(first_int * second_int)}")
                case 'div':
                    if second_int == 0:
                        print("cannot divide by zero")
                        continue
                    print(f"Answer: {(first_int / second_int)}")

        except:
            print("You've reached an exception. ")

    
    
    
if __name__ == '__main__':
    ex14()
    