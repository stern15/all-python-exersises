import re

def main():
	stuff=open("raven.txt")
	pattern = re.compile("(Len|Neverm)ore",re.IGNORECASE)
	for line in stuff:
		if re.search(pattern,line):
			print(pattern.sub("#######",line))                      
if __name__=="__main__":main() 