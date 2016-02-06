def main():
	x=dict(
	    one = 1,
		two = 2,
		three = 3,
		four = 4,
	)
	x["five"] = 5	
	for k in sorted(x.keys()):
		print(k,x[k])
if __name__ == "__main__": main()