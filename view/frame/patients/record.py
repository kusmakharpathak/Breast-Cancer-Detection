import tkinter as tk
from tkinter import ttk
from tksheet import Sheet
from tkinter import messagebox as mb
from model.patient.diagnosis import Diagnosis
from model.patient.patient import Patient
from model.user.user import Users
from model.predict.predict_module import Predict
from view.plot.plot import Plot
from common.utils.utils import Utils

from datetime import datetime


def exit1():
    print("Exit")
    if mb.askyesno('Exit', 'Are You Sure you want to Exit?'):
        mb.showinfo('Exit', 'Thank you\nSee you soon')
        exit()
    else:
        mb.showinfo('Back', 'You are not Exit')


class Record(ttk.Frame):
    def __init__(self, parent, controller, show_record):
        super().__init__(parent)
        self.search = controller.search
        self.email = controller.email
        self.dig_report = controller.dig_report
        self.doc_id = controller.doc_id
        self.pat_id = controller.pat_id
        self.dig_id = controller.dig_id

        self.mean_radius = controller.mean_radius
        self.mean_perimeter = controller.mean_perimeter
        self.radius_worst = controller.radius_worst
        self.perimeter_worst = controller.perimeter_worst
        self.mean_area = controller.mean_area

        self.add = show_record
        self.value_err = controller.value_err
        self.table = Sheet(self, height=500)
        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        settings_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="Background.TFrame"
        )

        settings_container.grid(row=0, column=0, sticky="EW", padx=5, pady=5)

        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(0, weight=1)

        search_label = ttk.Label(
            settings_container,
            text="Search =>",
            style="LightText.TLabel"
        )
        value_err = ttk.Label(
            settings_container,
            textvariable=self.value_err,
            style="Error.TLabel",
        )

        search_label.grid(column=0, row=1, sticky="W")
        value_err.grid(row=2, columnspan=3, sticky="W", pady=3)

        contact_no = tk.Entry(
            settings_container,
            justify="left",
            textvariable=self.search,
            width=40,
            font=("TkDefaultFont", 15)
        )
        contact_no.grid(column=1, row=1, sticky="EW")
        contact_no.focus()

        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self, style="Background.TFrame")
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)
        button_container.rowconfigure(0, weight=1)

        self.search_button = ttk.Button(
            settings_container,
            text="Search",
            # command=self.next,
            style="Email.TButton",
            cursor="hand2"  # hand1 in some systems
        )
        self.view_button = ttk.Button(
            settings_container,
            text="View All Patients",
            # command=self.next,
            style="Email.TButton",
            cursor="hand2"  # hand1 in some systems
        )
        self.delete_button = ttk.Button(
            settings_container,
            text="Remove",
            # command=self.next,
            style="Email.TButton",
            cursor="hand2"  # hand1 in some systems
        )
        self.add_report_button = ttk.Button(
            settings_container,
            text="Add/Update Report",
            # command=self.next,
            style="Email.TButton",
            cursor="hand2"  # hand1 in some systems
        )
        self.view_report_button = ttk.Button(
            settings_container,
            text="View Report",
            # command=self.next,
            style="Email.TButton",
            cursor="hand2"
        )

        self.exit_button = ttk.Button(
            settings_container,
            text="Exit/Logout",
            style="Email.TButton",
            cursor="hand2"
        )

        self.search_button.grid(column=2, row=1, sticky="EW", padx=2)
        self.view_button.grid(column=3, row=1, sticky="EW", padx=2)
        self.add_report_button.grid(column=3, row=2, sticky="EW", padx=2)
        self.view_report_button.grid(column=2, row=2, sticky="EW", padx=2)
        self.delete_button.grid(column=2, row=3, sticky="EW", padx=2)
        self.exit_button.grid(column=3, row=3, sticky="EW", padx=2)
        self.search_button['command'] = self.search_func
        self.view_button['command'] = self.view
        self.add_report_button['command'] = self.add_report
        self.view_report_button['command'] = self.rep
        self.delete_button['command'] = self.remove
        self.exit_button['command'] = exit1

    def many_value(self, val):
        print(len(val))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.table = Sheet(self, data=[[f"{r}, {c}" for c in range(8)] for r in range(len(val))], height=500, width=100)
        self.table.enable_bindings("single_select")
        self.table.grid(row=1, column=0, sticky="nswe")
        self.table.extra_bindings([
            ("cell_select", self.cell_select),
        ])
        self.table.change_theme("dark")

        self.table.column_width(column=0, width=30)
        self.table.column_width(column=1, width=100)
        self.table.column_width(column=2, width=100)
        self.table.column_width(column=5, width=200)
        self.table.column_width(column=6, width=200)
        self.table.headers((f"Header {c}" for c in range(8)))
        self.table.headers("Sn", 0)
        self.table.headers("First Name", 1)
        self.table.headers("Last Name", 2)
        self.table.headers("contact", 3)
        self.table.headers("Gender", 4)
        self.table.headers("Address", 5)
        self.table.headers("Date of Birth", 6)
        self.table.headers("Email", 7)
        # a = val[1].f_name
        for i in range(len(val)):
            self.table.set_cell_data(i, 1, val[i].f_name)
            self.table.set_cell_data(i, 2, val[i].l_name)
            self.table.set_cell_data(i, 3, val[i].contact_no)
            self.table.set_cell_data(i, 4, val[i].gender)
            self.table.set_cell_data(i, 5, val[i].address)
            self.table.set_cell_data(i, 6, val[i].dob)
            self.table.set_cell_data(i, 7, val[i].email)

        for i in range(len(val)):
            self.table.set_cell_data(i, 0, i + 1)

        self.table.hide("row_index")
        self.table.hide("top_left")

    def find_one(self, val):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.table = Sheet(self, data=[[f"{r}, {c}" for c in range(8)] for r in range(1)], height=100, width=100)
        self.table.enable_bindings("single_select")
        self.table.grid(row=1, column=0, sticky="nswe")
        self.table.extra_bindings([
            ("cell_select", self.cell_select),
        ])
        self.table.change_theme("dark")

        self.table.column_width(column=0, width=30)
        self.table.column_width(column=1, width=100)
        self.table.column_width(column=2, width=100)
        self.table.column_width(column=5, width=200)
        self.table.column_width(column=6, width=200)
        self.table.headers((f"Header {c}" for c in range(8)))
        self.table.headers("Sn", 0)
        self.table.headers("First Name", 1)
        self.table.headers("Last Name", 2)
        self.table.headers("contact", 3)
        self.table.headers("Gender", 4)
        self.table.headers("Address", 5)
        self.table.headers("Date of Birth", 6)
        self.table.headers("Email", 7)
        # a = val[1].f_name
        self.table.set_cell_data(0, 1, val.f_name)
        self.table.set_cell_data(0, 2, val.l_name)
        self.table.set_cell_data(0, 3, val.contact_no)
        self.table.set_cell_data(0, 4, val.gender)
        self.table.set_cell_data(0, 5, val.address)
        self.table.set_cell_data(0, 6, val.dob)
        self.table.set_cell_data(0, 7, val.email)
        # self.table.set_cell_data(0, 5, val._id)

        self.table.set_cell_data(0, 0, 1)

        self.table.hide("row_index")
        self.table.hide("top_left")

    def view_report(self, val):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.table = Sheet(self, data=[[f"{r}, {c}" for c in range(7)] for r in range(1)], height=100, width=100)
        self.table.enable_bindings("single_select")
        self.table.grid(row=1, column=0, sticky="nswe")
        self.table.extra_bindings([
            ("cell_select", self.cell_select1),
        ])
        self.table.change_theme("dark")

        self.table.column_width(column=0, width=30)
        self.table.column_width(column=1, width=100)
        self.table.column_width(column=2, width=100)
        self.table.column_width(column=5, width=200)
        self.table.column_width(column=6, width=200)
        self.table.headers((f"Header {c}" for c in range(7)))
        self.table.headers("Sn", 0)
        self.table.headers("Mean Radius", 1)
        self.table.headers("Mean Perimeter", 2)
        self.table.headers("Radius Worst", 3)
        self.table.headers("Perimeter Worst", 4)
        self.table.headers("Mean Area", 5)
        self.table.headers("Diagnosis", 6)
        # a = val[1].f_name
        self.table.set_cell_data(0, 1, val.mean_radius)
        self.table.set_cell_data(0, 2, val.mean_perimeter)
        self.table.set_cell_data(0, 3, val.radius_worst)
        self.table.set_cell_data(0, 4, val.perimeter_worst)
        self.table.set_cell_data(0, 5, val.mean_area)
        self.table.set_cell_data(0, 6, val.diagnosis)
        # self.table.set_cell_data(0, 5, val._id)

        self.table.set_cell_data(0, 0, 1)

        self.table.hide("row_index")
        self.table.hide("top_left")

    def search_func(self):
        print(self.search.get())
        self.data = self.table.set_sheet_data(verify=False)
        if self.search.get() == '':
            print(self.value_err.get())
            self.value_err.set("Enter Patients contact number")
            mb.showinfo("Report", "Please Enter Contact No")
            print(self.value_err.get())
            self.data = self.table.set_sheet_data(verify=False)
        else:
            patient = Patient.find_by_contact_no(self.search.get())
            if self.doc_id.get() == '':
                if patient:
                    self.value_err.set('')
                    self.find_one(patient)
                    self.mean_radius.set('')
                    self.mean_perimeter.set('')
                    self.radius_worst.set('')
                    self.perimeter_worst.set('')
                    self.mean_area.set('')
                else:
                    print(self.value_err.get())
                    self.value_err.set("No record Found")
                    mb.showinfo("Report", "No Record Found")
                    print(self.value_err.get())
                    self.data = self.table.set_sheet_data(verify=False)
            else:
                self.find_one(patient)

    def view(self):
        self.value_err.set('')
        val = Patient.find_all_by_doc_id(self.doc_id.get())
        if val:
            self.many_value(val)
        else:
            self.value_err.set('No Record Found')
            mb.showinfo("Report", "No Record Found")

    def rep(self):
        val = Diagnosis.find_by_patient_id(self.pat_id.get())
        if self.pat_id.get() == '':
            self.dig_id.set('')
            self.value_err.set("Please Select Patients")
            mb.showinfo("Report", "Please Select Patients")
        else:
            if val:
                self.value_err.set('')
                print(val)
                print(val.mean_radius)
                print(val.mean_perimeter)
                print(val.radius_worst)
                print(val.perimeter_worst)
                print(val.mean_area)
                print(val.diagnosis)
                self.view_report(val)
                self.mean_radius.set(val.mean_radius)
                self.mean_perimeter.set(val.mean_perimeter)
                self.radius_worst.set(val.radius_worst)
                self.perimeter_worst.set(val.perimeter_worst)
                self.mean_area.set(val.mean_area)

            else:
                print(self.value_err.get())
                self.value_err.set("No record Found")
                mb.showinfo("Report", "No Record Found")
                print(self.value_err.get())
                self.data = self.table.set_sheet_data(verify=False)
                self.dig_id.set('')
                self.mean_radius.set('')
                self.mean_perimeter.set('')
                self.radius_worst.set('')
                self.perimeter_worst.set('')
                self.mean_area.set('')

    def cell_select(self, response):
        a = list(response)
        contact = self.table.get_cell_data(a[1], 3)
        self.search.set(contact)
        patient = Patient.find_by_contact_no(contact)
        a = patient._id
        self.pat_id.set(a)
        print(self.pat_id.get())

    def cell_select1(self, response):
        # a = list(response)
        patients = Patient.find_by_contact_no(self.search.get())
        file = open(f"E:\\Python\\BreastCancer\\common\\docs\\{patients.f_name} ({patients.contact_no}).txt", 'a')
        val = Diagnosis.find_by_patient_id(self.pat_id.get())
        a = val._id
        email = patients.email
        doc = Users.find_by_id(patients.doctor_id)
        print(doc.f_name)
        print(doc.email)
        print(email)
        self.dig_id.set(a)
        test = Predict(val.mean_radius, val.mean_perimeter, val.radius_worst, val.perimeter_worst, val.mean_area)
        res = test.predict()
        if res:
            root = Plot(val.mean_radius, val.mean_perimeter, val.mean_area, val.radius_worst, val.perimeter_worst, patients.f_name, patients.contact_no)
            # root.mainloop()
            mb.showinfo("Report",
                        f"You are suffer from Breast Cancer till date\n"
                        f"Your Overall Report Are\n"
                        f"Test\t\t\tResults\t\tRef. Range\n"
                        f"-------------------------------------------------------------------------\n"
                        f"Mean Radius\t\t{self.mean_radius.get()}\t\t>17.85\n"
                        f"Mean Perimeter\t\t{self.mean_perimeter.get()}\t\t>114.6\n"
                        f"Mean Area\t\t{self.mean_area.get()}\t\t>992.1\n"
                        f"Radius Worst\t\t{self.radius_worst.get()}\t\t>19.82\n"
                        f"Perimeter Worst\t\t{self.perimeter_worst.get()}\t\t>127.1\n",
                        )
            Diagnosis.update_record(float(self.mean_radius.get()), float(self.mean_perimeter.get()),
                                    float(self.radius_worst.get()), float(self.perimeter_worst.get()),
                                    float(self.mean_area.get()), int(1), self.pat_id.get(),
                                    self.dig_id.get())
            file.write(
                f"\n=======================================================================\n"
                f"{patients.f_name}\n"
                f"Date = {datetime.today().strftime('%Y-%B-%d')}\n"
                f"Time = {datetime.today().strftime('%I:%M:%S %p')}\n"
                f"=======================================================================\n"
                "Report"
                f"You are not are suffer from Breast Cancer till date\n"
                f"Your Overall Report Are\n"
                f"Test\t\t\tResults\t\tRef. Range\n"
                f"-------------------------------------------------------------------------\n"
                f"Mean Radius\t\t{self.mean_radius.get()}\t\t>17.85\n"
                f"Mean Perimeter\t\t\t{self.mean_perimeter.get()}\t\t>114.6\n"
                f"Mean Area\t\t{self.mean_area.get()}\t\t>992.1\n"
                f"Radius Worst\t\t\t{self.radius_worst.get()}\t\t>19.82\n"
                f"Perimeter Worst\t\t{self.perimeter_worst.get()}\t\t>127.1\n"
                f"\n=======================================================================\n\n"
            )
            file.close()
            root.destroy()
            if patients.email == '':
                print("No email address")
            else:
                Utils.send_mail(patients.email, f"{patients.f_name} ({patients.contact_no}).txt",
                                f"{patients.f_name} ({patients.contact_no}).png", doc.f_name, doc.l_name)
            root.mainloop()

        else:
            root = Plot(val.mean_radius, val.mean_perimeter, val.mean_area, val.radius_worst, val.perimeter_worst, patients.f_name, patients.contact_no)
            mb.showinfo("Report",
                        f"You are not suffer from Breast Cancer till date\n"
                        f"Your Overall Report Are\n"
                        f"Test\t\t\tResults\t\tRef. Range\n"
                        f"-------------------------------------------------------------------------\n"
                        f"Mean Radius\t\t{self.mean_radius.get()}\t\t>17.85\n"
                        f"Mean Perimeter\t\t{self.mean_perimeter.get()}\t\t>114.6\n"
                        f"Mean Area\t\t{self.mean_area.get()}\t\t>992.1\n"
                        f"Radius Worst\t\t{self.radius_worst.get()}\t\t>19.82\n"
                        f"Perimeter Worst\t\t{self.perimeter_worst.get()}\t\t>127.1\n",
                        )
            Diagnosis.update_record(float(self.mean_radius.get()), float(self.mean_perimeter.get()),
                                    float(self.radius_worst.get()), float(self.perimeter_worst.get()),
                                    float(self.mean_area.get()), int(0), self.pat_id.get(),
                                    self.dig_id.get())
            file.write(
                f"\n=======================================================================\n"
                f"{patients.f_name}\n"
                f"Date = {datetime.today().strftime('%Y-%B-%d')}\n"
                f"Time = {datetime.today().strftime('%I:%M:%S %p')}\n"
                f"=======================================================================\n"
                "Report"
                f"You are not are suffer from Breast Cancer till date\n"
                f"Your Overall Report Are\n"
                f"Test\t\t\tResults\t\tRef. Range\n"
                f"-------------------------------------------------------------------------\n"
                f"Mean Radius\t\t{self.mean_radius.get()}\t\t>17.85\n"
                f"Mean Perimeter\t\t{self.mean_perimeter.get()}\t\t>114.6\n"
                f"Mean Area\t\t{self.mean_area.get()}\t\t>992.1\n"
                f"Radius Worst\t\t{self.radius_worst.get()}\t\t>19.82\n"
                f"Perimeter Worst\t\t{self.perimeter_worst.get()}\t\t>127.1\n"
                f"\n=======================================================================\n\n"
            )
            file.close()
            root.destroy()
            if patients.email=='':
                print("No email address")
            else:
                Utils.send_mail(patients.email, f"{patients.f_name} ({patients.contact_no}).txt",
                                f"{patients.f_name} ({patients.contact_no}).png", doc.f_name, doc.l_name)
            root.mainloop()
        print(self.dig_id.get())

    def add_report(self):
        if self.pat_id.get() == '':
            self.value_err.set("Please select Patients to add report")
        else:
            self.add_report_button['command'] = self.add
            print(self.pat_id.get())

    def remove(self):
        print(self.pat_id.get())
        if self.pat_id.get() == 'null':
            self.value_err.set("Please select Patients")
        else:

            if mb.askyesno('Verify', 'Are You Sure you want to remove?'):
                Patient.remove_pat(self.pat_id.get())
                Diagnosis.remove_pat(self.pat_id.get())
                mb.showwarning('Yes', 'Removed')
            else:
                mb.showinfo('No', 'Patients Data Remove cancelled')
