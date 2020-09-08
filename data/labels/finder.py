import os
path = "./"
for f in os.listdir(path):
	if(os.path.isfile(os.path.join(path,f))):
		dis = open(f)
		for l in dis.readlines():
			a=l.split(' ')
			if(a[0]=='7'):
				print(f)