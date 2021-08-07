import random

password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%&*@#^[]{}~()<>=+:;/" #Characters being used for password
password_amount = input("How many characters do you want your password to have:\n") 
password_amount = int(password_amount) #User types the length they want the password to be integers only


def password_gen():
    for i in range(password_amount):
        user_password = "" #Shell for password
        for p in range(password_amount):
            user_password += random.choice(password_characters) #Randoms between the characters in password_characters above

    print(f"Password: {user_password}") #Prints the generated password


password_gen() #Runs the above function
