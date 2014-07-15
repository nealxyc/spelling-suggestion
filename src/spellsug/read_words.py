'''
Created on Jul 15, 2014

@author: NXIONG
'''
import os.path as path
import sys

words = set()
successful = False
def usage(fin=None):
    if fin:
        print "Invalid file path: {}".format(fin)
    else:
        print "Needs dictionary file path as the first argument."
    pass

def readWords():
    if len(sys.argv) < 2:
        usage()
    elif not path.isfile(sys.argv[1]):
        usage(sys.argv[1])
        
    else:
        with open(sys.argv[1], 'r') as fin:
            for line in fin.readlines():
                for word in line.split():
                    words.add(word)
            return True
    return False
                  
if __name__ == '__main__':
    if readWords():
        print words