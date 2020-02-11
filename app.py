from tkinter import ttk
import tkinter as tk
from view import Email, Password, Das, Record, AddReport

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Timer.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure(
            "TimerText.TLabel",
            background=COLOUR_LIGHT_BACKGROUND,
            foreground=COLOUR_DARK_TEXT,
            font="Bahnschrift Light"
        )

        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
            font=("Bahnschrift Light", 15)
        )

        style.configure(
            "Error.TLabel",
            background=COLOUR_PRIMARY,
            foreground="red",
            font=("Bahnschrift Light", 12)
        )

        style.configure(
            "Email.TButton",
            background=[COLOUR_SECONDARY],
            foreground=COLOUR_LIGHT_TEXT,
            font=("Bahnschrift Light", 15)
        )

        style.map(
            "Email.TButton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        )

        style.configure(
            "Login.TButton",
            background=[COLOUR_SECONDARY],
            foreground='green',
            font=("Bahnschrift Light", 15)
        )

        style.map(
            "Login.TButton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        )

        style.configure(
            "View.TButton",
            background=[COLOUR_PRIMARY],
            foreground='green',
            font=("Bahnschrift Light", 15)
        )

        self["background"] = COLOUR_PRIMARY

        self.title("Breast Cancer Detection")
        self.resizable(False, False)
        self.iconbitmap("icon/favicon.ico")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.doc_id = tk.StringVar()
        self.dig_report = tk.StringVar()
        self.pat_id = tk.StringVar()
        self.dig_id = tk.StringVar()
        self.email = tk.StringVar()
        self.f_name = tk.StringVar()
        self.l_name = tk.StringVar()
        self.contact_no = tk.StringVar()
        self.address = tk.StringVar()
        self.dob = tk.StringVar()

        self.mean_radius = tk.StringVar()
        self.mean_perimeter = tk.StringVar()
        self.radius_worst = tk.StringVar()
        self.perimeter_worst = tk.StringVar()
        self.mean_area = tk.StringVar()

        self.gender = tk.StringVar(value="Gender")
        self.search = tk.StringVar(value='')
        self.password = tk.StringVar(value='')
        self.value_err = tk.StringVar(value='')
        self.ad = tk.StringVar(value='')
        self.pat_email = tk.StringVar(value='')
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = {}

        email = Email(container, self, lambda: self.show_frame(Password))
        password = Password(container, self, lambda: self.show_frame(Das))
        menu = Das(container, self, lambda: self.show_frame(Record))
        record = Record(container, self, lambda: self.show_frame(AddReport))
        add_report = AddReport(container, self, lambda: self.show_frame(Record))

        email.grid(row=0, column=0, sticky="NESW")
        password.grid(row=0, column=0, sticky="NESW")
        menu.grid(row=0, column=0, sticky="NESW")
        record.grid(row=0, column=0, sticky="NESW")
        add_report.grid(row=0, column=0, sticky="NESW")

        self.frames[Record] = record
        self.frames[Das] = menu
        self.frames[Password] = password
        self.frames[Email] = email
        self.frames[AddReport] = add_report

        self.show_frame(Email)

    def show_frame(self, container):
        if container == Record or container == AddReport:
            self.geometry("1100x700")
            self.resizable(False, False)
            frame = self.frames[container]
            frame.tkraise()
        elif container == Das:
            self.geometry("1000x700")
            self.resizable(False, False)
            frame = self.frames[container]
            frame.tkraise()
        else:
            self.geometry("700x250")
            frame = self.frames[container]
            frame.tkraise()


if __name__ == '__main__':
    root = App()
    root.mainloop()
    exit()
