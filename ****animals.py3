def main():
	donald=duck()
	chevro=dog()
	print(donald.sound())
	print(donald.walk())
class animal:
	def talk(self):
		print("i try to express myself")
	def walk(self):
		print("i try to walk as fast as i can")

class duck(animal):
	def sound(self):
		print("i quancckkkkk")
	def walk(self):
		#super().walk()
		print("i walk like a duck")

class dog(animal):
	def dog(self):
		print("i wuuufff")
	def walk(self):
		print("i galope")


if __name__=="__main__":main()