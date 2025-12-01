import sys
from functools import reduce
print(reduce(lambda x,y:(x[0]+((x[1]+y[1])%100==0),(x[1]+y[1])%100),[(0,int(t.replace('L','-').replace('R','')))for t in['50',*open(sys.argv[1]).readlines()]])[0])