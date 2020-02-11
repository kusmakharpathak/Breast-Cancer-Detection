from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Plot(Tk):
    def __init__(self, mean_radius, mean_perimeter, mean_area, radius_worst, perimeter_worst, name, contact):
        super(Plot, self).__init__()
        self.title(f"Report graph of {name} ({contact})")
        self.iconbitmap("E:\\Python\\BreastCancer\\icon\\favicon.ico")
        self.mean_radius = mean_radius
        self.mean_perimeter = mean_perimeter
        self.radius_worst = radius_worst
        self.perimeter_worst = perimeter_worst
        self.mean_area = mean_area
        self.name = name
        self.contact = contact
        self.canvas()

    def canvas(self):
        fig = Figure(figsize=(10, 5), dpi=100)
        x = ['mean_radius', 'mean_perimeter', 'mean_area', 'radius_worst', 'perimeter_worst']
        y_max = [17.85, 114.6, 992.1, 19.82, 127.1]
        y = [self.mean_radius, self.mean_perimeter, self.mean_area, self.radius_worst, self.perimeter_worst]
        a = fig.add_subplot(111)
        a.plot(x, y, "#00A3E0", label="Your Report")
        a.scatter(x, y)
        a.plot(x, y_max, 'r', label="Min Range")
        a.scatter(x, y_max)
        fig.legend()
        plt = FigureCanvasTkAgg(fig, self)
        a.set_xlabel("Diagnosis", fontsize=15)
        a.set_ylabel("Report", fontsize=15)
        fig.savefig(f"E:\\Python\\BreastCancer\\common\\docs\\{self.name} ({self.contact}).png", dpi=200)
        plt.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)


# root = Plot(21.56, 142.00, 1479.0, 25.450, 166.10, 'krishna', 9869284295)
# # # #
# root.mainloop()
