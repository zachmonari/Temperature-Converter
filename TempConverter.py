import csv
from datetime import datetime
import os

def celsius_to_fahrenheit(c): return (c * 9/5) + 32
def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def celsius_to_kelvin(c): return c + 273.15
def kelvin_to_celsius(k): return k - 273.15
def fahrenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15
def kelvin_to_fahrenheit(k): return (k - 273.15) * 9/5 + 32

def print_menu():
    print("\n🌡️ Temperature Converter")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Celsius to Kelvin")
    print("4: Kelvin to Celsius")
    print("5: Fahrenheit to Kelvin")
    print("6: Kelvin to Fahrenheit")
    print("S: Save history to file")
    print("L: Load history from file")
    print("Q: Quit and show log\n")

conversion_log = []
DEFAULT_HISTORY = "conversion_history.csv"

def save_to_file(path=DEFAULT_HISTORY):
    if not conversion_log:
        print("No conversions to save.")
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "conversion"])
        for ts, msg in conversion_log:
            writer.writerow([ts, msg])
    print(f"Saved {len(conversion_log)} entries to {path}")

def load_from_file(path=DEFAULT_HISTORY):
    if not os.path.exists(path):
        print(f"No file at {path}")
        return
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        loaded = 0
        for row in reader:
            conversion_log.append((row["timestamp"], row["conversion"]))
            loaded += 1
    print(f"Loaded {loaded} entries from {path}")

while True:
    print_menu()
    choice = input("Enter choice: ").strip().lower()
    if choice == "q":
        break
    if choice == "s":
        save_to_file()
        continue
    if choice == "l":
        load_from_file()
        continue
    if choice not in {'1','2','3','4','5','6'}:
        print("Invalid choice, try again.")
        continue
    try:
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice == "1":
        result = celsius_to_fahrenheit(temp); msg = f"{temp}°C → {result:.2f}°F"
    elif choice == "2":
        result = fahrenheit_to_celsius(temp); msg = f"{temp}°F → {result:.2f}°C"
    elif choice == "3":
        result = celsius_to_kelvin(temp); msg = f"{temp}°C → {result:.2f}K"
    elif choice == "4":
        result = kelvin_to_celsius(temp); msg = f"{temp}K → {result:.2f}°C"
    elif choice == "5":
        result = fahrenheit_to_kelvin(temp); msg = f"{temp}°F → {result:.2f}K"
    elif choice == "6":
        result = kelvin_to_fahrenheit(temp); msg = f"{temp}K → {result:.2f}°F"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversion_log.append((timestamp, msg))
    print("Result:", msg)

print("\nConversion log:")
for i, (ts, entry) in enumerate(conversion_log, 1):
    print(f"{i}. {ts} — {entry}")
print("Goodbye!")
