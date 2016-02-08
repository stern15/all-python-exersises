class Duck:
 	def quack(self):
 		print("quaccckkkk")
 	def walk(self):
 		print("walk like a duck")
 	def bark(self):
 		print("the duck cant bark")
 	def fur (self):
 		print ("the duck has feathers")
class Dog:
	def bark(self):
		print("woof")
	def fur(self):
		print("i have brown and white fur")
	def quack(self):
 		print("dog cant quack")
 	def walk(self):
 		print("walk like a dog")
def in_forest(Dog):
	Dog.bark()
	Dog.fur()
def in_pond(Duck): 
	Duck.quack()
 	Duck.walk()

def main():
	donald=Duck()
	box=Dog()
	in_forest(donald)
 	in_pond(box)

if __name__=="__main__":main()