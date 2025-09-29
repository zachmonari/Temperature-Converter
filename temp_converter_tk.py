import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import csv

# conversion functions
def celsius_to_fahrenheit(c): return (c * 9/5) + 32
def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def celsius_to_kelvin(c): return c + 273.15
def kelvin_to_celsius(k): return k - 273.15
def fahrenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15
def kelvin_to_fahrenheit(k): return (k - 273.15) * 9/5 + 32

CONVERSIONS = {
    "Celsius → Fahrenheit": lambda v: celsius_to_fahrenheit(v),
    "Fahrenheit → Celsius": lambda v: fahrenheit_to_celsius(v),
    "Celsius → Kelvin": lambda v: celsius_to_kelvin(v),
    "Kelvin → Celsius": lambda v: kelvin_to_celsius(v),
    "Fahrenheit → Kelvin": lambda v: fahrenheit_to_kelvin(v),
    "Kelvin → Fahrenheit": lambda v: kelvin_to_fahrenheit(v),
}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🌡️ Temperature Converter")
        self.geometry("520x400")
        self.resizable(False, False)

        # widgets
        self.option = tk.StringVar(value=list(CONVERSIONS.keys())[0])
        ttk.Label(self, text="Conversion:").place(x=20, y=20)
        ttk.Combobox(self, textvariable=self.option, values=list(CONVERSIONS.keys()), state="readonly", width=30).place(x=110, y=20)

        ttk.Label(self, text="Temperature:").place(x=20, y=60)
        self.temp_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.temp_var, width=20).place(x=110, y=60)

        ttk.Button(self, text="Convert", command=self.convert).place(x=350, y=55)
        ttk.Button(self, text="Save Log...", command=self.save_log).place(x=420, y=55)

        ttk.Label(self, text="Result:").place(x=20, y=100)
        self.result_label = ttk.Label(self, text="", font=("Segoe UI", 10, "bold"))
        self.result_label.place(x=110, y=100)

        ttk.Label(self, text="History:").place(x=20, y=140)
        self.history_list = tk.Listbox(self, width=70, height=10)
        self.history_list.place(x=20, y=165)

        ttk.Button(self, text="Clear History", command=self.clear_history).place(x=20, y=350)
        ttk.Button(self, text="Quit", command=self.quit).place(x=450, y=350)

        self.log = []

    def convert(self):
        try:
            value = float(self.temp_var.get())
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid number.")
            return

        conv_name = self.option.get()
        result = CONVERSIONS[conv_name](value)
        # format output with units inferred from name
        left_unit, right_unit = conv_name.split(" → ")
        # create message with 2 decimal places
        msg = f"{value:g}{left_unit[0]} → {result:.2f}{right_unit[0]}"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} — {msg}"
        self.log.append((timestamp, msg))
        self.history_list.insert(tk.END, entry)
        self.result_label.config(text=msg)

    def save_log(self):
        if not self.log:
            messagebox.showinfo("No data", "History is empty — nothing to save.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files","*.csv"),("All files","*.*")])
        if not path:
            return
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "conversion"])
                for ts, msg in self.log:
                    writer.writerow([ts, msg])
            messagebox.showinfo("Saved", f"Log saved to {path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")

    def clear_history(self):
        if messagebox.askyesno("Clear history", "Clear all history?"):
            self.log.clear()
            self.history_list.delete(0, tk.END)
            self.result_label.config(text="")

if __name__ == "__main__":
    App().mainloop()
