#!/usr/bin/env python

import os

def getVmState(id):
	result = os.popen('virsh list').readlines()
	vmresult = result[2]
	vmstates = vmresult.split(' ')
	vmid = int(vmstates[1])
	vmstate = vmstates[(len(vmstates)-1)]
	if vmid == id:
		return vmstate
	else:
		print 'The Domain is not normal'
	print 'getVmState'

if __name__ == '__main__':
	result = getVmState(2)
	print result
		
