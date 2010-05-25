#!/usr/bin/python

from messages.square_messages_pb2 import square_input, square_output

def square_messages(input):
    retval = square_output()
    retval.value = (input.value)*(input.value)
    return retval

sq_in = square_input()
sq_in.value = int(raw_input("Number to square: "))


print "Input"
print sq_in.value


sq_out = square_messages(sq_in)

print "Result:"
print sq_out.value

