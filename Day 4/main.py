with open('g:/Programmering/Python/Advent of code/Day 4/input.txt', 'r') as file:
    i = 0
    cards = [1]*218
    for line in file:
        line = line[line.find(':') + 1:]
        line = line.split("|")
        winningNumbers = []
        for winningNumber in line[0].strip().split():
            winningNumbers.append(winningNumber.lstrip())
        
        #Check for winning numbers
        c = 0
        for ownNumber in line[1].strip().split():
            if ownNumber.lstrip() in winningNumbers and ownNumber != " ":
                c += 1

        #Add the won cards to list
        for j in range(c):
            cards[i+j+1] += cards[i]
        i += 1

print(sum(cards))