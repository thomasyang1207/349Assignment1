class Node:
  def __init__(self):
    self.label = None #None for non-leaf branches; otherwise, label with the actual label
    self.children = {}
    self.attribute = None #None for leaf; attribute for actual; Attribute is a string. 

    self.misclassified = 0 #only used for testing... 

    #include information for pruning; if we find a contradictory test set; 

	# you may want to add additional fields here...