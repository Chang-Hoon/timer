from datetime import date
import time


now = date.today()
msg = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# print(msg)


mins = input("How long (in min)? >")
mins = int(mins)

INTERVAL = 10
count = 0
elapsed = 0
secs = 0
signs = ['+', '-']
ix = 0


while (elapsed / 60) <= mins:
    while secs != INTERVAL:
        # Sleep for a second
        time.sleep(1)
        secs += 1
        print('\r %s %02d/%d' % (signs[ix], secs, INTERVAL), end='')
    elapsed += secs
    ix ^= 1 # Toggle the sign
    secs = 0
    count += 1

print('\n\r%dtimes for %dm (%dsec)' %(count/2, elapsed/60, elapsed))