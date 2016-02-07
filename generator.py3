def main():
	for f in inclusif_range(25):
		print(f)
     
def inclusif_range(*args):
	numArgs=len(args)
	if numArgs<1:raise TypeError ("You have to have at least one arguement")
	elif numArgs==1:
		start=0
		step=1
		stop=args[0]
	elif numArgs==2:
		(start,stop)=args
		step=1
	elif numArgs==3:
		(start,stop,step)=args
	else: raise TypeError("{} are not accepted,please use less than 3".format(numArgs))
	i = start
	while i <= stop:
		yield i
		i+=step

if __name__=="__main__":main()
