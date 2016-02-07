def main():
	testfunc(3,8,85,677,8999,778,889,one=1,two="lol",three="joke") 

def testfunc(num1,num2,num3,*args,**kwargs):
	print(num1,num2,num3)
	for i in args:
		print (i)
	for k in kwargs:
		print(k,kwargs[k])

if __name__=="__main__":main()

