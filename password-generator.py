import random

password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%&*@#^[]{}~()<>=+:;/"
password_amount = input("How many characters do you want your password to have:\n")
password_amount = int(password_amount)


def password_gen():
    for i in range(password_amount):
        user_password = ""
        for p in range(password_amount):
            user_password += random.choice(password_characters)

    print(f"Password: {user_password}")


password_gen()