# Remove doubles from a rate list

rateList = open("rate-list-with-doubles.txt", "r")

lines = rateList.readlines()

linesWithoutDoubles = list(dict.fromkeys(lines))

cleanedRateList = open("rate-list-clean.txt", "w")

for line in linesWithoutDoubles:
    print(line)
    cleanedRateList.write(line)

cleanedRateList.close()