from datetime import datetime

now = datetime.now()
dt_string = now.strftime("_%H:%M_%d_%m_%Y")

print(dt_string)