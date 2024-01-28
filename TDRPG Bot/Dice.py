import random
import codes

#Takes the string input from the command and converts it into the total rolled value in a string 
def dice(input):
    input = input.replace(codes.prefix + 'r','')
    input = input.replace(codes.prefix + 'roll','')
    input = input.replace(' ','')
    output = "Your roll is: "
    if input.find('+') > -1 or input.find('-') > -1:
        output += str(multiroll(input))
    else:
        output += str(roll(input))

    return output

#Rolls a single type of dice
def roll(input):
    try:
        output = 0 
        n = 1
        d_index = input.find('d')
        num = int(input[:(d_index)])
        value = int(input[(d_index + 1):(len(input)+1)])

        while n <= num:
            output += random.randint(1,value)
            n+=1
    

    return output

#Takes a string of multiple rolls and seperates them
def multiroll(input):

    a = True
    total = 0
    output =''
    input = '+' + input
    rolls = []

    while a == True:
        print(input)
        plus_index = input.find('+')
        minus_index = input.find('-')

        if plus_index == 0:
            mult = 1
        elif minus_index == 0:
            mult = -1
        
        input = input[1:len(input)+1]
        print(input)
        plus_index = input.find('+')
        minus_index = input.find('-')

        if plus_index == -1 and minus_index == -1:
            index = len(input)+1
            a = False
        elif (plus_index > -1 and minus_index == -1) or (plus_index > -1 and minus_index > -1 and plus_index < minus_index):
            index = plus_index
        elif (plus_index == -1 and minus_index > -1) or (plus_index > -1 and minus_index > -1 and minus_index < plus_index):
            index = minus_index
        
        print(input[0:index])
        rolls.append(roll(input[0:index])*mult)
        input = input[index:len(input)]


    for x in rolls:
        total += x
        if x > 1:
            output += str(x) + ' + '
        else:
            output = output[0:len(output)-2]
            output+= '- ' + str(abs(x)) + '  '

    return(output[0:len(output) - 2] + ' = ' + str(total))

