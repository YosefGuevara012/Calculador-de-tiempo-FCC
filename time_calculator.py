def add_time(start, duration):

    days_of_the_week = ["sunday","monday","tuesday","wednesday","thursday","friday","satruday"]
  
    initial_time = start.split()
    start_hour = initial_time[0].split(":")
    duration_time = duration.split(":")
    period = initial_time[1]

    # time operatio// 

    number_of_days =  int(duration_time[0]) // 24 
    number_of_hours = int(duration_time[0]) % 24 

    minutes = int(start_hour[1])+ int(duration_time[1])
    hours = int(start_hour[0]) + number_of_hours

    print(number_of_days)
    print(number_of_hours)

    if minutes >= 60:
      hours+=1
      minutes = minutes - 60

    if minutes < 10:
        minutes = "0"+ str(minutes)
      

    if hours > 12 and period == "PM":
      hours = hours - 12
      period = "AM"
    elif hours > 12 and period == "AM":
      hours = hours - 12
      period = "PM"

    new_time = str(hours)+":"+ str(minutes) +" "+ period

    return new_time