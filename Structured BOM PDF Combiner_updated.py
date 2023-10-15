import os
import PyPDF2
import time
import easygui
import pandas
import re

def GetPartNumbers():
    ##this function gets filenames from the BOM
    path=easygui.fileopenbox("Choose Excel File of Filenames", "Parts only BOM list in column A")

    data=pandas.read_excel(path)
    print(data)
    AllParts=data['All'].tolist()
    print(AllParts)

    CustomParts=[]
    for it in AllParts:
        i=str(it)
        if i.startswith("J") or i.startswith("0"):
            CustomParts.append(i)

    return CustomParts

def GetMissing(BOMPARTS):
    All=os.listdir(PATH)
    remove=[]
    for i in ALL:
        item=re.sub(r"[\n\t\s\/\:\"]*", "", i)
        for b in BOMPARTS:
            bom=re.sub(r"[\n\t\s\/\:\"]*", "", b)
            if item==bom:
                remove.append(i)
                
    for r in remove:
        All.remove(r)

    if len(All)!=0:
        easygui.textbox("Add these pdfs now","Missing pdfs",'\n'.join(All))

def Combine(orderWpdf):
    pdfWriter=PyPDF2.PdfFileWriter()
    for f in orderWpdf:
        filename=f+".idw"
        try:
            pdfFileObj = open(filename,'rb')
        except:
            print("Could not open",filename)
            
        pdfReader =PyPDF2.PdfFileReader(pdfFileObj)
        for pageNum in range (pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    
"""Program will error out if there is a pdf missing from the specified directory & will tell u which pdf is missing.
There will be no error if there are extra (unused) pdfs in the directory - assumes a complete BOM is provided"""

PATH=easygui.diropenbox("Choose Folder with ALL component pdfs","Select Folder")
os.chdir(PATH)#makes this code run in given directory(folder)
NewName=easygui.enterbox("This will be the combined filename","Input New File Name")
AllParts=GetPartNumbers()
GetMissing(AllParts)
#Combine(AllParts)


"""
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
    elif: i.startswith(other): REMOVE THREE QUOTATIONS IF YOU USE MORE FILENAMING CONVENTIONS
        customOnly.append(i)

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
"""
