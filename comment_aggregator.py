from __future__ import print_function		#for printing python 3 style

#selenium_sandbox

BASE_URL = "https://www.regulations.gov/document?D=NHTSA-2016-0090-"
#add document number to complete url
#0001 is initial request page, 0002-1086 are comments submitted before period closed
#as of 12/23/16 13:03 EST the highest comment ID was 1125

from selenium import webdriver
import time

print("Launching Firefox...")
browser = webdriver.Firefox()		# create browser instance with Firefox

start = 43
stop = 100

def wait(seconds, purpose):
	if len(purpose) != 0:
		print("Waiting for " + purpose) 
	timeout = time.time() + seconds
	while time.time() < timeout:
		continue


print("Waiting for preferences to be set and Google homepage to be accessed...")

while(str(browser.current_url) != "about:preferences#content"):
	continue

#wait(45, "preferences to be set")		# wait for me to change browser settings
									# default save location and default pdf save behavior don't seem
									# to stick between instances of Firefox as initiated by Selenium


for id in range(start,stop):
	print("-----------------Loading comment page #" + str(id) + "-------------")
	if id%10 == 0:
		wait(5, "performance")		# pause execution every 10 pages, seems to improve performance
	#print "{",						# delimit comments with curly braces
	#print("Comment #" + str(id))	
	instanceURL = BASE_URL
	for i in range(4 - len(str(id))):
		instanceURL += "0"
	instanceURL += str(id)
	#print(str(id) + " : " + instanceURL)		#debug print
	#timeout = time.time() + 5					#10 second timeout for page gets
	print("Getting page...")
	# while time.time() < timeout:
	# 	try:
	browser.get(instanceURL)
	# 	wait(1,"")
	# except Exception, e:
	# 	print("Error getting page: " + str(e))
	timeout = time.time() + 20					#20 second timeout for page loads
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
			wait(10, "page to load...")

			elements = browser.find_elements_by_class_name('gwt-Anchor')
			elements = elements[11:]
			print("Found " + str(len(elements)) + " attachments")
			if len(elements) > 0:
				for element in elements:
					if "pdf" in str(element.get_attribute("href")):
						print("Downloading comment #" + str(id) + " attachment " + str(element.get_attribute("href"))[93:94])
						element.click()
					else:
						print("No PDF attachments found")

			break
		except Exception, e:
			print("Exception: " + str(e))
	#print "}"