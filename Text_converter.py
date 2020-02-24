# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:20:59 2020

@author: DELL
"""  
import argparse

def converter(inputed_string, option):
    ''' This function converts entered text'''
    if option == "A":
        reversed_string = "".join(reversed(inputed_string))
        print("A)Reversed text:" + reversed_string)
        #print("A) Capitalized string:\n" + capitalized_string)
    elif option == "B":
        capitalized_string = inputed_string.upper()
        print("B)Capitalized text:" +capitalized_string)
        #print("A) Reversed string:\n" + reversed_string)
    elif option == "C":
        reversed_string = "".join(reversed(inputed_string))
        capitalized_string = inputed_string.upper()
        print("A)Rever.:" + reversed_string + "\nB)Capit.:" + capitalized_string)
        # print("A) Reversed string:\n" + reversed_string +"\n" + "B) Capitalized string:\n" + capitalized_string)     
    else :
        print("Not listed option, try again!")
        
def main():
    '''Initialize parser, adding 2 arguments inside of parser, parse the arguments and call function converter '''
    parser = argparse.ArgumentParser(description="Convert entered string to reverse, upper or both")   
    parser.add_argument('-t', '--text', type=str, required = True,  help='Enter the text you wish to convert')
    parser.add_argument('-o','--option', type=str.upper, choices=["A","B","C"], help='(Optional) Enter reverse (A) or capitalize (B), default both (C)) ', default = "C")
    args = parser.parse_args()
    print("Input:" + args.text)
    print("Option:" + args.option)
    converter(args.text, args.option)
   
# Is this file being run directly by Python (main) or is it being imported(name of the file)?
if __name__ == '__main__':
 main()
    