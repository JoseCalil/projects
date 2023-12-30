import random
import string

def password_generator():

    length = int(input('How many characters do you need? \n'))
    
    if length < 3:
        print("\nPassword length must be at least 3 characters to meet the requirements!\n")
        print("Please select a valid length. \n")
        print("-----------------------------------------------------------------------")
        password_generator()
    
    uppercase_char = random.choice(string.ascii_lowercase)
    lowercase_char = random.choice(string.ascii_uppercase)
    special_char = random.choice('!@#$%^&*')

    rest_of_password = length -3
    all_chars = string.ascii_letters + '1234567890!@#$%^&*'
    random_chars = ''.join(random.choice(all_chars) for _ in range(rest_of_password))

    password = uppercase_char + lowercase_char + special_char +random_chars
    return password

random_password = password_generator()
print(f"Your new random password is: {random_password}" )




    
