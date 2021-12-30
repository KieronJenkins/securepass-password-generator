from tkinter import *
from tkinter import ttk
from random import randint

# from random import randrange

root = Tk()
root.title("SecurePass Password Generator")  # Title of window
root.iconbitmap(r"C:\Users\kiero\Desktop\SecurePass-PasswordGen\static\icon.ico")  # Icon image
root.geometry("390x170")  # Window size
root.configure(bg="#2e2e3b", pady=0)  # Window background colour and padding
root.resizable(False, False)  # Stops window being resized
root.attributes('-topmost', 1)  # Window always appears ontop of other windows


def slider_changed(*args):
    slider_value = int(slider.get())  # Get value of slider (default 8)
    # print(slider_value)
    pass_ran_length = slider_value  # Sets length to slider value
    password_text.delete(0, END)  # Deletes all text
    pw_length = int(pass_ran_length)
    my_password = ""  # password shell

    for x in range(pw_length):
        my_password += chr(randint(33, 126))  # Randoms the characters and numbers being used

    password_text.insert(0, my_password)  # Show generated password


password_text = Entry(root, text="", font=("Montserrat", 20), bd=0, bg="#272733",
                      fg="#f7f7f7")  # Password box and font styling
password_text.pack(pady=10)  # Password box padding

slider = ttk.Scale(root, from_=8, to=100, orient='horizontal', command=slider_changed, length=360)  # Slider styling
slider.pack()
slider.set(8)  # Sets slider to default of 8

slider_label = Label(root, text="Password Length: 8 - 100", font=("Montserrat", 14), bg="#2e2e3b", bd=0, fg="#f7f7f7")
slider_label.pack()  # Label styling

frame = Frame(root)
frame.pack(pady=5)

generate_btn = Button(frame, text="Generate New Password", command=slider_changed, bd=0, cursor="hand2", width=51,
                      height=2, bg="#272733", activebackground="#2e2e3b", fg="#f7f7f7")  # Button styling
generate_btn.pack()

root.mainloop()

