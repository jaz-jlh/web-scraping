#selenium_sandbox

BASE_URL = "https://www.regulations.gov/document?D=NHTSA-2016-0090-"
#add document number to complete url
#0001 is initial request page, 0002-1086 are comments submitted before period closed
#as of 12/23/16 13:03 EST the highest comment ID was 1125

from selenium import webdriver
import time

from pdf_extractor import extract_text,clear_files

path = "/home/jaz/Dropbox/python/web-scraping/pdfs/"

browser = webdriver.Firefox()		# create browser instance with Firefox

start = 7
stop = 100

def wait(seconds):
	timeout = time.time() + seconds
	while time.time() < timeout:
		continue

wait(45)							# wait for me to change browser settings
									# default save location and default pdf save behavior don't seem
									# to stick between instances of Firefox as initiated by Selenium


for id in range(start,stop):
	if id%10 == 0:
		wait(5)					# pause execution every 20 pages, seems to improve performance
		#extract_text("/home/jaz/Dropbox/python/web-scraping/pdfs/")
		#clear_files("/home/jaz/Dropbox/python/web-scraping/pdfs/")
									# moves files to recycle bin
	#print "{",						# delimit comments with curly braces
	#print("Comment #" + str(id))	
	instanceURL = BASE_URL
	for i in range(4 - len(str(id))):
		instanceURL += "0"
	instanceURL += str(id)
	#print(str(id) + " : " + instanceURL)		#debug print
	browser.get(instanceURL)
	timeout = time.time() + 20					#15 second timeout for page loads
	while time.time() < timeout:
		try:
			# Extracts data and prints to terminal---------------------
			#elements = browser.find_elements_by_tag_name('div')		# div 19 contains the information we want
			# if(len(elements[19].text) < 2):
			# 	continue;
			# author = elements[19].text
			# print("Author: " + author[13:])
			# date = elements[67].text
			# print("Date: " + date[13:])
			# comment = elements[28].text
			# print("Comment: " + comment[254:])
			
			# Code for identifying locations for Author, Date, and Comment Text-----------
			# Author: 19		Date: 67		Comment: 28
			#for i in range(len(elements)):
				# Sample bits of text to identify desired data
				# if "Michael" in ((elements[i]).text):
				# 	print("found submitter name at: " + str(i))
				# if "Date Posted" in ((elements[i]).text):
				# 	print("found date at: " + str(i))
				# if "fatalities" in ((elements[i]).text):
				# 	print("found message text at: " + str(i))
			
			# wait for page to load
			wait(10)

			elements = browser.find_elements_by_class_name('gwt-Anchor')

			if len(elements) < 1:
				continue
			for i in range(len(elements)):
				if "pdf" in elements[i].get_attribute("href"):
					elements[i].click()

			break
		except:
			print("error downloading")
	#print "}"