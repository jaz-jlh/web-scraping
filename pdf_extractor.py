# pdf extractor
# extracts the text from the pdfs 

import PyPDF2
from os import listdir
from os.path import isfile, join

path = "/home/jaz/Dropbox/python/web-scraping/pdfs"

pdfs = [file for file in listdir(path) if isfile(join(path,f))]

for filename in pdfs:
	pdfFileObj = open(filename,'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	for page in range(pdfReader.numPages):
		pageObject = pdfRead.getPage(page)
		print("{" + filename)
		pageObject.extractText()
		print("}\n")