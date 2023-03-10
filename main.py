import sys
from datetime import datetime
from math import pi
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("""
    Twinkle, twinkle, little star, 
        How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky. 
        Twinkle, twinkle, little star, 
            How I wonder what you are!""")
    print(sys.version)
    print(sys.version_info)
    teraz = datetime.now()
    print("Obecna data i czas")
    data = teraz.strftime("%Y/%M/%D" + "  " + "%H:%M:%S")
    print(data)
    r = float(input("Podaj r kola"))
    print("obwod kola wynosi " + str(pi*r**2))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Początek
