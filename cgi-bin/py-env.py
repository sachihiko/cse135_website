#!/usr/bin/python3
import  os

print('Cache-Control: no-cache')
print('Content-type: text/html')
print()
print("<html><head><title>Environment Variables</title></head>"
	"<body><h1 align=center>Environment Variables</h1><hr/>")

for k, v in sorted(os.environ.items()):
    print(f"<b>{k}:</b> {v}<br/>")
print("</body></html>")
