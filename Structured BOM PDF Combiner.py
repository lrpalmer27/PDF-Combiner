import os
import PyPDF2
import time

"""Program will error out if there is a pdf missing from the specified directory & will tell u which pdf is missing.
There will be no error if there are extra (unused) pdfs in the directory - assumes a complete BOM is provided"""

#Where are pdfs/What will be the new pdf name?
PATH=input("PATH to pdf folder")
os.chdir(PATH)#makes this code run in given directory(folder)
NewName=input("New file name?")

#Gets all part numbers
print("Copy & Paste Part Numbers now")
end='' #by clicking enter this loop will close
givenOrder=[]
for line in iter(input,end):
    givenOrder.append(line)

#Gets filenaming conventions to consider
jobNumber = "J" #input("Job Number: ")
salesNumber = "0" #input("Sales order number: ")
#other = input("Other: ") - DELETE HASHTAG AT START IF YOU START USING MORE FILENAMING CONVENTIONS

#makes a new list with only custom parts (No p-parts so effectivly no non-J# or SO# parts)
customOnly=[]
for i in givenOrder:
    if i.startswith(jobNumber):
        customOnly.append(i)
    elif i.startswith(salesNumber):
        customOnly.append(i)
    """elif: i.startswith(other): REMOVE THREE QUOTATIONS IF YOU USE MORE FILENAMING CONVENTIONS
        customOnly.append(i)"""

#Adds .idw.pdf to end of each item in the list - to follow vault filenaming conventions
orderWpdf =[]
for i in customOnly:
    orderWpdf.append(i+".idw.pdf")

#Check for missing/differnt filenames
    missingFiles =[]
for i in orderWpdf:
    if i not in os.listdir('.'):
        missingFiles.append(i)
        
if len(missingFiles) !=0:
    print("Missing or different files: ", missingFiles)
    input() #Holds windows program runner open until user input
    exit()
    
#Metrics starting values    
t0= time.time() #start code timer

#Does the actual combining
pdfWriter=PyPDF2.PdfFileWriter()
for filename in orderWpdf:
    pdfFileObj = open(filename,'rb')
    pdfReader =PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range (pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#CREATE NEW PDF & CLOSE PDF
PdfOutput = open(NewName+'.pdf','wb')
pdfWriter.write(PdfOutput)
PdfOutput.close()

t2=time.time()
deltaTime=(t2-t0)

#prints things to look at
print ("Number of PDFs combined: ", len(customOnly) )
print ("Code runtime: ", deltaTime)
print ((len(customOnly))/deltaTime,"PDFs combined per second")
print ("Number of P-parts/stock parts: ", ((len(givenOrder)) - (len(customOnly))))  
print (len(givenOrder), "Items in given list")
print (len(os.listdir('.')), "PDFs actually in directory")

    
print("The pdf package titled: ", NewName, "can be found in the directory: ", PATH)
