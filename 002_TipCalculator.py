print('Welcome to the tip calculator')
bill =float(input('What was the total bill? $'))
tip_percent = int(input('What percentage tip would you like to give? 10,12 or 15?'))
people_num = int(input('How many people to split the bill?'))

total = bill + ((bill * tip_percent)/100)
print(f'Each person should pay: ${round(total/people_num,2)}')