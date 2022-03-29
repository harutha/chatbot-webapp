import time
import os
chickens_per_year = 50000000000

seconds_per_year = 60 * 60 * 24 * 52

chickens_per_second = chickens_per_year / seconds_per_year

print(chickens_per_second)

total = chickens_per_year / seconds_per_year
running_total = 0
def chickens_killed():
    global running_total
    while True: 
        running_total += total
        # time.sleep(1)
        print(running_total)
        time.sleep(1)
        os.system('cls')
        if running_total > chickens_per_year:
            break
        return running_total

chickens_killed()