"""
By Jimmy Bowden
remove_classes_tool.py
This is used to remove any extra spaces in a large string that is in the clipboard and then is pasted back in.
Primary use is to simplify the removal of extra spaces and for the removal of extra classes and spans for SilverCloud Employees.
This should be done before putting any extra styling in the content item or else it will be removed
Recommended Shortcut is CTRL+SHFT+A
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
    finalString2 = ""
    #this is the regex for the classes
    regex = r"\w*=\"(\w*: (\d*\.*\d*|\w*)%?;|\d*\.*\d*|\w*)%?\""
    #This is the regex for the spans
    regex2 = r"(<\/?span \w*=\"(\w*: (\d*\.*\d*|\w*)%?;|(\d*\.*\d*)|(\w*))%?\"*>|<\/?span\s*>)"
    #regex3 = r"</\w*>\s*<"
    regex3 = r">\s*<"
    cleanInput = str(myInput).replace("&nbsp;", " ") 
    splitList = cleanInput.split()
    for word in splitList:
        if finalString == "":
            finalString = re.sub(regex2, "", word)
        else:
            finalWord = re.sub(regex2, "", word)
            finalString = finalString + " " + finalWord
    secondSplit = finalString.split()
    for word in secondSplit:
        if finalString == "":
            finalString2 = re.sub(regex, "", word)
        else:
            finalWord = re.sub(regex, "", word)
            finalString2 = finalString2 + " " + finalWord

    finalString3 = re.sub(regex3, "><", finalString2)
    return finalString3[1:]
 


     
#------------------------------Main#------------------------------
def run_remove_classes_tool():
    pyperInput = getInput()
    pyperclip.copy(parseInput(pyperInput))


if __name__ == '__main__':
	run_remove_classes_tool()

    