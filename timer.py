import time


good = False

duration = input("Enter duration of the timer in mm:ss \n")
while not good:
    if duration.find(':') == 2 and len(duration) == 5:
        durationSec = duration[3:]
        durationMin = duration[0:2]
        secIsInt = bool((57 >= ord(durationSec[0:1]) >= 48) and (57 >= ord(durationSec[1:2]) >= 48))
        minIsInt = bool((57 >= ord(durationMin[0:1]) >= 48) and (57 >= ord(durationMin[1:2]) >= 48))
        if secIsInt and minIsInt:
            print("INTS EVERYWHERE!")
            if int(durationSec) < 60:
                good = True
    if not good:
        print("Invalid input. Make sure to use mm:ss, like so: 05:30 -> 5 mins, 30 seconds \n")
        duration = input("Enter duration of the timer in mm:ss \n")

durationSec = int(duration[3:])
durationMin = int(duration[0:2])


print("Got it!")

print("Writing to the text file...")

while durationMin != 0 or durationSec != 0:
    durationSec -= 1
    time.sleep(1)
    f = open('countdown.txt', 'w')
    f.write(str(durationMin) + ':' + '{:02}'.format(durationSec))


    if durationSec == 0 and durationMin != 0:
        durationMin -= 1
        durationSec = 60

f.close()
