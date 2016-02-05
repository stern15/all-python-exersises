# your code goes here
def main():
 	func(8)
 	func()
 	func(9)

def func(a=3):
	for i in range(a,20):
		print(i, end=" ")
	print()

if __name__== "__main__":main()

