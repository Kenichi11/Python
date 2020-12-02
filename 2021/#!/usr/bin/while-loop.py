#!/usr/bin/env python 3
# save file as while-loop.py
count = 0
#while (check if this is true)
while(count < 256):
	print(str(count)+" ",end='')
	#print(str(count)+"")
	count = count + 1
	if(count % 20 == 0):
		print(" * ")
