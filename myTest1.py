import node, parse, math
from ID3 import ID3

def myTest1():
	data = [dict(a=1, b=0, Class=2), dict(a=1, b=1, Class=1),
          dict(a=2, b=0, Class=2), dict(a=2, b=1, Class=3),
          dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=3)]
	myNode = ID3(data, 0)
	print(myNode)
	print("Success!")

if __name__ == "__main__":
    myTest1()