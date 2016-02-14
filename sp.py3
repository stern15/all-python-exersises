#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC
def main():
    text=open("lol.rtf","r")
    write=open("lolo.rtf","w")
    for line in text:
    	print(line,file = write, end="")
    print("done.")
if __name__ == "__main__": main()
