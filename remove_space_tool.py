"""
By Jimmy Bowden
remove_space_tool.py
This is used to remove any extra spaces in a large string that is in the clipboard and then is pasted back in.
Primary use is to simplify the removal of extra spaces for SilverCloud Employees.
Recommended Shortcut is CTRL+SHFT+S
"""

import pyperclip
import re

#------------------------------Functions#------------------------------
#In order for this function to work, you need to already have something in your clipboard
def getInput():
    pyperInput = pyperclip.paste()
    return pyperInput


#This parses through the input (string) and takes out spaces
def parseInput(myInput):
    splitList = []
    finalString = ""
    cleanInput = str(myInput).replace("&nbsp;", " ") 
    splitList = cleanInput.split()
    for word in splitList:
        if finalString == "":
            finalString = word
        else:
            finalString = finalString + " " + word
    #regex = r"</\w*>\s*<"
    regex = r">\s*<"
    cleanFinalString = re.sub(regex, "><", finalString)
    return cleanFinalString
 
#------------------------------Main#------------------------------
def run_remove_spaces_tool():
    pyperInput = getInput()
    pyperclip.copy(parseInput(pyperInput))


if __name__ == '__main__':
	run_remove_spaces_tool()