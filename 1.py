import sys

f = open("log.txt", "r")

logList = f.readlines()
timeout = 0
for data in logList:
    day,address,response = data.split(",")
    if response == "-\n" :
        timeout = 1
        errBegin = day
    if (timeout == 1) & (response != '-\n'):
        print(errBegin + ' ~ ' + day)
        timeout = 0
        sys.exit()
f.close()
print("error not found")