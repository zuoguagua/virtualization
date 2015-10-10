#!/usr/bin/env python

from os import popen

def is_empty(str):
	return str and str.strip()

def handleVcpuinfo():
	vcpuinfo = popen("virsh vcpuinfo 2")
	newresult = []
	for item in vcpuinfo:
		item.replace("\n","")
		newresult.append(item)
	
	result = []
	for item in newresult:
		newitem = is_empty(item)
		result.append(newitem)
	
	return result

def handleVcpuCount():
	myresult = handleVcpuinfo()
	count = 0
	newresult = []
	for item in myresult:
		newitem = item.split(":")
		newresult.append(newitem)
	for item in newresult:
		if item[0] == "VCPU":
			count+=1
	return count



if __name__ == "__main__":
	#result = handleVcpuinfo()
	#print result
	count = handleVcpuCount()
	print count

