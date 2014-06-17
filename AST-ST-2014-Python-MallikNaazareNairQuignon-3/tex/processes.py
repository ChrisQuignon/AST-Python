#! /usr/bin/python
from multiprocessing import Process, Pool
import time
import glob

def function(n):
    return [[len(z),z] for z in n]

#SETUP
strips = list()
files = glob.glob('./txtfiles/*.txt')
for filename in files:
	bigfile=open(filename, 'r')
	line=bigfile.readlines()
	bigfile.close()
	for word in line:
		strips.append(word.strip())
print 'Processing ', len(strips), 'words takes :'
pool = Pool(processes=8)


runtime = time.time()
for strip in strips:
	function(strip)
print (time.time() - runtime), 'ms with bad serialisation'

#time.sleep(5)#wait for the processors to cool down
runtime = time.time()
map(function, [strips])
print (time.time() - runtime), 'ms with internal optimization'

#time.sleep(5)#wait for the processors to cool down
runtime = time.time()
result = pool.apply_async(function, [strips])
print (time.time() - runtime), 'ms in parallel'






