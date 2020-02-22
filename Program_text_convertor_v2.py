# -*- coding: utf-8 -*-
"""
This program converts text.
User is asked to enter string.
User is asked to select either reverse or capitalize option. Select right option otherwise program does not convert text.
User can convert another text if wants.
"""
import time

def converter(option,input_string):
    '''This function   '''
    if option == "B":
        capitalized_string = input_string.upper()
        print("B) Capitalized string:\n" + capitalized_string)
        time.sleep(2)
    elif option == "A":
        reversed_string = "".join(reversed(input_string))
        print("A) Reversed string:\n" + reversed_string)
    elif option == "C":
        reversed_string = "".join(reversed(input_string))
        capitalized_string = input_string.upper()
        print("A) Reversed string:\n" + reversed_string +"\n" + "B) Capitalized string:\n" + capitalized_string)        
        time.sleep(2)
    else:   
        print("You entered wrong letter just A and B is accepted!")
        time.sleep(2)
        
counter = "Y"
while counter == "Y":
    input_string = input('Enter a string:')
    option = input("What do you want to do with text? You can either reverse (press A), capitalize (press B) or both (press C):\n").upper()
    converter(option,input_string)
    counter = input("Do you want to convert another string? Press Y if so, otherwise press anything else:\n").upper()
else:
    print("We are finished!")
    