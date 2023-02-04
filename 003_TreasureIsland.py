print('Welcome to treasure island. Your mission is to find the treasure.')
choice = input('Left or right?').lower()
result = 'Game Over'
if choice == 'left':
    choice = input('Swim or wait?').lower()
    if choice == 'wait':
        choice = input('Which door? Red,Blue or Yellow?').lower()
        if choice== 'yellow':
            result = 'You Win!'
print(result)