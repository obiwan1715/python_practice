# this code checks to see if a year is a leap year

#ask user to input year as string

year = raw_input('To check if a year is a leap year, please enter the year now: ')

#convert string into an integer

year = int(year)

#check if year is divisible by 4 and return print string accordingly

if year % 4 == 0:
	print "Yes," ,year, "was a leap year"

else:
	print "No," ,year, "was NOT a leap year"

