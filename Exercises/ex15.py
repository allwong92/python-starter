import datetime as dt
def ex15():
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
            answer = 0    

            match op:
                case 'add':
                    answer = first_int + second_int
                    print(f"Answer: {answer}")
                case 'sub':
                    answer = first_int - second_int
                    print(f"Answer: {answer}")
                case 'mul':
                    answer = first_int * second_int
                    print(f"Answer: {answer}")
                case 'div':
                    if second_int == 0:
                        print("cannot divide by zero")
                        continue
                    answer = first_int / second_int
                    print(f"Answer: {answer}")

            file = open("ouput.txt", 'a')
            date = dt.datetime.now().strftime('%x')+ ' ' + dt.datetime.now().strftime('%X') + ' ' + dt.datetime.now().strftime('%p')
            
            file.write(f"{date}: {first_int} {op} {second_int} = {answer} \n")
            
            file.close()

        except:
            print("You've reached an exception. ")
    
if __name__ == '__main__':
    ex15()