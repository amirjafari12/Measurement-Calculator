print("Welcome to the Measurement Calculator\n\r")
print("Celsius in Fahrenheit\n\rFahrenheit in Celsius\n\rinch in cm\n\rcm in inch\n\rft in m\n\rm in ft\n\r")
selection = input("Chose which calculator do you want: ")


def C_F():
    C = float(input("Please enter one degree Celsius: "))
    F = C * 1.8 + 32
    print(f"Fahrenheit = {F}")

def F_C():
    F = float(input("Please enter one degree Fahrenheit: "))
    C = (F - 32) * 5/9
    print(f"Celsius = {C}")

def inch_cm():
    inch = float(input("Please enter a inch size: "))
    cm = inch * 2.54
    print(f"Centimeter = {cm}")

def cm_inch():
    cm = float(input("Please enter a cm size: "))
    inch = cm / 2.54
    print(f"Inch = {inch}")

def ft_m():
    ft = float(input("Please enter a foot size: "))
    m = ft * 0.3048
    print(f"Meter = {m}")

def m_ft():
    m = float(input("Please enter a meter size: "))
    ft = m / 0.3048
    print(f"Foot = {ft}")


if selection == "Celsius in Fahrenheit":
    print("You choose the calculator for Celsius in Fahrenheit")
    C_F()

elif selection == "Fahrenheit in Celsius":
    print("You choose the calculator for Fahrenheit in Celsius")
    F_C()

elif selection == "inch in cm":
    print("You choose the calculator for inch in cm")
    inch_cm()

elif selection == "cm in inch":
    print("You choose the calculator for cm in inch")
    cm_inch()

elif selection == "ft in m":
    print("You choose the calculator for ft in m")
    ft_m()

elif selection == "m in ft":
    print("You choose the calculator for m in ft")
    m_ft()

else:
    print("input invalid")
