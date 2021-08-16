from tkinter import *
from PIL import ImageTk, Image
import random
import string

password_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


def random_choice():
    random_length = int(25)  # Randoms between 8 and 128 characters
    random_password = ""  # Password shell
    random_password = "".join(random.sample(password_characters, random_length))
    return random_password


main_pass = random_choice()


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(main_pass)
    root.update()


root = Tk()
root.geometry("420x210")
root.configure(bg="#2e2e3b")
root.resizable(False, False)

root.title("SecurePass Password Generator")
root.iconbitmap(r"C:\Users\kiero\Desktop\SecurePass-PasswordGen\static\icon.ico")

header_img = ImageTk.PhotoImage(Image.open(r"C:\Users\kiero\Desktop\SecurePass-PasswordGen\static\securepass-logo.png"))
header_img_label = Label(image=header_img, bg="#2e2e3b", width=400)
header_img_label.grid(columnspan=3, column=1, row=0, pady=15, padx=5)

gen_password_img = PhotoImage(file=r"C:\Users\kiero\Desktop\SecurePass-PasswordGen\static\genpass-btn.png")
gen_exit_img = PhotoImage(file=r"C:\Users\kiero\Desktop\SecurePass-PasswordGen\static\exitpass-btn.png")
copy_icon = PhotoImage(file=r"C:\Users\kiero\Desktop\SecurePass-PasswordGen\static\copyicon.png")

password_amount = Entry(root, width=33, bg="#3d4255", fg="#f9f9f9", borderwidth=0, font="Montserrat")
password_amount.insert(10, main_pass)
password_amount.grid(columnspan=2, column=0, row=2, pady=10, padx=10)

copy_icon_btn = Button(root, image=copy_icon, width=20, height=20, borderwidth=0, bg="#2e2e3b", cursor="hand2",
                       activebackground="#2e2e3b", command=copy_password())
copy_icon_btn.grid(columnspan=3, column=2, row=2, pady=8)

generate_password_btn = Button(root, image=gen_password_img, width=175, height=36, borderwidth=0, bg="#2e2e3b",
                               cursor="hand2", activebackground="#2e2e3b", command=random_choice())
generate_password_btn.grid(columnspan=2, column=1, row=3, pady=4, padx=2)

root.mainloop()
