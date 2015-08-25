# Lesson 1 in Programming Foundations with Python (Udacity)

import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while break_count < total_breaks:
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=TRJYCW_dCN4")
	break_count += 1
