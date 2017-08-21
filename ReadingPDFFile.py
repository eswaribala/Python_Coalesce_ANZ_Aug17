# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:34:13 2017

@author: BALASUBRAMANIAM
"""

from PyPDF2 import PdfFileWriter, PdfFileReader

#output = PdfFileWriter()
input1 = PdfFileReader(open("Ruby-lang.pdf", "rb"))

# print the title of document1.pdf
print ("title = %s" % (input1.getDocumentInfo().title))
# print how many pages input1 has:
print ("Ruby-lang.pdf has %s pages." % input1.getNumPages())



# add page 1 from input1 to output document, unchanged
#output.addPage(input1.getPage(0))
'''
# add page 2 from input1, but rotated clockwise 90 degrees
#output.addPage(input1.getPage(1).rotateClockwise(90))

# add page 3 from input1, rotated the other way:
#output.addPage(input1.getPage(2).rotateCounterClockwise(90))
# alt: output.addPage(input1.getPage(2).rotateClockwise(270))

# add page 4 from input1, but first add a watermark from another pdf:
page4 = input1.getPage(0)
watermark = PdfFileReader(open("responsive-web-design-training.pdf", "rb"))
page4.mergePage(watermark.getPage(0))

# add page 5 from input1, but crop it to half size:
page5 = input1.getPage(0)
page5.mediaBox.upperRight = (
    page5.mediaBox.getUpperRight_x() / 2,
    page5.mediaBox.getUpperRight_y() / 2
)
output.addPage(page5)


# finally, write "output" to document-output.pdf
outputStream = open("document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()

# a writer
writer=PdfFileWriter()
outfp=open("outpath.pdf",'wb')
writer.addPage(page5)
writer.write(outfp)
outfp.close()
'''