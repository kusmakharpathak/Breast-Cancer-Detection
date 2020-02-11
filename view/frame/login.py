import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from common.utils.utils import Utils
from model.user.user import Users


class Email(ttk.Frame):
    def __init__(self, parent, controller, show_password, **kwargs):
        super().__init__(parent, **kwargs)
        self.email = controller.email
        self.next = show_password
        self.value_err = controller.value_err

        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        email_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="Background.TFrame"
        )

        email_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        email_container.columnconfigure(0, weight=1)
        email_container.rowconfigure(1, weight=1)

        email_label = ttk.Label(
            email_container,
            text="Email: ",
            style="LightText.TLabel"
        )
        title_label = ttk.Label(
            email_container,
            text="Welcome To Breast Cancer Please Login: ",
            style="LightText.TLabel"
        )
        value_err = ttk.Label(
            email_container,
            text="Hello",
            textvariable=self.value_err,
            style="Error.TLabel",
        )
        email_label.grid(column=0, row=1, sticky="W")
        title_label.grid(column=0, row=0, columnspan=3, sticky="W")
        value_err.grid(row=2, columnspan=3, sticky="W")

        email_input = tk.Entry(
            email_container,
            justify="left",
            textvariable=self.email,
            width=40,
            font=("TkDefaultFont", 15)
        )
        email_input.grid(column=1, row=1, sticky="EW")
        email_input.focus()

        for child in email_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self, style="Background.TFrame")
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        self.next_button = ttk.Button(
            button_container,
            text="Next",
            style="Email.TButton",
            cursor="hand2"
        )
        self.next_button.grid(column=0, row=0, sticky="EW", padx=2)

        self.next_button['command'] = self.email_check

    def email_check(self):
        if self.email.get() == '':
            self.value_err.set("Please Enter Your email")
        elif not Utils.email_is_valid(self.email.get()):
            self.value_err.set("Please Enter valid email in format\teg: abc@def.ghi")
        else:
            if not Users.find_by_email(self.email.get()):
                self.value_err.set("Sorry we could not find your email")
                print("Sorry we could not find your email")
            else:
                self.value_err.set("")
                self.next_button['command'] = self.next


class Password(ttk.Frame):
    def __init__(self, parent, controller, show_menu, **kwargs):
        super().__init__(parent, **kwargs)
        self.email = controller.email
        self.password = controller.password
        self.doc_id = controller.doc_id
        self.menu = show_menu
        self.value_err = controller.value_err

        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        password_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="Background.TFrame"
        )

        password_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        password_container.columnconfigure(0, weight=1)
        password_container.rowconfigure(1, weight=1)

        password_label = ttk.Label(
            password_container,
            text="Password: ",
            style="LightText.TLabel"
        )
        value_err = ttk.Label(
            password_container,
            text="Hello",
            textvariable=self.value_err,
            style="Error.TLabel",
        )
        password_label.grid(column=0, row=1, sticky="W")
        value_err.grid(row=2, columnspan=3, sticky="W", pady=3)

        password_input = tk.Entry(
            password_container,
            justify="left",
            show="*",
            textvariable=controller.password,
            width=40,
            font=("TkDefaultFont", 15)
        )
        password_input.grid(column=1, row=1, sticky="EW")
        password_input.focus()

        for child in password_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self, style="Background.TFrame")
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        self.login_button = ttk.Button(
            button_container,
            text="Login",
            style="Login.TButton",
            cursor="hand2"  # hand1 in some systems
        )
        self.login_button.grid(column=0, row=0, sticky="EW", padx=2)

        self.login_button['command'] = self.password_check

    def password_check(self):
        if self.password.get() == '':
            self.value_err.set("Enter your Password")

        elif Users.login(self.email.get(), self.password.get()):
            self.value_err.set("")
            doc = Users.find_by_email(self.email.get())
            _id = doc.id
            self.doc_id.set(value=_id)
            print(self.doc_id.get())
            mb.showinfo('Welcome', 'Welcome to The System')
            self.login_button['command'] = self.menu
        else:
            self.value_err.set("Incorrect Password!!\t Try Again")
