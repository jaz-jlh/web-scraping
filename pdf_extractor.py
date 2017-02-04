# pdf extractor
# extracts the text from the pdfs 

import PyPDF2
from os import listdir
from os.path import isfile, join

import send2trash

def extract_all_text(path):
	pdfs = [file for file in listdir(path) if isfile(join(path,file))]

	for filename in pdfs:
		pdfFileObj = open(path + filename,'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		print("{" + filename + ":\n")
		for page in range(pdfReader.numPages):
			pageObject = pdfReader.getPage(page)
			try:
				print((pageObject.extractText()).replace("\n",""))
			except:
				print("Error extracting text\n")
		print("}\n")

def clear_files(path):
	files = [file for file in listdir(path) if isfile(join(path,file))]
	for filename in files:
		#print(path + filename)
		send2trash.send2trash(path + filename)

#clear_files("/home/jaz/Dropbox/python/web-scraping/pdfs/")