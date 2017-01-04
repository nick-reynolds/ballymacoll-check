from urllib2 import Request, urlopen, URLError, HTTPError
import prowlpy

req = Request('http://www.ballymacollstud.com')
siteUp = True
errorText = 'No error found'

apikey = ''
p = prowlpy.Prowl(apikey)

try:
	response = urlopen(req)
	the_page = response.read()
except HTTPError as e:
    errorText = 'The server couldn\'t fulfill the request. Error code: ' + str(e.code)
    siteUp = False
except URLError as e:
    errorText = 'Failed to reach a server. Reason: ' + e.reason
    siteUp = False
else:
    # everything is fine
    i = the_page.find('<title>Ballymacoll Stud</title>')
    if i < 0:
    	errorText = 'Didn\'t find title'
    	siteUp = False
    	
if not siteUp:
	#send notification to prowl
	try:
		p.add('Ballymacoll Check','Server Down',"The Ballymacoll site is down. Error: " + errorText, 1, None, "http://www.ballymacollstud.com/")
		print 'Sent message to Prowl'
	except Exception,msg:
		print msg
	