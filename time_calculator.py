def add_time(start, duration, day="None"):

    # Creates a list with the days
    days_of_the_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    # takes the argument day and create a lower case string
    day_of_the_week = day.casefold()
    
    # process the information from the arguments by dividing each string
    initial_time = start.split()
    start_hour = initial_time[0].split(":")
    duration_time = duration.split(":")
    period = initial_time[1]
    
    # time operations// 

    # caculate the amount of day from the given hours
    number_of_days =  int(duration_time[0]) // 24 
    # caculate the amount of hours to add from the given hours
    number_of_hours = int(duration_time[0]) % 24 
    # calculates the number of week from the calculated days
    number_of_weeks = number_of_days // 7
    # calculates the numer of days to add
    number_of_days = number_of_days % 7
    

    # Calculates the final result of the minutes
    minutes = int(start_hour[1])+ int(duration_time[1])
    # Calculates the final result of the hours
    hours = int(start_hour[0]) + number_of_hours

    # if the number of minutes > 60 adds an adicional hour
    if minutes >= 60:
      hours+=1
      minutes = minutes - 60
    
    # if the number of minutes < 10 adds an 0 to the time minutes str

    if minutes < 10:
        minutes = "0"+ str(minutes)
      
    # analize if the hours are > than 12 to set the period of the day  

    if hours >= 12 and period == "PM":
      hours = hours - 12
      period = "AM"
      

    elif hours >= 12 and period == "AM":
      hours = hours - 12
      period = "PM"

    if hours == 0:
      hours = 12
    
      
      
    day_identifier = 0

    for i in range(len(days_of_the_week)):
      if days_of_the_week[i].casefold() == day_of_the_week:
        day_identifier = i+1
    
    #print("day_identifier " + str(day_identifier))

    day_identifier += number_of_days
    #print("day_identifier += number_of_days " + str(day_identifier))

    
    
    if number_of_days == 0 :
      day_identifier -= 1
    elif day_identifier >= 7:
      number_of_weeks += 1
      day_identifier = day_identifier % 7
    
    

    #print("day_identifier " + str(day_identifier))
    
    
    if number_of_days == 0 and day_of_the_week != "none" : 
      new_time = str(hours)+":"+ str(minutes) +" "+ period+" "+ days_of_the_week[day_identifier]

    elif number_of_days > 0 and day_of_the_week == "none" : 

      if number_of_days == 1:
        new_time = str(hours)+":"+ str(minutes) +" "+ period+" (next day)" 
      else:  
        new_time = str(hours)+":"+ str(minutes) +" "+ period+" ("+ str(number_of_days + 7*number_of_weeks) + " days later)"

    elif day_of_the_week == "none":
      new_time = str(hours)+":"+ str(minutes) +" "+ period
    else:
      new_time = str(hours)+":"+ str(minutes) +" "+ period+", "+ days_of_the_week[day_identifier] + " ("+ str(number_of_days + 7*number_of_weeks) + " days later)"


  
    return new_time