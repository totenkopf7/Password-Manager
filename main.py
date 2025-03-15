from tkinter import *
# this is not a class that is why it was not in the (*)
from tkinter import messagebox
import random
import pyperclip
import json
# Class for login window

class loginWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("To login, enter name and password")
        self.config(padx=50, pady=50, width=500, height=350, bg="#282120")
        self.resizable(False, False)


        self.canvas = Canvas(self, width=200, height=200, bg="#282120", highlightthickness=0)
        self.logo_image = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_image)
        self.canvas.grid(column=1, row=0)

        self.username_check_label = Label(self, text="Name:", bg="#282120", fg="#D4483B")
        self.username_check_label.grid(column=0, row=2)
        self.password_check_label = Label(self, text="Password:", bg="#282120", fg="#D4483B")
        self.password_check_label.grid(column=0, row=3)
        self.space1 = Label(self, text=" ", bg="#282120")
        self.space1.grid(column=1, row=1)

        self.username_check_input = Entry(self, width=32, bg="#282120", fg="#D4483B", insertbackground="#D4483B")
        self.username_check_input.grid(column=1, row=2)
        self.username_check_input.focus()
        self.password_check_input = Entry(self, width=32, bg="#282120", fg="#D4483B", insertbackground="#D4483B", show="*")
        self.password_check_input.grid(column=1, row=3)
        self.space2 = Label(self, text=" ", bg="#282120")
        self.space2.grid(column=0, row=4)
        self.enter_button = Button(self, text="Login", width=7, bg="#282120", fg="#D4483B", command=self.validate)
        self.enter_button.grid(column=1, row=5, columnspan=2)

    def validate(self):
        username = self.username_check_input.get()
        password = self.password_check_input.get()
        if username == "username" and password == "password":
            self.destroy()
            global load_manager
            load_manager()
        else:
            messagebox.showwarning(title="Error", message="Incorrect name and/or password!")
            self.username_check_input.delete(0, END)
            self.password_check_input.delete(0, END)


# This function loads the password manager after logging in.


def load_manager():
    app = ManagerWindow()
    app.mainloop()


# Class for managerWindow


class ManagerWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Password Manager")
        self.config(padx=50, pady=50, bg="#282120")
        self.resizable(False, False)


        self.canvas = Canvas(self, width=200, height=200, bg="#282120", highlightthickness=0)
        self.logo_image = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_image)
        self.canvas.grid(column=1, row=0)

        # Labels
        self.website_label = Label(self, text="Website:", bg="#282120", fg="#D4483B")
        self.website_label.grid(column=0, row=2)
        self.email_label = Label(self, text="Email:", bg="#282120", fg="#D4483B")
        self.email_label.grid(column=0, row=3)
        self.password_label = Label(self, text="Password:", bg="#282120", fg="#D4483B")
        self.password_label.grid(column=0, row=4)
        self.line_label1 = Label(self, text=" ", bg="#282120")
        self.line_label1.grid(column=1, row=1)
        self.line_label2 = Label(self, text=" ", bg="#282120")
        self.line_label2.grid(column=1, row=5)

        # Entries
        self.website_input = Entry(self, width=32, bg="#282120", fg="#D4483B", insertbackground="#D4483B")
        self.website_input.grid(column=1, row=2)
        self.website_input.focus()
        self.email_input = Entry(self, width=32, bg="#282120", fg="#D4483B", insertbackground="#D4483B")
        self.email_input.grid(column=1, row=3)
        # self.email_input.insert(0, "anything@gmail.com")
        self.password_input = Entry(self, width=32, bg="#282120", fg="#D4483B", insertbackground="#D4483B")
        self.password_input.grid(column=1, row=4)

        # Buttons
        self.generate_password_button = Button(self, text="Generate a password", bg="#282120", fg="#D4483B", command=self.generate_password)
        self.generate_password_button.grid(column=2, row=4)

        self.add_password = Button(self, text="Add", width=45, bg="#282120", fg="#D4483B", command=self.save)
        self.add_password.grid(column=1, row=6, columnspan=2)

        self.search = Button(self, text="Search", width=14, bg="#282120", fg="#D4483B", command=self.find_password)
        self.search.grid(column=2, row=2)

    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []


        password_letters = [random.choice(letters) for _ in range(nr_letters)]

        password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

        password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
        password_list = password_letters + password_symbols + password_numbers
        random.shuffle(password_list)


        password = "".join(password_list)
        self.password_input.delete(0, "end") #Clear the password input before inserting
        self.password_input.insert(0, password)
        pyperclip.copy(password)

    def save(self):
        website = self.website_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        new_data = {

            website: {
                "email": email,
                "password": password,

            }

                    }

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please fill all the fields!")

        else:
            try:
                with open("data.json", "r") as file:

                    # Reading old data
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # Updating old data with new data
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                self.website_input.delete(0, END)
                self.email_input.delete(0, END)
                self.password_input.delete(0, END)
                self.website_input.focus()

    def find_password(self):
        website = self.website_input.get()
        try:
            with open("data.json") as file:
                data = json.load(file)

        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="Not found!")

        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\n\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"  Password for {website} not found:  ")


app = loginWindow()
app.mainloop()





