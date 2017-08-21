'''
Created on 21-Aug-2017

@author: BALASUBRAMANIAM
'''
from PyPDF2 import PdfFileWriter, PdfFileReader

#output = PdfFileWriter()
input1 = PdfFileReader(open("API.pdf", "rb"))

# print the title of document1.pdf
print ("title = %s" % (input1.getDocumentInfo().title))
print ("Author = %s" % (input1.getDocumentInfo().author))
print ("Creator = %s" % (input1.getDocumentInfo().creator))
print ("Producer = %s" % (input1.getDocumentInfo().producer))

# print how many pages input1 has:
print ("API.pdf has %s pages." % input1.getNumPages())
print (input1.documentInfo)

output = PdfFileWriter()

output.addPage(input1.getPage(0))
responsiveInput = PdfFileReader(open("responsive-web-design-training.pdf",
                                      "rb"))
output.addPage(responsiveInput.getPage(0))
outputStream = open("new-document.pdf", "wb")
output.write(outputStream)
outputStream.close()


