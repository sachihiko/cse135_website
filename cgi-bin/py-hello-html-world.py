#!/usr/bin/python3
import html
import os
import datetime

now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
client_ip = html.escape(os.environ["REMOTE_ADDR"])
print('Cache-Control: no-cache')
print('Content-type: text/html')
print()
print(f'''
<html>
<head><title>Hello World - plz work</title></head>
<body>
<body><h1 align=center>Python says hello world</h1><hr/>

This program was generated at: {current_time}<br/>
Your current IP address is: {client_ip}<br/>
</body>
</html>
''')
