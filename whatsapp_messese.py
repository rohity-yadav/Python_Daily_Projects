import datetime
import pywhatkit as kit

now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 1  # 

kit.sendwhatmsg("+918007937274", "Hello! This is an automated message", hour, minute)
