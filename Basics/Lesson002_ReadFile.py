# Read a file and print each line

rateList = open("rate-list-with-doubles.txt", "r")

lines = rateList.readlines()

for line in lines:
    print(line)

