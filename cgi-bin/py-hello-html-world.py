#!/usr/bin/python3
import request
import datetime

now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
client_ip = request.environ.get('REMOTE_ADDR')
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
