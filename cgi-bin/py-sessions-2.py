#!/usr/bin/python3
import os

print("Cache-Control: no-cache")
print("Content-type: text/html\n")
print("<html><head><title>Python Sessions</title></head><body>")
print("<h1>Python Sessions Page 2 </h1>")

# cookie = os.environ['HTTP_COOKIE']
cookie = os.environ.get('HTTP_COOKIE')
if cookie and cookie != 'destroyed':
    print(f'Cookie: {cookie}')
else:
    print('Cookie: None')

print("<br />")
print("<a href=\"/cgi-bin/py-sessions-1.py\">Session Page 1</a>")
print("<br />")
print("<a href=\"/py-cgiform.html\">Python CGI Form</a>")
print("<br /><br />")


print("<form action=\"/cgi-bin/py-destroy-session.py\" method=\"get\">")
print("<button type=\"submit\">Destroy Session</button>")
print("</form>")

print("</body>")
print("</html>")

