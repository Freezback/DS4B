# -*- coding: utf-8 -*-
"""
This program converts text.
User is asked to enter string.
User is asked to select either reverse or capitalize option. Select right option otherwise program does not convert text.
User can convert another text if wants.
"""
def converter(option, string):
    '''This function  '''
    if option == "B":
        word = string.capitalize()
        print("Capitalized string: \n\n", word)
    elif option == "A":
        word = "".join(reversed(string))
        print("Reversed string: \n\n", word)
    else:   
        print("You entered wrong letter just A and B is accepted!")
        
counter = 1
while counter == 1:
    string = str(input('Enter a string: '))
    option = input("What do you want to do with text? You can either reverse (press A) or capitalize (press B): \n")
    converter(option,string)
    counter = int(input("Do you want to convert another string? Press 1 otherwise press anything else: \n"))
else:
    print("We are finished!")
