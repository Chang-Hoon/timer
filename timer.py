from datetime import date
import time
import math


now = date.today()
msg = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# print(msg)


mins = input("How long (in minute)? > ")
mins = math.ceil(int(mins))

INTERVAL = 10.0
count = 0

max_count = math.ceil(mins * 60 / INTERVAL / 2) 
elapsed = 0
secs = 0
signs = ['+', '-']
ix = 0

while (elapsed / 60) <= mins:
    while secs <= INTERVAL:
        print('\r [{:03d}/{:03d}] {:s} {:04.1f}/{:.1f}...'.format(count+1, max_count, signs[ix], secs, INTERVAL), end='')
        # Sleep for a second
        time.sleep(0.1)
        secs += 0.1

    elapsed += secs
    ix ^= 1 # Toggle the sign
    secs = 0
    # Count if the sign become '+'
    if ix == 0:
        count += 1
        print('\r [{:03d}/{:03d}] Done.      \n'.format(count, max_count), end='')
# print('\r [{:03d}/{:03d}] Done.      \n'.format(count, max_count), end='')
print('\n\r%d times for %dm (%dsec)' %(count, elapsed/60, elapsed))