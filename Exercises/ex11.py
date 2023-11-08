import datetime as dt
def ex11():
    date = open("output.txt", 'a') # a means append to file
    print(dt.datetime.now())
    x = dt.datetime.now().strftime('%x') # legal format code for local version of date
 
    date.write(f"Today's Date is: {x}.\n")  # write to output.txt
    date.close()


if __name__ == '__main__':
    ex11()