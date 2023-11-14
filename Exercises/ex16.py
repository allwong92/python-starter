import hashlib as hl
def ex16():
    username_and_password = {}

    while True:
        username = input("Enter username: ")
        if username == 'exit':
            break

        password = input("Enter password: ")
        if password == 'exit':
            break
        
        username_and_password[username] = hl.sha256(password.encode('utf-8')).hexdigest()

    for key, value in username_and_password.items():
        print(f"{key}: {value}")
        

if __name__ == '__main__':
    ex16()