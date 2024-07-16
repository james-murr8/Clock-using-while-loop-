import time 

t0 = time.time()

hour = 0
mins = 0
secs = 0
 
while (hour < 24):
    mins = 0

    while (mins < 60):
        secs = 0
        
        while (secs < 60):
            
            print(f"Hour: {hour}, Mins: {mins}, Secs: {secs}")

            secs += 1

        mins += 1

    hour += 1
            
t1 = time.time()

total = t1-t0
print(f"Total execution time: {total} seconds")
