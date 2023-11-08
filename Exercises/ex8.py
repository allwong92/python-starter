def ex8():
    myList = [6,2,7,3,77,7,1]
    min = myList[0]
    for i in myList:
        if i < min:
            min = i
    print(min)


if __name__ == '__main__':
    ex8()