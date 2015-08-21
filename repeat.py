import sys

def rp():
	print ' '.join([sys.argv[1][:len(sys.argv[1])]] * int(sys.argv[2]))
	
