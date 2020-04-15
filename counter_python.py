import time

time1 = 0
for time1 in range(1, 50, 1):
    print(time1, sep=' ', end=' ', flush=True)
    time.sleep(1)
    time1 += 1
