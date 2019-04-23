from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H%M%S")
f = open( current_time + ".txt", "w+")
f.close()