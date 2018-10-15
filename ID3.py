from node import Node
from collections import Counter
from math import log2


def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"

  returns tree root (Node)
  '''
  out = Node()
  out.label = default
  if len(examples) == 0: 
    return out
  
  #Count of how many class types there are in total
  classification = [ex['Class'] for ex in examples]
  targetCount = Counter(classification)
  if len(examples[0]) <= 1:
    out.label = max(classification, key=targetCount.get)
    return out

  if len(targetCount) <= 1:
    out.label = [i for i in targetCount.keys()][0]
    return out

  # calculate initial entropy
  entropyFun = lambda ex, tC: sum([tC[key] / len(ex) * log2(len(ex) / tC[key]) for key in tC.keys()]);
  initialEntropy = entropyFun(examples, targetCount)

  # for each (remaining attribute), partition based on the attribute value; 
  attributeMaps = {}
  attributeEntropies = {}
  for attr in [i for i in examples[0].keys() if i != 'Class']: 
    attributeMaps[attr] = {}
    for ex in examples: 
      if ex[attr] in attributeMaps[attr]: attributeMaps[attr][ex[attr]].append(ex)
      else: attributeMaps[attr][ex[attr]] = [ex]

    attributeClassCount = {}
    for val, listOfExamples in attributeMaps[attr].items():
      attributeClassCount[val] = Counter([ex['Class'] for ex in listOfExamples])
    
    attributeEntropies[attr] = sum([len(attributeMaps[attr][val]) / len(examples) * (initialEntropy - entropyFun(attributeMaps[attr][val], count)) for val,count in attributeClassCount.items()])

  bestAttr = max(attributeEntropies, key=attributeEntropies.get)

  out.label = None
  out.attribute = bestAttr
  out.defaultChild = ID3([], max(classification, key=targetCount.get))
  for val,listOfExamples in attributeMaps[bestAttr].items():
    for ex in listOfExamples:
      del ex[bestAttr]
    tempCount = Counter([ex['Class'] for ex in listOfExamples])
    mode = max(tempCount, key=tempCount.get)
    out.children[val] = ID3(listOfExamples, mode)

  return out




def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

  

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples. Returns the accuracy (fraction
  of examples the tree classifies correctly). 
  '''
  return len([ex for ex in examples if ex['Class'] == evaluate(node, ex)]) / len(examples)




def evaluate(node, example):
  '''
  Takes in a tree and one example. Returns the Class value that the tree
  assigns to the example.
  '''
  curNode = node;
  while curNode.label == None:
    exampleValue = example.get(curNode.attribute,None)
    curNode = curNode.children.get(exampleValue, curNode.defaultChild)
  return curNode.label