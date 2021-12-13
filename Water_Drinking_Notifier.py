import time
import plyer
import pyttsx3
from plyer import notification

i = 0

try:
    time_Interval = int(input("How much time gap do you need ? In minutes... : "))
    count = int(input("How much times do you want this notification ? : "))
except:
    print("Enter a integer!")
    exit()

while count > i:
    notification.notify(
        title = "Drink water!",
        message = "It's time to drink or else may I ask your father to throw a shoe towards you ?"
    )
    pyttsx3.speak("Drink water I said. Can't you understand Duffer!"),
    time.sleep(time_Interval*60)
    i = i+1
    