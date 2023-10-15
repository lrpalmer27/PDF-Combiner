import os
import PyPDF2
import time

"""Python will yeild an error if there is a pdf missing from the specified directory & will tell u which pdf is missing.
There will be no error if there are extra (unused) pdfs in the directory"""


#USER INPUT
PATH=input("PATH to pdf folder")
os.chdir(PATH)#makes this code run in given directory
NewName=input("New file name?")
metrics=input("Metrics? (Y)")
#Gets all part numbers
print("Copy & Paste Part Numbers now")
end='' #by clicking enter this loop will close
order=[]
for line in iter(input,end):
    order.append(line)

#Metrics starting values    
t0= time.time() # start code timer
countlist = 0


#Adds .pdf to end of each item in the list
orderWpdf =[]
for i in order:
    orderWpdf.append(i+".idw.pdf")
    countlist +=1

#Does the combining
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
deltatime=(t2-t0)

#prints things to look at
if metrics == "Y":
    directory= os.listdir('.')
    print ('Files in the specified directory:', directory)
    print ('Specified order:', order)
    print ('Specified order with .idw & .pdf at the end', orderWpdf)
    print ("Code runtime: ", deltatime)
    
    #PDFS in dir
    countpdf=-1
    for i in os.listdir('.'):
        countpdf+=1
        
    if countpdf!=countlist:
        print (countlist, "Items in original list")
        print (countpdf, "PDFs actually in directory")
    else:
        print (countlist, "PDFs combined")
        print (countlist/deltatime ,"PDFs per second")

 
print("The pdf package titled: ", NewName, "can be found in the directory: ", PATH)

