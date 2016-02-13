#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC
def main():
    text=open("utf8.txt","r",encoding="utf_8")
    read=open("utf8.html","w")
    outbites= bytearray()
    for line in text:
        for char in line:
            if ord(char) > 127:
                outbites+= bytes("&#{:04d};".format(ord(char)),encoding="utf_8") 
            else:
                outbites.append(ord(char))
    outstr = str(outbites,encoding="utf_8")
    print(outstr,file = read)
    print(outstr)
    print("done")

if __name__ == "__main__": main()
