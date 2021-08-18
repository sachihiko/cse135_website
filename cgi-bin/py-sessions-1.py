#!/usr/bin/python3
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

print("Cache-Control: no-cache")
print("Content-type: text/html\n")
print("<html><head><title>Python Sessions</title></head><body>")
print("<h1>Python Sessions Page 1 </h1>")

name = form['username'].value

if name:
    print(f"<p><b>Name:</b> {name}")
else:
    print("<p><b>Name:</b> You do not have a name set</p>")

print("<br/><br/>")
print("<a href=\"/cgi-bin/py-sessions-2.py\">Session Page 2</a><br/>")
print("<a href=\"/py-cgiform.html\">Python CGI Form</a><br />")
print("<form style=\"margin-top:30px\" action=\"/cgi-bin/py-destroy-session.py\" method=\"get\">")
print("<button type=\"submit\">Destroy Session</button>")
print("</form>")

print("</body>")
print("</html>")