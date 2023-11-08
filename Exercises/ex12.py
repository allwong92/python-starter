def ex12():
    userInput = input("Enter integer: ")
    
    try:
         userInput = int(userInput) 
         userInput *= -1
         print(userInput)
    except:
        print(f"ERROR: {userInput} is not an integer.")
    
        
if __name__ == '__main__':
    ex12()