#selenium_sandbox

BASE_URL = "https://www.regulations.gov/document?D=NHTSA-2016-0090-"

from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.get(BASE_URL + '0015')
time.sleep(5)
print("done sleeping")

try:
	elements = browser.find_elements_by_tag_name('div')



	# Code for identifying locations for Author, Date, and Comment Text
	# for i in range(len(elements)):
	# 	if "Michael" in ((elements[i]).text):
	# 		print("found submitter name at: " + str(i))
	# 	if "Date Posted" in ((elements[i]).text):
	# 		print("found date at: " + str(i))
	# 	if "fatalities" in ((elements[i]).text):
	# 		print("found message text at: " + str(i))
except:
	print("could not find elements")