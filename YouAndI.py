import sys
import time
replay = "blank"

print("You are a soldier. Or at least, you were once. But you have long since retired.")
print("Now, your village has recently been attacked by a fearsome beast. It's up to you to slay it.")
print("The blacksmith has already prepared a sword for you, all you need to do now, is wake up.")
print()
print("\033[1m" + "You and I" + "\033[0m")
print()
while replay != "yes" or replay != "Yes":
    print("As the sun rises, the light slowly creeps in through your curtains to brighten up your room. You wake up.")
    print("Today is the day of your departure. You should get going.")
    print("a) Get up")
    print("b) Stay in bed")
    getup = input()
    if getup == "a" or getup == "A" or getup == "a)":
        getup = True
        print("Good")
    elif getup == "b" or getup == "B" or getup == "b)":
        getup = False
        print("Bad")