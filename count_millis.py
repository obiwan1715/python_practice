import time

start = time.time()
for x in range (0,1001):
	print x
end = time.time()
print("That took " + str(end-start) + " seconds to print, which is really fast.")
