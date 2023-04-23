import sys

f = open("log.txt", "r")
n = int(input())

logList = f.readlines()
cnt = 0
for data in logList:
    day,address,response = data.split(",")
    if response == "-\n" :
        cnt += 1
        errBegin = day
    if (cnt >= n) & (response != '-\n'):
        print(errBegin + ' ~ ' + day)
        sys.exit()

f.close()
print("error not found")