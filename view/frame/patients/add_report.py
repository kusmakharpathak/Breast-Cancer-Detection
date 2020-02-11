import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from model.patient.diagnosis import Diagnosis


class AddReport(ttk.Frame):
    def __init__(self, parent, controller, record, **kwargs):
        super().__init__(parent)
        self.record = record
        self.contact_no = controller.contact_no
        self.doc_id = controller.doc_id
        self.pat_id = controller.pat_id
        self.dig_id = controller.dig_id

        self.mean_radius = controller.mean_radius
        self.mean_perimeter = controller.mean_perimeter
        self.radius_worst = controller.radius_worst
        self.perimeter_worst = controller.perimeter_worst
        self.mean_area = controller.mean_area

        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        add_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="Background.TFrame"
        )

        add_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        add_container.columnconfigure(0, weight=1)
        add_container.rowconfigure(1, weight=1)

        radius_label = ttk.Label(
            add_container,
            text="Mean Radius: ",
            style="LightText.TLabel"
        )
        texture_label = ttk.Label(
            add_container,
            text="Mean Area: ",
            style="LightText.TLabel"
        )

        perimeter_label = ttk.Label(
            add_container,
            text="Mean Perimeter: ",
            style="LightText.TLabel"
        )
        area_label = ttk.Label(
            add_container,
            text="Radius Worst: ",
            style="LightText.TLabel"
        )
        smoothness_label = ttk.Label(
            add_container,
            text="Perimeter Worst: ",
            style="LightText.TLabel"
        )

        radius_label.grid(column=0, row=1, sticky="W")
        texture_label.grid(column=2, row=1, sticky="W")
        perimeter_label.grid(column=0, row=2, sticky="W")
        area_label.grid(column=2, row=2, sticky="W")
        smoothness_label.grid(column=0, row=3, sticky="W")

        radius_input = tk.Entry(
            add_container,
            justify="left",
            textvariable=self.mean_radius,
            width=20,
            font=("TkDefaultFont", 15)
        )
        texture_input = tk.Entry(
            add_container,
            justify="left",
            textvariable=self.mean_area,
            width=20,
            font=("TkDefaultFont", 15)
        )

        perimeter_input = tk.Entry(
            add_container,
            justify="left",
            textvariable=self.mean_perimeter,
            width=20,
            font=("TkDefaultFont", 15)
        )
        area_input = tk.Entry(
            add_container,
            justify="left",
            textvariable=self.radius_worst,
            width=20,
            font=("TkDefaultFont", 15)
        )
        smoothness_input = tk.Entry(
            add_container,
            justify="left",
            textvariable=self.perimeter_worst,
            width=20,
            font=("TkDefaultFont", 15)
        )

        radius_input.grid(column=1, row=1, sticky="EW")
        texture_input.grid(column=3, row=1, sticky="EW")
        perimeter_input.grid(column=1, row=2, sticky="EW")
        area_input.grid(column=3, row=2, sticky="EW")
        smoothness_input.grid(column=1, row=3, sticky="EW")
        radius_input.focus()

        for child in add_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self, style="Background.TFrame")
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        self.add_button = ttk.Button(
            button_container,
            text="Add = >",
            style="Email.TButton",
            cursor="hand2"
        )
        self.back_button = ttk.Button(
            button_container,
            text="<=",
            style="Email.TButton",
            cursor="hand2"
        )
        self.add_button.grid(column=1, row=0, sticky="W", padx=2)
        self.back_button.grid(column=0, row=0, sticky="E", padx=2)

        self.add_button['command'] = self.add
        self.back_button['command'] = self.back

    def add(self):
        # dig = Diagnosis.find_by_patient_id(self.pat_id.get())
        print(
            f"mean_radius = {self.mean_radius.get()}\nmean_area = {self.mean_area.get()}\nmean_perimeter = {self.mean_perimeter.get()}"
            f"\nperimeter_worst = {self.perimeter_worst.get()}\nradius_worst = {self.radius_worst.get()}\npat_id = {self.pat_id.get()}")
        print(f"Dig Id = {self.dig_id.get()}")
        if (self.mean_radius.get() == '') or (self.mean_perimeter.get() == '') or (self.radius_worst.get() == '') or (
                self.perimeter_worst.get() == '') or (self.mean_area.get() == '') or (self.pat_id.get() == ''):
            print("Null Value")
            mb.showinfo("Report", "Please Enter All Details")
        elif self.dig_id.get() == '':
            # mean_radius, mean_perimeter, radius_worst, perimeter_worst, mean_area, diagnosis, patient_id
            Diagnosis.add_record(float(self.mean_radius.get()), float(self.mean_perimeter.get()),
                                 float(self.radius_worst.get()), float(self.perimeter_worst.get()),
                                 float(self.mean_area.get()), int(0), self.pat_id.get())
            mb.showinfo("Report", "Reported Added Success")
            print("success")
        elif self.dig_id.get():
            Diagnosis.update_record(float(self.mean_radius.get()), float(self.mean_perimeter.get()),
                                    float(self.radius_worst.get()), float(self.perimeter_worst.get()),
                                    float(self.mean_area.get()), int(0), self.pat_id.get(),
                                    self.dig_id.get())
            print(self.dig_id.get())
            mb.showinfo("Report", "Reported Updated Success")
            print("success")

    def back(self):
        self.back_button['command'] = self.record
