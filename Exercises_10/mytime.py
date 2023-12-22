from datetime import datetime as dt

current_datetime = dt.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)


