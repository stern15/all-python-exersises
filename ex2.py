a, b = 0, 1
while a < 50:
    print(a)
    print(b)
    print("-----")
    a, b = b, a + b
print("Done")

doc = open("/Users/semasuka/Desktop/yeah.rtf")
for line in doc.readlines():
    print(line)