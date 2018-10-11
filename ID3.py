from node import Node
from collections import Counter
import math

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
    out.label = targetCount.elements()[0]
    return out

  # calculate initial entropy

  # for each (remaining attribute), partition based on the attribute; 

  # find the attribute that results in the greatest reduction in entropy

  # change the label to None; change the attribute to the best attribute

  # Run ID3 on the partitioned examples, remembering to REMOVE from each, the attribute that has been split. For each new
  # tree created, remember to add the children based on the label of the examples. 

  #return the created node

  
  



def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

  # Initial strategy: Reduced error pruning

  

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples. Returns the accuracy (fraction
  of examples the tree classifies correctly). 
  '''


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
