#!/usr/bin/python

import httplib, urllib

from messages.square_messages_pb2 import square_input, square_output


input = square_input()
input.value = 18

params = input.SerializeToString()
headers = {"Content-type": "application/x-protobuf","Accept": "application/x-protobuf", "Content-length": len(str(params))}
conn = httplib.HTTPConnection("localhost:1234")
conn.request("POST", "/", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
conn.close()

output = square_output()
output.ParseFromString(data)

print output.value

