#!/usr/bin/python3
import os
import sys
# from urllib.parse import parse_qsl

print("Cache-Control: no-cache")
print("Content-type: text/html\n")
print("<html><head><title>General Request Echo</title></head>"
	"<body><h1 align=center>General Request Echo</h1><hr/>")
print(f"Protocol: {os.environ['SERVER_PROTOCOL']}<br/>")
print(f"Method: {os.environ['REQUEST_METHOD']}<br/>")
print(f"Message Body: {sys.stdin.read()}<br/>")
print("</body>")
print("</html>")