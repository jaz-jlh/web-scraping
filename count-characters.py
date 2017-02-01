#Imports
import requests, bs4


BASE_URL = "https://www.regulations.gov/document?D=NHTSA-2016-0090-"
#add document number to complete url
#0001 is initial request page, 0002-1086 are comments submitted before period closed
#as of 12/23/16 13:03 EST the highest comment ID was 1125


testURL = BASE_URL + "0015"
res = requests.get(testURL)
try:
	res.raise_for_status()							# Good practice to halt the program if something goes wrong
except Exception as exc:
	print('There was a problem %s' % (exc))
if res.status_code == 200:
	print("Successfully retrieved webpage!")
	print("Total characters in page: " + str(len(res.text)))
print(res.text)
