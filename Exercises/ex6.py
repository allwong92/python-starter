def ex6():
    myList = [11, 100, 101, 999, 1001]
    end = len(myList)-1
    for i in range(0,len(myList)//2):
        last_digit = myList[end]
        myList[end] = myList[i]
        myList[i] = last_digit
        end = end - 1
    
    print(myList)

    
if __name__ == '__main__':
    ex6()