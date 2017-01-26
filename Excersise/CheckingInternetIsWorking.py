__author__ = 'Sanjay'
import urllib.request

def testInternet():
	try:
		urllib.request.urlopen("http://google.com", timeout=2)
		print ("Internet is Working!")
	except urllib.URLError:
		print ("No Internet Connection! Please contact your administrator!")

if __name__ == '__main__':
	testInternet()