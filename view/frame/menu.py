from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as mb
from model.patient.patient import Patient


class Das(ttk.Frame):
    def __init__(self, parent, controller, show_patients):
        super().__init__(parent)
        self.email = controller.email
        self.view_pat = show_patients
        self.geo = controller
        self.email = controller.email
        self.f_name = controller.f_name
        self.l_name = controller.l_name
        self.contact_no = controller.contact_no
        self.address = controller.address
        self.gender = controller.gender
        self.dob = controller.dob
        self.doc_id = controller.doc_id
        self.pat_email = controller.pat_email
        self.next = show_patients
        self.value_err = controller.value_err
        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        menu_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="Background.TFrame"
        )

        menu_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        menu_container.columnconfigure(0, weight=1)
        menu_container.rowconfigure(1, weight=1)

        for child in menu_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self, style="Background.TFrame")
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        self.view = ttk.Button(
            button_container,
            text="View Patients",
            style="View.TButton",
            cursor="hand2"
        )
        self.add = ttk.Button(
            button_container,
            text="Add Patients",
            style="View.TButton",
            cursor="hand2"
        )
        self.view.grid(column=0, row=2, sticky="EW", padx=2)
        self.add.grid(column=0, row=1, sticky="EW", padx=2, pady=10)

        self.view['command'] = self.view_pat
        self.add['command'] = self.add_pat

        # Add Box
        add_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="Background.TFrame"
        )

        add_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        add_container.columnconfigure(0, weight=1)
        add_container.rowconfigure(1, weight=1)

        f_name_label = ttk.Label(
            add_container,
            text="First Name: ",
            style="LightText.TLabel"
        )
        l_name_label = ttk.Label(
            add_container,
            text="Last Name: ",
            style="LightText.TLabel"
        )
        address_label = ttk.Label(
            add_container,
            text="Address: ",
            style="LightText.TLabel"
        )
        gender_label = ttk.Label(
            add_container,
            text="Gender: ",
            style="LightText.TLabel"
        )
        date_of_birth_label = ttk.Label(
            add_container,
            text="Date of Birth: ",
            style="LightText.TLabel"
        )
        contact_no_label = ttk.Label(
            add_container,
            text="Contact No: ",
            style="LightText.TLabel"
        )

        email_label = ttk.Label(
            add_container,
            text="Email: ",
            style="LightText.TLabel"
        )

        f_name_label.grid(column=0, row=1, sticky="W")
        l_name_label.grid(column=2, row=1, sticky="W")
        contact_no_label.grid(column=0, row=2, sticky="W")
        address_label.grid(column=2, row=2, sticky="W")
        gender_label.grid(column=0, row=3, sticky="W")
        date_of_birth_label.grid(column=2, row=3, sticky="W")
        email_label.grid(column=0, row=4, sticky="W")

        f_name_input = tk.Entry(
            add_container,
            justify="left",
            textvariable=controller.f_name,
            width=20,
            font=("TkDefaultFont", 15)
        )
        l_name_input = tk.Entry(
            add_container,
            justify="left",
            textvariable=controller.l_name,
            width=20,
            font=("TkDefaultFont", 15)
        )
        contact_no_input = tk.Entry(
            add_container,
            justify="left",
            textvariable=controller.contact_no,
            width=20,
            font=("TkDefaultFont", 15)
        )
        address_input = tk.Entry(
            add_container,
            justify="left",
            textvariable=controller.address,
            width=20,
            font=("TkDefaultFont", 15)
        )
        date_of_birth_input = tk.Entry(
            add_container,
            justify="left",
            textvariable=controller.dob,
            width=20,
            font=("TkDefaultFont", 15)
        )
        email_input = tk.Entry(
            add_container,
            justify="left",
            textvariable=controller.pat_email,
            width=20,
            font=("TkDefaultFont", 15)
        )

        value_err = ttk.Label(
            add_container,
            text="Hello",
            textvariable=self.value_err,
            style="Error.TLabel",
        )

        gender = ttk.Combobox(add_container, textvariable=controller.gender, font=("TkDefaultFont", 15))
        gender['value'] = ("Male", "Female")
        gender["state"] = "readonly"
        gender.grid(column=1, row=3, sticky="EW")

        f_name_input.grid(column=1, row=1, sticky="EW")
        l_name_input.grid(column=3, row=1, sticky="EW")
        contact_no_input.grid(column=1, row=2, sticky="EW")
        address_input.grid(column=3, row=2, sticky="EW")
        date_of_birth_input.grid(column=3, row=3, sticky="EW")
        email_input.grid(column=1, row=4, columnspan=3, sticky="EW")
        f_name_input.focus()

        for child in add_container.winfo_children():
            child.grid_configure(padx=5, pady=5)
        value_err.grid(row=5, columnspan=3, sticky="W", pady=3)

    def add_pat(self):
        self.geo.geometry("1000x700")
        print(f"first name = {self.f_name.get()}\nLast Name = {self.l_name.get()}\nContact No = {self.contact_no.get()}"
              f"\nAddress = {self.address.get()}\ngender = {self.gender.get()}\nDate of Birth = {self.dob.get()}\nDoc_id = {self.doc_id.get()}\nEmail = {self.pat_email.get()}")
        # def add_patient(cls, f_name, l_name, contact_no, dob, gender, address, doctor_id):
        if (self.f_name.get() == '') or (self.l_name.get() == '') or (self.contact_no.get() == '') or (self.dob.get() == '') or (self.gender.get() == '') or (self.address.get() == '') or (self.doc_id.get() == ''):
            print("Null Value")
            self.value_err.set("Please Enter all value")
        elif Patient.find_by_contact_no(self.contact_no.get()):
            print("Contact no already registered")
            self.value_err.set("Contact no already registered")
        elif self.doc_id.get() == '':
            print("Doctor id not found")
            self.value_err.set("Doctor id not found so login")
        elif self.gender.get() == "Gender":
            print("Select Gender")
            self.value_err.set("Select Gender")
        else:
            self.value_err.set("")
            if mb.askyesno('Exit', 'Details Check!!\n'
                                   f'First Name\t = {self.f_name.get()}\n'
                                   f'Last Name\t = {self.l_name.get()}\n'
                                   f'Contact No\t = {self.contact_no.get()}\n'
                                   f'Date of Birth\t = {self.dob.get()}\n'
                                   f'Gender\t = {self.gender.get()}\n'
                                   f'Address\t = {self.address.get()}\n'
                                   
                                   f'Email\t={self.pat_email.get()}'
                                   f'Doctor\t= {self.doc_id.get()}'):
                Patient.add_patient(self.f_name.get(), self.l_name.get(), self.contact_no.get(), self.dob.get(),
                                    self.gender.get(), self.address.get(), self.doc_id.get(), self.pat_email.get())
                mb.showinfo('Exit', 'Patients Added Success')
            else:
                mb.showinfo('Back', 'Patients Data Recheck')
