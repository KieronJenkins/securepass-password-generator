import random

password_choice = ["YES", "Yes", "yes", "Y", "y"] #If user types any of these for generate_password

password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%&*@#^[]{}~()<>=+:;/" #List of characters used in password
generate_password = input("Do you want a randomly generated password? Please answer Yes or No: \n")


def random_choice():
    random_length = int(random.uniform(8, 128)) #Randoms between 8 and 128 characters
    if generate_password in password_choice: #If users answer matches password_choice
        random_password = "" #Password shell
        for rp in range(random_length): #Selecting the random length
            random_password += random.choice(password_characters) #Randomly picking from password_characters
        print(f"Random Password: {random_password}") #Prints random password
        return
    else:
        password_gen() #If user types anything other than password_choice runs password_gen function


def password_gen():
    password_amount = input("How many characters do you want your password to have:\n")
    password_amount = int(password_amount) #User puts in the number for password length
    for i in range(password_amount): #Selects users number
        user_password = "" 
        for p in range(password_amount): 
            user_password += random.choice(password_characters) #Randomly picking from password_characters

    print(f"Password: {user_password}")


random_choice()
