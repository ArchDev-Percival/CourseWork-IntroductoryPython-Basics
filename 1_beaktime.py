import time
import webbrowser

break_count = 0
total_breaks = 10

print ("The current time is: "+time.ctime())
while (break_count < total_breaks):
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=PU5xxh5UX4U",2)
    break_count = break_count + 1

