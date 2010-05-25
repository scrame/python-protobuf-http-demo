#!/usr/bin/python

import string

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from messages.square_messages_pb2 import square_input, square_output

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','application/x-protobuf')
        self.end_headers()
        contentlength = string.atoi(self.headers.getheader('content-length')) 
        data = self.rfile.read(contentlength) 
        input = square_input()
        input.ParseFromString(data)
        self.rfile.close()
        output = self.square_messages(input)
        self.wfile.write(output.SerializeToString())
        self.wfile.close()
        
    def square_messages(self,input):
        retval = square_output()
        retval.value = (input.value)*(input.value)
        return retval



def main():
    try:
        server = HTTPServer(('', 1234), MyHandler)
        print 'Welcome to the machine...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
