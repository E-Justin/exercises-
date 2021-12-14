# this program will give you the time until _____ ( a certain date)

from datetime import datetime
now = datetime.now()



currentTime = now.strftime("%m/%d/%Y, %H:%M:%S")

currentMonth = int(currentTime[0] + currentTime[1])
currentDay = int(currentTime[3] + currentTime[4])
currentYear = int(currentTime[6] + currentTime[7] + currentTime[8] + currentTime[9])
#currentHour = int(currentTime[12] + currentTime[13])
#currentMinute = int(currentTime[15] + currentTime[16])
#currentSecond = int(currentTime[18] + currentTime[19])

#print("Current time/ date :")
#print ("Month : %d " % currentMonth)
#print ("Day : %d " % currentDay)
#print ("Year : %d " % currentYear)
#print( "Hour : %d " % currentHour)
#print ("Minute : %d " % currentMinute)
#print ("Second : %d " % currentSecond)

daysInAYear = 365
monthsInAYear = 12
hoursInADay = 24

daysUntil = 0
yearsUntil = 0
monthsUntil = 0

daysFebLeap = 29#2L


daysInAMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


#print(currentTime)
# 12/14/2021, 06:28:49
# 01234567890123456789

targetTime = input("What is the date that you would like to countdown to (mm/dd/yyyy")
#targetOccasion = str(input("What is the occasion or name of the holdiay?"))

#print("Target time : %s" % targetTime)
# 12/25/2021
# 0123456789
targetMonth = int(targetTime[0] + targetTime[1])
targetDay = int(targetTime[3] + targetTime[4])
targetYear = int(targetTime[6] + targetTime[7] + targetTime[8] + targetTime[9])
#print("Target month : %d " % targetMonth)
#print("Target day : %d " % targetDay)
#print("Target year : %d " % targetYear)

if targetDay > currentDay: # if the target day is greater than the day today
    daysUntil = targetDay - currentDay
elif targetDay < currentDay:
    daysInThisMonth = daysInAMonth[currentMonth -1]
    daysUntil = daysInThisMonth - currentDay + targetDay
    monthsUntil = -1

if targetMonth != currentMonth: # if months are different
    if targetMonth > currentMonth: # if target month is greater than current month
        monthsUntil = targetMonth - currentMonth
    elif targetMonth < currentMonth: # if target month is less than current month
        monthsUntil += (12 - currentMonth) + targetMonth

print("~~~~~~~~~~ Time until %s ~~~~~~~~~~" )
print("Years  : %d" % yearsUntil)
print("Months : %d" % monthsUntil)
print("Days   : %d" % daysUntil)
#print("Hours  : %d" % hoursUntil)
#print("Minutes: %d" % minutesUntil)
#print("Seconds: %d" % secondsUntil)
