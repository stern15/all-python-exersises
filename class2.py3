def main():
	donald=duck()
	donald.set_variable("color","blue")
	print(donald.get_variable("color"))
	
class duck():
	def __init__(self,**kwargs):
		self._variable=kwargs

	def set_variable(self,i,j):
		self._variable[i]=j

	def get_variable(self,i):
		return self._variable.get(i,None)


if __name__=="__main__":main()
