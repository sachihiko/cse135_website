#!/usr/bin/python3
import os
from urllib.parse import parse_qsl

print("Cache-Control: no-cache")
print("Content-type: text/html\n")
print("<html><head><title>GET Request Echo</title></head>"
	"<body><h1 align=center>GET Request Echo</h1><hr/>")

query_str = os.environ['QUERY_STRING']

print(f"<b>Query  String:</b>  {query_str}\n")
if len(query_str) > 0:
    query_list = parse_qsl(query_str)
for k, v in query_list:
    print(f"{k}: {v}<br/>")
print("</body></html>")