#!/usr/bin/python3
import os
from urllib.parse import parse_qsl

print("Cache-Control: no-cache")
print("Content-type: text/html\n")
print("<html><head><title>GET Request Echo</title></head>"
	"<body><h1 align=center>GET Request Echo</h1><hr/>")

query_str = os.environ['QUERY_STRING']

print(f"<b>Query String:</b>  {query_str}<br/><br/>")
print("<table> Formatted Query String:")

if len(query_str) > 0:
    query_list = parse_qsl(query_str)
for k, v in query_list:
    print(f"<tr><td>{k}:</td><td>{v}</td></tr><br/>")
print("</table></body></html>")