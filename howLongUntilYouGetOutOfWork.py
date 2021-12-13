# this program will countdown until you get off work/ school

from datetime import datetime

now = datetime.now() # gets date/ time in the following format: 2021-05-06 13:36:49.706922
currentTime = now.strftime("%H:%M:%S") # converts time to a string in the following format hh:mm:ss

currentHour = int(currentTime[0] + currentTime[1])
currentMinute = int(currentTime[3] + currentTime[4])
currentSecond = int (currentTime[6] + currentTime[7])

print ("Current time : %d:%d:%d" % (currentHour, currentMinute, currentSecond))

#selection = int(input("Select from the following menu:\n 1 : how much time until I get off work\n 2 : how much time until I get out of school"))


thenTime = input("What time do you get off work ? (in standard time hh/mm)")

amOrPm = str(input ("Press 1 for AM\n Press 2 for PM "))
while (amOrPm != '1' and amOrPm != '2'):
    amOrPm = str(input ("Press 1 for AM\n Press 2 for PM "))

thenHour = int(thenTime[0] + thenTime[1]) # extracts hour and converts to int
thenMinute = int (thenTime[3] + thenTime[4]) # extracts minhte and converts to in


print ("Time to get off work in standard time : %d: %d " % (thenHour, thenMinute)) # in standard time

if amOrPm == '2':
    thenHour += 12 # converts into military time 

print ("Time to get off work in military time : %d: %d " % (thenHour, thenMinute)) # now in military time

secondsUntil = 60 - currentSecond # get seconds until

if (thenMinute > currentSecond):  # get minutes until
    minutesUntil = thenMinute - currentSecond
if (thenMinute < currentSecond):
    hoursUntil = -1
    minutesUntil = (60 + thenMinute) - currentMinute

hoursUntil += (thenHour  - currentHour) # get hours until

print ("This is how long until you get out : %d:%d:%d " % (hoursUntil, minutesUntil, secondsUntil))



