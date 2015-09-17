import os, Tkinter, tkFileDialog, tkMessageBox, shutil, sys

#ask user what directory to search in for all the .TXT documents, then change working directory to that directory.
root = Tkinter.Tk()
dirName = tkFileDialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')
os.chdir(dirName)
print "Found correct directory"

#create new COMBINED-IMG.txt
combined = open("COMBINED-IMG.txt","w")
print "Completed creating COMBINED-IMG.txt"

#create empty array to store all .TXT names
textFiles = []

#appends all .TXT files to textFiles array
for file in os.listdir(dirName):
    if file.endswith(".TXT"):
        textFiles.append(file)
print "Created array of .TXT files"
    
#store the number of .TXT files into textFilesLength
textFilesLength = len(textFiles) 

#copy over first file to COMBINED-IMG.txt
shutil.copyfile(textFiles[0],"COMBINED-IMG.txt")
print "Copied first .TXT file to COMBINED-IMG.txt"

#this is the bread and butter. We find the last line of COMBINED-IMG.txt and find the number on that line, take that number, add it to a new line, then add that new line to COMBINED-IMG.txt. We loop until completion
for f in range(0,textFilesLength-1):
    #Open first file, read the number on the last line, save the number into a string, then into an integer
    with open("COMBINED-IMG.TXT", "r") as firstFile:
        firstData = firstFile.readlines()
        lastLine = firstData[len(firstData)-1]
        firstNumberString = ""
        for i in range(3,8):
            firstNumberString += lastLine[i]
        firstNumber = int(float(firstNumberString))
        print "Found firstNumber: " + firstNumberString

    #create a starting point for secondFile numbers (one more than the last number from firstFile)        
    secondNumber = firstNumber + 1        

    #Open second file, search for "DSC...", write that line to COMBINED-IMG.txt
    with open(textFiles[f+1],"r") as secondFile:
        for line in secondFile:
            #define currentNumberString as empty
            currentNumberString = ""
            # Create a string of secondNumber, then determine the length of that number
            secondNumberString = str(secondNumber)
            numberLength = len(secondNumberString)
            #find lines starting with "DSC"
            if "DSC" in line:
                #if the number is one digit, add the one digit to currentNumberString
                if numberLength == 1:
                    for i in range (7,8):
                        currentNumberString += line[i]
                #if the number is two digits, add the two digits to currentNumberString
                elif numberLength == 2:  
                    for i in range (6,8):
                        currentNumberString += line[i]
                #if the number is three digits, add the three digits to currentNumberString
                elif numberLength == 3:  
                    for i in range (5,8):
                        currentNumberString += line[i]
                #if the number is four digits, add the four digits to currentNumberString
                elif numberLength == 4:  
                    for i in range (4,8):
                        currentNumberString += line[i]
                #if the number is five digits, add the five digits to currentNumberString
                elif numberLength == 5:  
                    for i in range (3,8):
                        currentNumberString += line[i]
                #replace the current digits in the line with the new digits from secondNumberString, add one to secondNumber string, then write the new line to COMBINED-IMG.txt
                newLine = line.replace(currentNumberString, secondNumberString, 1)
                secondNumber += 1
                with open("COMBINED-IMG.txt", "a") as combined2:
                    combined2.write(newLine)
                    
#opens the folder that COMBINED-IMG.txt is located in, then terminates the program                    
def openFolder():
    os.startfile(dirName)
    sys.exit("Thanks for using Combiner!")
 
#button that when clicked will invoke openfolder().
B1 = Tkinter.Button(root, text = "Thanks for using Combiner! \n \n Click me to go to the folder!", padx = "100", pady = "100", command = openFolder)
B1.pack()
root.mainloop()

#Close the open file
combined.close()
