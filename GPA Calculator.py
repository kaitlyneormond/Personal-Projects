from tkinter import *

class GPACalculator(Tk):
    def __init__(self):
        super().__init__()
        self.title("GPA Calculator")
        self.geometry("800x800")
        self.create_main_window()

    def create_main_window(self):
        self.main_label = Label(self, text="GPA Calculator")
        self.main_label.pack(pady=10)

        # GPA Hours Entry
        self.hours_label = Label(self, text="Enter GPA Hours:")
        self.hours_label.pack(pady=5)
        self.hours_entry = Entry(self)
        self.hours_entry.pack(pady=5)

        # Cumulative GPA Entry
        self.gpa_label = Label(self, text="Enter Cumulative GPA:")
        self.gpa_label.pack(pady=5)
        self.gpa_entry = Entry(self)
        self.gpa_entry.pack(pady=5)

        # Number of classes taken
        self.class_amount_label = Label(self, text="Enter number of classes being taken:")
        self.class_amount_label.pack(pady=5)
        self.class_amount_entry = Entry(self)
        self.class_amount_entry.pack(pady=5)

        # Button to create rows for class inputs
        self.create_rows_button = Button(self, text="Create Class Inputs", command=self.create_rows)
        self.create_rows_button.pack(pady=5)

        # Calculate GPA Button
        self.calculate_gpa_button = Button(self, text="Calculate GPA", command=self.calculate_gpa)
        self.calculate_gpa_button.pack(pady=5)

        # Exit Button
        self.exit_button = Button(self, text="Exit", command=self.quit)
        self.exit_button.pack(pady=5)

        # Result Label
        self.result_label = Label(self, text="")
        self.result_label.pack(pady=5)

        # Container for class inputs
        self.class_inputs_frame = Frame(self)
        self.class_inputs_frame.pack(pady=5)

    def create_rows(self):
        try:
            num_classes = int(self.class_amount_entry.get())
            for widget in self.class_inputs_frame.winfo_children():
                widget.destroy()
            self.class_entries = []
            self.grade_vars = []
            for i in range(num_classes):
                frame = Frame(self.class_inputs_frame)
                frame.pack(pady=5)
                credit_label = Label(frame, text="Enter Credit Hours:")
                credit_label.pack(side=LEFT)
                credit_entry = Entry(frame)
                credit_entry.pack(side=LEFT, padx=5)
                self.class_entries.append(credit_entry)
                
                grade_label = Label(frame, text="Select Grade:")
                grade_label.pack(side=LEFT)
                grade_var = StringVar(frame)
                grade_var.set("A")
                grade_menu = OptionMenu(frame, grade_var, "A", "B", "C", "D", "F")
                grade_menu.pack(side=LEFT, padx=5)
                self.grade_vars.append(grade_var)
        except ValueError:
            self.result_label.config(text="Please enter a valid number of classes.")

    def calculate_gpa(self):
        try:
            hours = float(self.hours_entry.get())
            cumulative_gpa = float(self.gpa_entry.get())
            total_new_quality_points = cumulative_gpa * hours
            total_new_hours = hours

            grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

            for credit_entry, grade_var in zip(self.class_entries, self.grade_vars):
                credit_hours = float(credit_entry.get())
                grade = grade_var.get()
                total_new_quality_points += grade_points[grade] * credit_hours
                total_new_hours += credit_hours

            new_gpa = total_new_quality_points / total_new_hours
            self.result_label.config(text=f"New GPA: {new_gpa:.2f}")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers for all fields.")

if __name__ == "__main__":
    app = GPACalculator()
    app.mainloop()

