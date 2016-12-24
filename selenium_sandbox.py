#selenium_sandbox

BASE_URL = "https://www.regulations.gov/document?D=NHTSA-2016-0090-"
#add document number to complete url
#0001 is initial request page, 0002-1086 are comments submitted before period closed
#as of 12/23/16 13:03 EST the highest comment ID was 1125

from selenium import webdriver
import time

browser = webdriver.Firefox()		# create browser instance with Firefox

for id in range(1087,1125):
	if id%20 == 0:
		time.sleep(10)
	print "{",
	print("Comment #" + str(id))
	instanceURL = BASE_URL
	for i in range(4 - len(str(id))):
		instanceURL += "0"
	instanceURL += str(id)
	#print(str(id) + " : " + instanceURL)	#debug print
	browser.get(instanceURL)
	pageReady = 0
	timeout = time.time() + 15		#15 second timeout
	while time.time() < timeout:
		try:
			elements = browser.find_elements_by_tag_name('div')
			if(len(elements[19].text) < 2):
				continue;
			author = elements[19].text
			print("Author: " + author[13:])
			date = elements[67].text
			print("Date: " + date[13:])
			comment = elements[28].text
			print("Comment: " + comment[254:])
			
			# Code for identifying locations for Author, Date, and Comment Text
			# Author: 19		Date: 67		Comment: 28
			# for i in range(len(elements)):
			# 	if "Michael" in ((elements[i]).text):
			# 		print("found submitter name at: " + str(i))
			# 	if "Date Posted" in ((elements[i]).text):
			# 		print("found date at: " + str(i))
			# 	if "fatalities" in ((elements[i]).text):
			# 		print("found message text at: " + str(i))
			break;
		except:
			pageReady = 0
	print "}"