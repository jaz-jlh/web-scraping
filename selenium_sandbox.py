#selenium_sandbox

BASE_URL = "https://www.regulations.gov/document?D=NHTSA-2016-0090-"
#add document number to complete url
#0001 is initial request page, 0002-1086 are comments submitted before period closed
#as of 12/23/16 13:03 EST the highest comment ID was 1125

from selenium import webdriver
import time

browser = webdriver.Firefox()		# create browser instance with Firefox

for id in range(2,10):
	instanceURL = BASE_URL
	for i in range(4 - len(str(id))):
		instanceURL += "0"
	instanceURL += str(id)
	#print(str(id) + " : " + instanceURL)	#debug print
	browser.get(instanceURL)
	pageReady = 0
	while True:
		try:
			elements = browser.find_elements_by_tag_name('div')
			time.sleep(0.5)
			print("Author: " + elements[19].text)
			print("Date: " + elements[67].text)
			print("Comment: " + elements[28].text)
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