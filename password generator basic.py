import random

def password_generator():
    chars  = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*'
    password =''

    for x in range(5):
        password += random.choice(chars)
    return password

random_password = password_generator()
print(f"Hello, your random password is: {random_password}" )




    