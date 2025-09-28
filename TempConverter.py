def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(temp):
    return (temp - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def print_menu():
    print("\n🌡️ Temperature Converter")
    print("Choose a conversion:")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Celsius to Kelvin")
    print("4: Kelvin to Celsius")
    print("5: Fahrenheit to Kelvin")
    print("6: Kelvin to Fahrenheit")
    print("Q: Quit and show log")

# Store results
conversion_log = []

while True:
    print_menu()
    choice = input("Enter your choice (1-6 or Q): ").strip().lower()

    if choice == 'q':
        break

    if choice not in {'1', '2', '3', '4', '5', '6'}:
        print("❌ Invalid choice. Try again.")
        continue

    try:
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        msg = "{}°C → {:.2f}°F".format(temp, result)
    elif choice == "2":
        result = fahrenheit_to_celsius(temp)
        msg = "{}°F → {:.2f}°C".format(temp, result)
    elif choice == "3":
        result = celsius_to_kelvin(temp)
        msg = "{}°C → {:.2f}K".format(temp, result)
    elif choice == "4":
        result = kelvin_to_celsius(temp)
        msg = "{}K → {:.2f}°C".format(temp, result)
    elif choice == "5":
        result = fahrenheit_to_kelvin(temp)
        msg = "{}°F → {:.2f}K".format(temp, result)
    elif choice == "6":
        result = kelvin_to_fahrenheit(temp)
        msg = "{}K → {:.2f}°F".format(temp, result)

    print("✅ Conversion Result:", msg)
    conversion_log.append(msg)

# Show all conversions
print("\n📝 Your Conversion Log:")
for i, entry in enumerate(conversion_log, start=1):
    print("{}. {}".format(i, entry))

print("\nThanks for using the Temperature Converter! 🌡️")