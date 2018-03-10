import time
import os

os.system('mode con: cols=60 lines=23')  # This instruction is to set the cmd windows to the good dimensions
Pomodoro = "      ____                            __                \n     / __ \____  ____ ___  ____  ____/ /___  _________  \n    / /_/ / __ \/ __ `__ \/ __ \/ __  / __ \/ ___/ __ \ \n   / ____/ /_/ / / / / / / /_/ / /_/ / /_/ / /  / /_/ / \n  /_/    \____/_/ /_/ /_/\____/\__,_/\____/_/   \____/ \n\n              _______                              \n             /_  __(_)___ ___  ___  _____          \n              / / / / __ `__ \/ _ \/ ___/          \n             / / / / / / / / /  __/ /              \n            /_/ /_/_/ /_/ /_/\___/_/               \n\n\n"

print(Pomodoro)

inputIsNumber = False
while not inputIsNumber:
    try:
        work = round(float(input("Select your work time (minutes) : ")) * 60)
        pause = round(float(input("            break time (minutes) : ")) * 60)
        inputIsNumber = True
    except ValueError:
        print("Durée invalide.")


ASCI_art = {1: ["   ██╗      ",
                "  ███║      ",
                "  ╚██║      ",
                "   ██║      ",
                "   ██║      ",
                "   ╚═╝      "],
            2: ["██████╗     ",
                "╚════██╗    ",
                " █████╔╝    ",
                "██╔═══╝     ",
                "███████╗    ",
                "╚══════╝    "],
            3: ["██████╗     ",
                "╚════██╗    ",
                " █████╔╝    ",
                " ╚═══██╗    ",
                "██████╔╝    ",
                "╚═════╝     "],
            4: ["██╗  ██╗    ",
                "██║  ██║    ",
                "███████║    ",
                "╚════██║    ",
                "     ██║    ",
                "     ╚═╝    "],
            5: ["███████╗    ",
                "██╔════╝    ",
                "███████╗    ",
                "╚════██║    ",
                "███████║    ",
                "╚══════╝    "],
            6: [" ██████╗    ",
                "██╔════╝    ",
                "███████╗    ",
                "██╔═══██╗   ",
                "╚██████╔╝   ",
                " ╚═════╝    "],
            7: ["███████╗    ",
                "╚════██║    ",
                "    ██╔╝    ",
                "   ██╔╝     ",
                "   ██║      ",
                "   ╚═╝      "],
            8: ["  █████╗    ",
                " ██╔══██╗   ",
                " ╚█████╔╝   ",
                " ██╔══██╗   ",
                " ╚█████╔╝   ",
                "  ╚════╝    "],
            9: [" █████╗     ",
                "██╔══██╗    ",
                "╚██████║    ",
                " ╚═══██║    ",
                " █████╔╝    ",
                " ╚════╝     "],
            0: [" ██████╗    ",
                "██╔═████╗   ",
                "██║██╔██║   ",
                "████╔╝██║   ",
                "╚██████╔╝   ",
                " ╚═════╝    "],
            10: ["       ",
                 "██╗    ",
                 "╚═╝    ",
                 "██╗    ",
                 "╚═╝    ",
                 "       "]}


def sommeur(a, b):  # given two numbers a & b, returns the ASCI art of the number a*10 + b
    a = ASCI_art[a]
    b = ASCI_art[b]
    c = [a[i] + b[i] for i in range(6)]
    return c


def horaire(d):  # Given a number of seconds d, returns the ASCII art of the time of d seconds with format mm:ss
    a_min, b_min = (d // 60) // 10, (d // 60) % 10
    a_sec, b_sec = (d % 60) // 10, (d % 60) % 10
    c_min, c_sec = sommeur(a_min, b_min), sommeur(a_sec, b_sec)
    c = ["   " + c_min[i] + ASCI_art[10][i] + c_sec[i] for i in range(6)]
    return c


def timer():
    a = work
    b = pause
    while a > 0:
        map(print, horaire(a))
        c = horaire(a)
        print(Pomodoro)
        for i in range(6):
            print(horaire(a)[i])
        print("                          W O R K \n")
        time.sleep(1 - 0.004)  # My functions took 0.004 seconds per loop to execute
        a -= 1
    while b > 0:
        c = horaire(b)
        print(Pomodoro)
        for i in range(6):
            print(horaire(b)[i])
        print("                         B R E A K \n")
        time.sleep(1 - 0.004)
        b -= 1
    return


while(1):
    timer()
