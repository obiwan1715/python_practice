tm = open('eu_refugee_plan.txt', 'r')
for line in tm:
	line = line.strip()
	line = line.translate(None, '!@#$%^&*()_+=-,.<>/?;:"[]\{}|`~')
	line = line.lower()
	list = line.split(' ')
	print list

