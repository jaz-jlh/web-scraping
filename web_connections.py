# web connections
import requests
res = requests.get('https://google.com/')
try:
	res.raise_for_status()							# Good practice to halt the program if something goes wrong
except Exception as exc:
	print('There was a problem %s' % (exc))
print("Request returned status code: " + str(res.status_code))
print(str(len(res.text)))
print(res.text[:250])
