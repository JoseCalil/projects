import random
import string

#function that creates the password
def password_generator():
    
#allows user to choose the length required
    length = int(input('How many characters do you need? \n'))
   
    if length < 3:
        print("\nPassword length must be at least 3 characters to meet the requirements!\n")
        print("Please select a valid length. \n")
        print("-----------------------------------------------------------------------")
        return password_generator()
    
    uppercase_char = random.choice(string.ascii_lowercase)
    lowercase_char = random.choice(string.ascii_uppercase)
    special_char = random.choice('!@#$%^&*')

    rest_of_password = length -3
    all_chars = string.ascii_letters + '1234567890!@#$%^&*'
    random_chars = ''.join(random.choice(all_chars) for _ in range(rest_of_password))

    password = uppercase_char + lowercase_char + special_char +random_chars
    return password
    
#allows user to choose a new password if they don't like it or to keep it
def redo_password():

    while True:

        print("\nAre you satisfied with you password or would you like a new one? \n")
        print("1. I\'m satisfied with it!")
        print("2. Let me get a different password!")
        choice = input("\nEnter decision here: ")

        if choice == '1':
            print("That\'s awesome, enjoy!\n")
            print("Have a great day!")
            print("-----------------------------------------------------------------------")
            break

        elif choice == '2':
            print("No worries at all! Let\'s get you set with a new password!")
            print("-----------------------------------------------------------------------")
            new_password = password_generator()
            print(f"Your new random password is: {new_password}")
            print("-----------------------------------------------------------------------")
            
            
        else :
            print("Please choose to keep your password or get a new password.")
            print("-----------------------------------------------------------------------")
            redo_password()

random_password = password_generator()
print(f"Your new random password is: {random_password}")

redo_password()
