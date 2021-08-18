#!/usr/bin/python3
import html
import os
import datetime

now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
client_ip = html.escape(os.environ["REMOTE_ADDR"])

print("Cache-Control: no-cache")
print("Content-type: application/json\n")
print("{\n\t\"message\": \"Hello Sachi\",")
print(f"\t\"date\": \"{current_time}\",")
print(f"\t\"currentIP\": \"{client_ip}\"")
print("}")