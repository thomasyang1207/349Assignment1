import node, parse, math
from ID3 import ID3, evaluate, test
from unit_tests import testPruning

def myTest1():
	data = [dict(a=1, b=0, Class=2), dict(a=1, b=1, Class=1), dict(a=2, b=0, Class=2), dict(a=2, b=1, Class=3), dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=3)]
	myNode = ID3(data, 0)
	print(myNode)
	print("Test 1: Success!")

def myTest2():
	data = [dict(a=1, b=0, Class=2), dict(a=1, b=1, Class=1), dict(a=2, b=0, Class=2), dict(a=2, b=1, Class=3), dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=3)]
	myTree = ID3(data, 0)
	myAttr = evaluate(myTree, dict(a=1, b=0))
	print("Tested attribute: ", myAttr)
	print("Test 2: Success!")

def myTest3():
	data = [dict(a=1, b=0, Class=2), dict(a=1, b=1, Class=1), dict(a=2, b=0, Class=2), dict(a=2, b=1, Class=3), dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=3)]
	myTree = ID3(data, 0)
	testResults = test(myTree, [dict(a=1, b=0, Class=2), dict(a=1, b=1, Class=1), dict(a=2, b=0, Class=2)])
	print("Test accuracy: ", testResults)
	print("Test 2: Success!")

def myTest4():
	testPruning()
	print("Test 4: Success (?)")

def houseVotesTest():
	print("houseVotesTest not implemented")

if __name__ == "__main__":
    myTest1()
    myTest2()
    myTest3()
    myTest4()
    houseVotesTest()
