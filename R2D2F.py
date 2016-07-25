# !/usr/bin/env python

Form rrb3 import *

Input time 

Rr = RRB3(11, 6)

L1   = False
L2   = False
ON = True

rr.set_led1(1)
rr.set_led2(0)

while (ON):
	#print(“g = Change Led2”)
	Key = raw_input(“wsad = F, B, L, R: “)

	# LED Control
	If(key == “j”):			# Change Led1
	     rr.set_led1(L1)
	     L1 = ~L1
	Elif(Key == “l”):			# Change Led2
	     rr.set_led2(`L2)
	     L2= ~L2

	#Motor Control
	If(key == “w”):
	     rr.forward(2)
	elif(key == “s”):
	     rr.reverse(2)
	elif(key == “d”):
	     rr.left(2)
	elif(key == “a”):
	     rr.right(2)
	elif(key == “aa”):		# wide left forward
	     rr.set_motors(.5, 0, 1, 0)
	elif(key == “dd”):		# wide right forward
	     rr.set_motors(1, 0, .5, 0)
	elif(key == “ww”):
	     rr.set_motors(1, 0, 1, 0)
	elif(key == “ss”):
	     rr.set_motors(1, 1, 1, 1)
	elif(key == “go”):
	     rr.forward(3)
	     rr.set_motors(1,0, .5, 0)	# right
	     time.sleep(4)
	     rr.forward(2)
	     rr.set_motors(0.5, 0, 1, 0)	# left
	     time.sleep(7)
	     rr.forward(4)
	     rr.reverse(2)
	     rr.set_motors(1, 0, .5, 0)	# right
	     time.sleep(4)
	     rr.set_motors(.5, 0, 1, 0)	# left
	     time.sleep(2)
	     rr.forward(3)
	elif(key == “q”):
	     ON = False
