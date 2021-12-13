# this program will countdown until you get off work/ school

from datetime import datetime

now = datetime.now() # gets date/ time in the following format: 2021-05-06 13:36:49.706922
currentTime = now.strftime("%H:%M:%S") # converts time to a string in the following format hh:mm:ss

currentHour = int(currentTime[0] + currentTime[1])
currentMinute = int(currentTime[3] + currentTime[4])
currentSecond = int (currentTime[6] + currentTime[7])

print ("Current time : %d:%d:%d" % (currentHour, currentMinute, currentSecond))


thenTime = input("What time do you get off work ? (in standard time hh/mm)")

amOrPm = str(input ("Press 1 for AM\n Press 2 for PM "))
while (amOrPm != '1' and amOrPm != '2'):
    amOrPm = str(input ("Press 1 for AM\n Press 2 for PM "))

thenHour = int(thenTime[0] + thenTime[1]) # extracts hour and converts to int
thenMinute = int (thenTime[3] + thenTime[4]) # extracts minhte and converts to in


print ("Time to get off work in standard time : %d: %d " % (thenHour, thenMinute)) # in standard time

if amOrPm == '2':
    thenHour += 12 # converts into military time 



def todayCountDown(thenHour, thenMinute):
    secondsUntil = 60 - currentSecond # get seconds until
    hoursUntil = 0
    if (thenMinute > currentMinute):  # get minutes until
        minutesUntil = thenMinute - currentSecond
    if (thenMinute == currentMinute):
        minutesUntil = 0
    if (thenMinute < currentMinute):
        hoursUntil = -1
        minutesUntil = (60 + thenMinute) - currentMinute

    
    hoursUntil += (thenHour  - currentHour) # get hours until

    print ("You get off of work in :\n%d hours\n%d minutes\n%d seconds" % (hoursUntil, minutesUntil, secondsUntil))

    
todayCountDown(thenHour, thenMinute)





