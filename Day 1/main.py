digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
chardig = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digmap =  {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
ans = 0

with open('g:/Programmering/Python/Advent of code/Day 1/input.txt', 'r') as file:
    for line in file:
        first = ""
        last = ""
        #Find first and last digits, could be done faster by going backwards to find last digit.
        for i in range(len(line)):
            if(line[i] in digits):
                if(first == ""):
                    first = line[i]
                last = line[i]
            else:
                for j in range(1, 6):
                    if(line[i:i+j] in chardig):
                        tmp = digmap[line[i:i+j]]
                        if (first == ""):
                            first = tmp
                        last = tmp
        ans += int(first+last)

print(ans)