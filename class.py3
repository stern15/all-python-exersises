def main():
	donald=duck(123)
	victor=duck(33)
	donald.quack()
	donald.walk()
	victor.quack()
	victor.walk()
class duck:
	def __init__ (self,number):
		self.num=number
	def quack(self):
		print("Quaaaaack!!!",self.num)
	def walk(self):
		print("Walk like a duck",self.num)

if __name__=="__main__":main()