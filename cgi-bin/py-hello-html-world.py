#!/usr/bin/python3
import socket
import datetime

now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("Cache-Control: no-cache\n")
print("Content-type: text/html\n\n")
print("<html><head><title> Hello World</title></head>"
    "<body><h1 align=center>Hello Python World</h1>"
    "<hr/>\n")

print("Hello World<br/>\n")
print(f"This program was generated at: {current_time}\n<br/>")
print(f"Your current IP address is: {ip}<br/>")
print("</body></html>")