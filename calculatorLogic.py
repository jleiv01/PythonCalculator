'''
Created on Oct 19, 2021
First Python Code
@author: Jose
'''

operation = input(''' 
Please type in the desired operation: 
+ addition
- subtraction
/ division
* multiplication
''')

if operation == '*':
    print('You have selected multiplication')
    
elif operation == '+':
    print('You have selected addition')
    
elif operation == '-':
    print('You have selected Subtraction')
    
elif operation == "/":
    print('You have selected Division')
    
else:
    print('''Something is wrong with your input, 
    exiting program.......''')